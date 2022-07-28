from lwaf import Client

lwaf = Client()
lwaf.login_by_nickname("nickname", "password")
lwaf.global_conversation_join()

@lwaf.event(type="gcnm")
def event(data):
    conversation_message = data["cm"]
    user = conversation_message["u"]
    lwaf.global_conversation_send_message(f"Привет, {user['n']}!")