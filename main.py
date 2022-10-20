from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Chat_Bot_Name')

conversation = ['Hi', 'Hello', 'How are you?', 'I am great!', 'Are you a robot?', 'Yes, I am a robot made in Python']


trainer = ChatterBotCorpusTrainer(bot)
trainer.train(conversation)

while True:
    question = input("User: ")
    answer = bot.get_response(question)
    if float(answer.confidence) > 0.5:
        print('Chat_Bot_Name: ', answer)
    else:
        print('Chat_Bot_Name: Sorry, I cannot answer this question yet')
