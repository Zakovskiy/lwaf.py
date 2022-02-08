# Первый бот на lwaf.py

Добро пожаловать в первую часть туториала, здесь будет представлено как можно взаимодействовать с `Client`

Для начала работы с апи следует импортировать нужный объект - `lwaf.Client`

```python
from lwaf import Client
```

`Client` - готовый инструмент для того, чтобы делать запросы к апи LWAF

## Первый запрос

Для того чтобы инициализировать `Client` вам понадобится передать аргументы `nickname` и `password`

Напишем само взаимодействие:

```python
lwaf = Client("nickname", "password")
lwaf.global_conversation_join()
```

С помощью этого запроса, пользователь вступит в глобальный чат

Вот, что должно получиться в итоге:

```python
from lwaf import Client

lwaf = Client("nickname", "password")
lwaf.global_conversation_join()
```

Поздравляю, теперь вы умеете работать с запросами!

## Первый бот


```python
from lwaf import Client

lwaf = Client("nickname", "password")
lwaf.global_conversation_join()

@lwaf.event(type="gcnm")
def event(data):
    conversation_message = data["cm"]
    user = conversation_message["u"]
    lwaf.global_conversation_send_message(f"Привет, {user['n']}!")
```

Разберем новый код построчно:

`@lwaf.event(type="gcnm")` - это декоратор, он означает, что если событие будет отвечать заданным правилам (`type="gcnm"`), сработает хендлер под декоратором

`def event(data)` - объявление хендлера, `event` - название функции, может быть разумно любым, `data` - аргумент, который обязательно вернется в хендлер, нужный для получения информации о событии

`conversation_message = data["cm"]` - получение информации о новом сообщение

`user = conversation_message["u"]` - получение информации о пользователе, написавшем сообщение

`lwaf.global_conversation_send_message(f"Привет, {user['n']}!")` - отправка сообщения в чат с пользователем

## Экзамплы по этой части туториала

* [easy-bot](https://github.com/Zakovskiy/lwaf.py/tree/main/examples/easy_bot.py)
