import hashlib


class Client:
	def __init__(self) -> None:
		self.key = "zakovskiy"

	def md5(self, string: str) -> str:
		return hashlib.md5(string.encode()).hexdigest()

	def md5Salt(self, string: str) -> str:
		for i in range(5):
			string = self.md5(f"{string}{self.key}")
		return string