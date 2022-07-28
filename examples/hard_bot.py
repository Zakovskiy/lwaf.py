from lwaf import Client
import random

lwaf = Client()
lwaf.login_by_nickname("nickname", "password")

lwaf.global_conversation_join()

@lwaf.event(type="gcnm")
def event(data):
    conversation_message = data["cm"]
    message_type = conversation_message["t"]
    message_id = conversation_message["mid"]
    user = conversation_message["u"]

    if message_type == 1:
        message = conversation_message["m"].lower()
        args = message.split()

        if args[0] == "!тест":
            lwaf.global_conversation_send_message("Я работаю!", message_id)
        elif args[0] == "!кто":
            users = lwaf.global_conversation_get_user_list()
            random_user = random.choice(users)
            
            lwaf.global_conversation_send_message(f"Я думаю, это - {random_user.nickname}!", message_id)
