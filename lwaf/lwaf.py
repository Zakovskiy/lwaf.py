import json
import requests
from .utils import md5hash, objects
from .abc_socket import SocketHandler


class Client(SocketHandler):
    def __init__(self, device_id: str = "libraryzakovskiy", version: str = "4.0") -> None:
        self.version: str = version

        self.device_id: str = device_id
        self.access_token: str = None
        self.user_id: str = None
        self.webApi = "http://185.188.183.144:5000/api/lwaf/"
        self.md5: md5hash.Client = md5hash.Client()

        SocketHandler.__init__(self, self)

    def config(self) -> dict:
        data = {
            "te": "cfg"
        }
        self.send_data(data)
        return self.get_data("cfg")

    def login_by_nickname(self, nickname: str, password: str, md5: bool = False) -> objects.Account:
        data = {
            "te": "asi",
            "tsi": "n",
            "did": self.device_id,
            "n": nickname,
            "pw": password if md5 else self.md5.md5Salt(password)
        }
        self.send_data(data)
        response = self.get_data("asi")
        if not response.get("e"):
            self.user_id = response["a"]["uid"]
            self.access_token = response["a"]["at"]
            return objects.Account(response["a"])
        raise Exception(response)

    def login_by_access_token(self, access_token: str) -> objects.Account:
        data = {
            "te": "asi",
            "tsi": "at",
            "did": self.device_id,
            "at": access_token
        }
        self.send_data(data)
        response = self.get_data("asi")
        if not response.get("e"):
            self.user_id = response["a"]["uid"]
            self.access_token = response["a"]["at"]
            return objects.Account(response["a"])
        raise Exception(response)

    def dashboard(self) -> objects.Account:
        data = {
            "te": "db",
            "v": self.version
        }
        self.send_data(data)
        response = self.get_data("db")
        if not response.get("e"):
            return objects.Account(response["a"])
        raise Exception(response)

    def sex_change(self, sex_type: int) -> dict:
        """
        
        **??????????????????**
            - sex_type : 
                0 - ??????????????
                1 - ??????????????
        """
        response = requests.get(f"{self.webApi}user/changeSex?token={self.access_token}&type={type}").json()
        return response

    def get_user(self, user_id: str) -> objects.User:
        response = requests.get(f"{self.webApi}user/get?token={self.access_token}&userId={user_id}").json()
        if response["success"]:
            return objects.User(response["user"])
        raise Exception(response)

    def friends_list(self, user_id: str) -> objects.FriendsList:
        response = requests.get(f"{self.webApi}friends/{user_id}/list?token={self.access_token}").json()
        if response["success"]:
            return objects.FriendsList(response["friends"])
        raise Exception(response)

    def friends_accept(self, friend_id: str) -> dict:
        response = requests.get(f"{self.webApi}friends/{friend_id}/accept?token={self.access_token}").json()
        return response

    def friends_add(self, user_id: str) -> dict:
        response = requests.get(f"{self.webApi}friends/add?token={self.access_token}&userId={user_id}").json()
        return response

    def friends_delete(self, friend_id: str) -> dict:
        response = requests.get(f"{self.webApi}friends/{friend_id}/delete?token={self.access_token}").json()
        return response

    def private_conversation_get_messages(self, friend_id: str, offset: int = 0, limit: int = 100) -> dict:
        response = requests.get(f"{self.webApi}privateConversation/{friend_id}/?token={self.access_token}&offset={offset}&limit={limit}").json()
        return response

    def private_conversation_send_message(self, friend_id: str, content: str, reply_message_id: str = "") -> None:
        response = requests.get(f"{self.webApi}privateConversation/{friend_id}/sendMessage?token={self.access_token}&content={content}&replyMessageId={reply_message_id}").json()
        return response

    def private_conversation_delete_message(self, friend_id: str, message_id: str) -> dict:
        response = requests.get(f"{self.webApi}privateConversation/{friend_id}/deleteMessage?token={self.access_token}&messageId={message_id}").json()
        return response

    def global_conversation_join(self) -> dict:
        data = {
            "te": "gcj"
        }
        self.send_data(data)
        return self.get_data("gcj")

    def global_conversation_left(self) -> dict:
        data = {
            "te": "gcl"
        }
        self.send_data(data)
        return self.get_data("gcl")

    def global_conversation_get_user_list(self) -> objects.PlayersList:
        data = {
            "te": "gcgul"
        }
        self.send_data(data)
        response = self.get_data("gcgul")
        if not response.get("e"):
            return objects.PlayersList(response["p"])
        raise Exception(response)

    def global_conversation_get_messages(self) -> objects.ConversationMessages:
        data = {
            "te": "gcgm"
        }
        self.send_data(data)
        response = self.get_data("gcgm")
        if not response.get("e"):
            return objects.ConversationMessages(response["cm"])
        raise Exception(response)

    def global_conversation_send_message(self, message: str, reply_message_id: str = "") -> None:
        data = {
            "te": "gcsm",
            "m": message,
            "rmid": reply_message_id
        }
        self.send_data(data)

    def get_room_list(self) -> dict:
        data = {
            "te": "rli",
        }
        self.send_data(data)
        return self.get_data("rli")

    def create_room(self, room_name: str, room_password: str, room_players_count: int = 4) -> dict:
        data = {
            "te": "rc",
            "rn": room_name,
            "rp": self.md5.md5Salt(room_password) if room_password else ""
        }
        self.send_data(data)
        return self.get_data("rc")

    def join_room(self, room_id: str, room_password: str = "") -> dict:
        data = {
            "te": "rj",
            "rp": self.md5.md5Salt(room_password) if room_password else "",
            "rid": room_id
        }
        self.send_data(data)
        return self.get_data("rj")

    def left_room(self) -> None:
        data = {
            "te": "rle"
        }
        self.send_data(data)

    def get_posts_list(self, author: str) -> dict:
        response = requests.get(f"{self.webApi}posts/getList?token={self.access_token}&author={author}").json()
        return response

    def get_post_info(self, post_id: str) -> dict:
        response = requests.get(f"{self.webApi}posts/{post_id}/get?token={self.access_token}").json()
        return response

    def room_send_message(self, message: str) -> None:
        data = {
            "te": "rsm",
            "m": message
        }
        self.send_data(data)

    def room_track_add(self, key: str) -> None:
        data = {
            "te": "rta",
            "k": key
        }
        self.send_data()

    def room_track_set_reaction(self, type: int) -> None:
        """
        
        **??????????????????**
            - type : 
                1 - ????????
                2 - ??????????????
                3 - ??????????????????
        """
        data = {
            "te": "rtsr",
            "t": type
        }
        self.send_data(data)

    def admin_get_reports(self) -> dict:
        data = {
            "te": "agr"
        }
        self.send_data(data)
        return self.send_data("agr")

    def admin_close_report(self, report_id: str) -> dict:
        data = {
            "te": "acr",
            "rid": report_id
        }
        self.send_data(data)
        return self.send_data("acr")

    def admin_ban_user(self, user_id: str, timestamp: int) -> dict:
        data = {
            "te": "abu",
            "uid": user_id,
            "ts": timestamp
        }
        self.send_data(data)
        return self.send_data("abu")

    def admin_kick_user(self, user_id: str) -> dict:
        data = {
            "te": "aku",
            "uid": user_id,
        }
        self.send_data(data)
        return self.send_data("aku")

    def admin_get_clients(self) -> dict:
        data = {
            "te": "agc",
        }
        self.send_data(data)
        return self.send_data("agc")

    def admin_delete_user_from_server(self, user_id: str) -> dict:
        data = {
            "te": "adufs",
            "uid": user_id
        }
        self.send_data(data)
        return self.send_data("adufs")

    def admin_database(self, request: str) -> dict:
        data = {
            "te": "adb",
            "adbr": request
        }
        self.send_data(data)
        return self.get_data("adb")

    def post_set_reaction(self, post_id: str, reaction_type: int = 1):
        response = requests.get(f"{self.webApi}posts/{post_id}/setReaction?token={self.access_token}&reactionType={reactionType}").json()
        return response

    def post_get_comments(self, post_id: str):
        data = {
            "te": "pgc",
            "pid": post_id,
        }
        self.send_data(data)
        return self.get_data("pgc")

    def wheel_spin(self) -> dict:
        data = {
            "te": "ws"
        }
        self.send_data(data)
        return self.get_data("ws")

    def report_user_send(self, to_id: str, content: str) -> dict:
        data = {
            "te": "rus",
            "c": content,
            "tid": to_id
        }
        self.send_data(data)
        return self.get_data("rus")

    def report_message_send(self, message_id: str) -> dict:
        data = {
            "te": "rms",
            "mid": message_id,
        }
        self.send_data(data)
        return self.get_data("rms")

    def save_favorite_track(self, key: str) -> dict:
        data = {
            "te": "sftr",
            "k": key
        }
        self.send_data(data)
        return self.send_data("sftr")

    def remove_favorite_track(self) -> dict:
        data = {
            "te": "rftr",
        }
        self.send_data(data)
        return self.send_data("rftr")

    def loto_send_numbers(self, numbers: str) -> dict:
        data = {
            "te": "lsn",
            "ln": numbers
        }
        self.send_data(data)
        return self.send_data("lsn")

    def change_nickname(self, nickname: str) -> dict:
        data = {
            "te": "cn",
            "n": nickname
        }
        self.send_data(data)
        return self.send_data("cn")

    def change_about(self, about: str) -> dict:
        response = requests.get(f"{self.webApi}user/changeAbout?token={self.access_token}&about={about}").json()
        return response

    def change_confidentiality(self, type: str) -> dict:
        data = {
            "te": "cc",
            "t": type
        }
        self.send_data(data)
        return self.send_data("cc")

    def get_rating(self) -> dict:
        data = {
            "te": "gr",
        }
        self.send_data(data)
        return self.send_data("gr")
