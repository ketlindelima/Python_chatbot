from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Chat_Bot_Name')

conversation = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você é um robô?', 'Sim, um robô feito em Python']


trainer = ListTrainer(bot)
trainer.train(conversation)

while True:
    pergunta = input("User: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Chat_Bot_Name: ', resposta)
    else:
        print('Chat_Bot_Name: Ainda não sei responder esta pergunta')
