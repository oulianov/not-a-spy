from phospho import Agent, Message

agent = Agent()

@agent.ask()
def myask(message):
    print(f"Your message was {message.content}, now I can do stuff in the background")

@agent.chat()
def mychat(message):
    return Message(f"Hello {message.content}!")
