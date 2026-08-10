class Prompt:
    def prompt_message(self):
        raise NotImplementedError
class chatbot_1(Prompt):
    def prompt_message(self):
        print("Hi from chatbot 1")
class chatbot_2(Prompt):
    def prompt_message(self):
        print("Hi from chatbot 2")
chat_1 = chatbot_1()
chat_2 = chatbot_2()
chat_1.prompt_message()
chat_2.prompt_message()
prompt = Prompt()
prompt.prompt_message()
