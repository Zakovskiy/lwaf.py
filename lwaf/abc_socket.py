import socket
import json
import threading


class SocketHandler:
    def __init__(self, client: object) -> None:
        self.address: str = "185.188.183.144"
        self.port: int = 5555
        
        self.client = client
        self.data: list = []
        self.handlers: dict = {"te": [], "rte": []}

        self.alive: bool = False
        self.create_connection()

    def create_connection(self) -> None:
        self.alive = True
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.address, self.port))
        threading.Thread(target=self._listener).start()

    def _listener(self) -> None:
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
                        data = json.loads(str.strip())
                        type = "rte" if data.get("te", "rte") == "rte" else "te"
                        if data.get(type) in self.handlers[type]:
                            for handler in self.handlers[type]:
                                handler(data)
                        else:
                            self.data.append(data)
                else:
                    buffer = buffer + r
            else:
                self.alive = False

    def send_data(self, content: dict) -> None:
        self.client_socket.sendall((json.dumps(content)+"\n").encode("utf-8"))

    def listen(self) -> dict:
        while len(self.data) <= 0:
            pass
        res = self.data[0]
        del self.data[0]
        return res

    def get_data(self, type: str, format: str = "te") -> dict:
        while self.alive:
            if not self.data:
                continue
            data = self.data[-1]
            if data.get(format, "error") not in [type, "error"]:
                continue
            del self.data[-1]
            return data

    def event(self, type: str = None, format: str = "te") -> object:
        def register_handler(handler):
            if type in self.handlers[format]:
                self.handlers[format][type].append(handler)
            else:
                self.handlers[format][type] = [handler]
            return handler
        return register_handler