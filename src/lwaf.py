import socket
import json
import threading
from utils import md5hash, objects

class Client:

    def __init__(self, nickname: str, password: str, device_id: str = "libraryzakovskiy"):
        self.address = "185.188.183.144"
        self.port = 5555

        self.device_id = device_id
        self.access_token = None
        self.user_id = ""

        self.md5 = md5hash.Client()

        self.data = []

        self.alive = False
        self.create_connection()

        if nickname and password: self.login_by_nickname(nickname, password)

    def login_by_nickname(self, nickname: str, password: str):
        data = {
            "te": "asi",
            "tsi": "n",
            "did": self.device_id,
            "n": nickname,
            "pw": self.md5.md5Salt(password)
        }
        self.send_data(data)
        response = self.listen()
        if not response.get("e"):
            self.user_id = response["a"]["uid"]
            self.access_token = response["a"]["at"]
            return objects.Account(response["a"])
        print(f"[DEBUG] [LWAF] Error login >> {response}")

    def login_by_access_token(self, access_token: str):
        data = {
            "te": "asi",
            "tsi": "at",
            "did": self.device_id,
            "at": access_token
        }
        self.send_data(data)
        response = self.listen()
        if not response.get("e"):
            return objects.Account(response["a"])
        print(f"[DEBUG] [LWAF] Error login >> {response}")

    def dashboard(self, app_version: str = "1.0"):
        data = {
            "te": "db",
            "v": app_version
        }
        self.send_data(data)
        response = self.listen()
        if not response.get("e"):
            return objects.Account(response["a"])
        return response

    def sex_change(self, sex_type: int):
        """
        
        **Параметры**
            - sex_type : 
                0 - мужской
                1 - женский
        """
        data = {
            "te": "sc",
            "st": sex_type
        }
        self.send_data(data)
        return self.listen()

    def get_user(self, user_type: str, content: str):
        """
        **Параметры**
            - user_type : 
                n - получение информации по никнейму
                uid - получение информации по user_id
            - content : никнейм или user_id (в зависимости от user_type)
        """
        data = {
            "te": "gu",
            "ut": user_type,
            "c": content
        }
        self.send_data(data)
        response = self.listen()
        if not response.get("e"):
            return objects.User(response["u"])
        return response

    def friend_list(self, user_id: str):
        data = {
            "te": "fli",
            "uid": user_id
        }
        self.send_data(data)
        response = self.listen()
        if not response.get("e"):
            return objects.FriendList(response["fli"])
        return response

    def private_conversation_join(self, friend_id: str):
        data = {
            "te": "pcj",
            "fid": friend_id
        }
        self.send_data(data)
        return self.listen()

    def private_conversation_get_messages(self, friend_id: str):
        data = {
            "te": "pcgm",
            "fid": friend_id
        }
        self.send_data(data)
        return self.listen()

    def private_conversation_send_message(self, friend_id: str, message: str, reply_message_id: str):
        data = {
            "te": "pcsm",
            "fid": friend_id,
            "m": message,
            "rmid": reply_message_id
        }
        self.send_data(data)
        return self.listen()

    def private_conversation_delete_message(self, friend_id: str, message_id: str = ""):
        data = {
            "te": "pcdm",
            "fid": friend_id,
            "mid": message_id
        }
        self.send_data(data)
        return self.listen()

    def global_conversation_join(self):
        data = {
            "te": "gcj"
        }
        self.send_data(data)
        return self.listen()

    def global_conversation_get_user_list(self):
        data = {
            "te": "gcgul"
        }
        self.send_data(data)
        response = self.listen()
        if not response.get("e"):
            return objects.PlayersList(response["p"]).players
        return response

    def global_conversation_get_messages(self):
        data = {
            "te": "gcgm"
        }
        self.send_data(data)
        response = self.listen()
        if not response.get("e"):
            return objects.ConversationMessages(response["cm"]).cm
        return response

    def global_conversation_send_message(self, message: str, reply_message_id: str = ""):
        data = {
            "te": "gcsm",
            "m": message,
            "rmid": reply_message_id
        }
        self.send_data(data)
        return self.listen()

    def get_room_list(self):
        data = {
            "te": "gu",
        }
        self.send_data(data)
        return self.listen()

    def create_room(self, room_name: str, room_password: str, room_players_count: int = 4):
        data = {
            "te": "rc",
            "rn": room_name,
            "rp": self.md5.md5Salt(room_password)
        }
        self.send_data(data)
        return self.listen()

    def join_room(self, room_id: str, room_password: str = ""):
        data = {
            "te": "rj",
            "rp": self.md5.md5Salt(room_password),
            "rid": room_id
        }
        self.send_data(data)
        return self.listen()

    def get_posts_list(self):
        data = {
            "te": "pgl"
        }
        self.send_data(data)
        return self.listen()

    def get_post_info(self, post_id):
        data = {
            "te": "pgi",
            "pid": post_id
        }
        self.send_data(data)
        return self.listen()

    def room_send_message(self, message: str):
        data = {
            "te": "rsm",
            "m": message
        }
        self.send_data(data)
        return self.listen()

    def room_track_add(self, key: str):
        data = {
            "te": "rta",
            "k": key
        }
        self.send_data()
        return self.listen()

    def room_track_set_reaction(self, type: int):
        """
        
        **Параметры**
            - type : 
                1 - лайк
                2 - дизлайк
                3 - суперлайк
        """
        data = {
            "te": "rtsr",
            "t": type
        }
        self.send_data(data)
        return self.listen()

    def create_connection(self):
        self.alive = True
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.address, self.port))
        threading.Thread(target=self._listener).start()

    def _listener(self):
        buffer = bytes()
        while self.alive:
            r = self.client_socket.recv(2048)
            read = len(r)
            if read != 0:
                i = read - 1
                if r[i] == 10:
                    buffer = buffer + r
                    d = buffer.decode()
                    buffer = bytes()
                    for str in d.strip().split("\n"):
                        self.data.append(str.strip())
                else:
                    buffer = buffer + r
            else:
                self.alive = False

    def send_data(self, content:list):
        self.client_socket.sendall((json.dumps(content)+"\n").encode("utf-8"))

    def listen(self):
        while len(self.data) <= 0:
            pass
        res = self.data[0]
        del self.data[0]
        return json.loads(res)

    def event(self, type: str = None):
        def handler(function):
            while self.alive:
                recv = self.listen()
                if recv.get("te") == type or not type:
                    function(recv)
                else:
                    continue
        return handler

if __name__ == "__main__":

    lwaf = Client("Team LWAF", "4719zx")