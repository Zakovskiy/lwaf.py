class Account:
    def __init__ (self, data: dict) -> None:
        self.json: dict = data
        self.user_id: str = data.get("uid")
        self.nickname: str = data.get("n")
        self.lvl: int = data.get("l")
        self.balance: int = data.get("b")
        self.likes: int = data.get("li")
        self.dislikes: int = data.get("di")
        self.tracks: int = data.get("tr")
        self.superlikes: int = data.get("sli")
        self.sex: int = data.get("s")
        self.role: int = data.get("r")
        self.wheel_count: int = data.get("wc")
        self.wheel_timestamp: int = data.get("wts")
        self.time_ban: int = data.get("tb")
        self.favorite_track: str = data.get("ftr")
        self.last_tracks: list = data.get("ltr")
        self.access_token: str = data.get("at")
        self.device_id: str = data.get("did")
        self.vk_id: int = data.get("vid")
        self.about: str = data.get("a")
        self.hide_balance: bool = data.get("hb")
        self.hide_friends: bool = data.get("hf")
        self.hide_last_tracks: bool = data.get("hlt")
        self.last_seen: int = data.get("ls")
        self.mail: str = data.get("ma")

class User:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.user_id: str = data.get("uid")
        self.nickname: str = data.get("n")
        self.lvl: int = data.get("l")
        self.balance: int = data.get("b")
        self.likes: int = data.get("li")
        self.dislikes: int = data.get("di")
        self.tracks: int = data.get("tr")
        self.superlikes: int = data.get("sli")
        self.sex: int = data.get("s")
        self.role: int = data.get("r")
        self.wheel_count: int = data.get("wc")
        self.wheel_timestamp: int = data.get("wts")
        self.time_ban: int = data.get("tb")
        self.favorite_track: str = data.get("ftr")
        self.last_tracks: list = data.get("ltr")
        self.friend_id: str = data.get("fid")
        self.friend_type: int = data.get("ft")
        self.ranks: list = []
        for rank in data.get("rs", []):
            self.ranks.append(Rank(rank))

class Rank:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.rank_id: int = data.get("rid")
        self.title: str = data.get("t")
        self.background_color: str = data.get("bgc")
        self.icon_link: str = data.get("il")

class FriendList:
    def __init__(self, data: list) -> None:
        self.json: list = data
        self.friend_list: list = []
        for friend in data:
            self.friend_list.append(Friend(friend))

class Friend:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.friend_id: str = data.get("fid")
        self.friend_type: int = data.get("ft")
        self.last_message: Message = Message(data.get("lm"))
        self.user: User = User(data.get("u"))

class Message:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.message_id: str = data.get("mid")
        self.message: str = data.get("m")
        self.type: int = data.get("t")
        self.timestamp: int = data.get("ts")
        self.user_id: str = data.get("uid")
        self.user: User = User(data.get("u"))

class PlayersList:
    def __init__(self, data: list) -> None:
        self.players: [Player] = []
        for player in data:
            self.players.append(Player(player))

class Player:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.user_id: str = data.get("uid")
        self.nickname: str = data.get("n")
        self.lvl: int = data.get("l")
        self.balance: int = data.get("b")
        self.likes: int = data.get("li")
        self.dislikes: int = data.get("di")
        self.tracks: int = data.get("tr")
        self.superlikes: int = data.get("sli")
        self.sex: int = data.get("s")
        self.role: int = data.get("r")
        self.wheel_count: int = data.get("wc")
        self.wheel_timestamp: int = data.get("wts")
        self.time_ban: int = data.get("tb")
        self.favorite_track: str = data.get("ftr")
        self.last_tracks: str = data.get("ltr")

class ConversationMessages:
    def __init__(self, data: list) -> None:
        self.cm: [Message] = []
        for message in data:
            self.cm.append(Message(message))