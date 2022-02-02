

class Account:

    def __init__ (self, data: dir):
        self.json = data
        self.user_id = data["uid"]
        self.nickname = data["n"]
        self.lvl = data["l"]
        self.balance = data["b"]
        self.likes = data["li"]
        self.dislikes = data["di"]
        self.tracks = data["tr"]
        self.superlikes = data["sli"]
        self.sex = data["s"]
        self.role = data["r"]
        self.wheel_count = data["wc"]
        self.wheel_timestamp = data["wts"]
        self.wheel_timestamp = data["wts"]
        self.time_ban = data["tb"]
        self.favorite_track = data["ftr"]
        self.last_tracks = data["ltr"]
        self.access_token = data["at"]
        self.device_id = data["did"]
        self.vk_id = data["vid"]

class User:

    def __init__(self, data: dir):
        self.json = data
        self.user_id = data.get("uid")
        self.nickname = data.get("n")
        self.lvl = data.get("l")
        self.balance = data.get("b")
        self.likes = data.get("li")
        self.dislikes = data.get("di")
        self.tracks = data.get("tr")
        self.superlikes = data.get("sli")
        self.sex = data.get("s")
        self.role = data.get("r")
        self.wheel_count = data.get("wc")
        self.wheel_timestamp = data.get("wts")
        self.wheel_timestamp = data.get("wts")
        self.time_ban = data.get("tb")
        self.favorite_track = data.get("ftr")
        self.last_tracks = data.get("ltr")
        self.friend_id = data.get("fid")
        self.friend_type = data.get("ft")
        self.ranks = []
        for rank in data.get("rs", []):
            self.ranks.append(Rank(rank))

class Rank:

    def __init__(self, data: dir):
        self.json = data
        self.rank_id = data["rid"]
        self.title = data["t"]
        self.background_color = data["bgc"]
        self.icon_link = data["il"]

class FriendList:

    def __init__(self, data: list):
        self.json = data
        self.friend_list = []
        for friend in data:
            self.friend_list.append(Friend(friend))

class Friend:

    def __init__(self, data: dir):
        self.json = data
        self.friend_id = data["fid"]
        self.friend_type = data["ft"]
        self.last_message = Message(data["lm"])
        self.user = User(data["u"])

class Message:

    def __init__(self, data: dir):
        self.json = data
        self.message_id = data.get("mid")
        self.message = data.get("m")
        self.type = data.get("t")
        self.timestamp = data.get("ts")
        self.user_id = data.get("uid")
        self.user = User(data.get("u"))

class PlayersList:

    def __init__(self, data: list):
        self.players = []
        for player in data:
            self.players.append(Player(player))

class Player:

    def __init__(self, data: dir):
        self.json = data
        self.user_id = data.get("uid")
        self.nickname = data.get("n")
        self.lvl = data.get("l")
        self.balance = data.get("b")
        self.likes = data.get("li")
        self.dislikes = data.get("di")
        self.tracks = data.get("tr")
        self.superlikes = data.get("sli")
        self.sex = data.get("s")
        self.role = data.get("r")
        self.wheel_count = data.get("wc")
        self.wheel_timestamp = data.get("wts")
        self.wheel_timestamp = data.get("wts")
        self.time_ban = data.get("tb")
        self.favorite_track = data.get("ftr")
        self.last_tracks = data.get("ltr")

class ConversationMessages:

    def __init__(self, data: list):
        self.cm = []
        for message in data:
            self.cm.append(Message(message))