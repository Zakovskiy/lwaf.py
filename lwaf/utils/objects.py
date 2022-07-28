class Account:
    def __init__ (self, data: dict) -> None:
        self.json: dict = data
        self.user_id: str = data.get("id")
        self.nickname: str = data.get("nickname")
        self.balance: int = data.get("balance")
        self.likes: int = data.get("likes")
        self.dislikes: int = data.get("dislikes")
        self.tracks: int = data.get("tracks")
        self.superlikes: int = data.get("superLikes")
        self.sex: int = data.get("sex")
        self.role: int = data.get("role")
        self.wheel_count: int = data.get("wheelcount")
        self.wheel_timestamp: int = data.get("wheeltimestamp")
        self.time_ban: int = data.get("ban_time")
        self.favorite_track: str = data.get("favorite_track")
        self.last_tracks: list = data.get("last_tracks")
        self.access_token: str = data.get("token")
        self.device_id: str = data.get("did")
        self.vk_id: int = data.get("vkId")
        self.about: str = data.get("about")
        self.hide_balance: bool = data.get("hide_balance")
        self.hide_friends: bool = data.get("hide_friends")
        self.hide_last_tracks: bool = data.get("hide_lt")
        self.last_seen: int = data.get("last_seen")

class User:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.user_id: str = data.get("id")
        self.nickname: str = data.get("nickname")
        self.balance: int = data.get("balance")
        self.likes: int = data.get("likes")
        self.dislikes: int = data.get("dislikes")
        self.tracks: int = data.get("track")
        self.superlikes: int = data.get("superLikes")
        self.sex: int = data.get("sex")
        self.role: int = data.get("role")
        self.wheel_count: int = data.get("wheelcount")
        self.wheel_timestamp: int = data.get("wheeltimestamp")
        self.time_ban: int = data.get("ban_time")
        self.favorite_track: str = data.get("favorite_track")
        self.last_tracks: list = data.get("last_tracks")
        self.friend_id: str = data.get("friendId")
        self.friend_type: int = data.get("friendType")
        self.ranks: list = []
        for rank in data.get("ranks", []):
            self.ranks.append(Rank(rank))

class Rank:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.rank_id: int = data.get("rank_id")
        self.title: str = data.get("title")
        self.background_color: str = data.get("background_color")
        self.icon_link: str = data.get("icon_link")

class FriendsList:
    def __init__(self, data: list) -> None:
        self.json: list = data
        self.friend_list: list = []
        for friend in data:
            self.friend_list.append(Friend(friend))

class Friend:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        self.friend_id: str = data.get("friendId")
        self.friend_type: int = data.get("friendType")
        self.last_message: Message = Message(data.get("lastMessage", {}))
        self.user: User = User(data.get("user", {}))

class Message:
    def __init__(self, data: dict) -> None:
        self.json: dict = data
        print(data)
        self.message_id: str = data.get("message_id")
        self.content: str = data.get("content")
        self.type: int = data.get("type")
        self.timestamp: int = data.get("timesend")
        self.user_id: str = data.get("user_id")
        self.friend_id: str = data.get("friend_id")
        self.user: User = User(data.get("user", {}))

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