# Python_chatbot

Hi, there! 
In this short tutorial, I will show you how to implement the Python *ChatterBot* library to create a ChatBot that can learn with interactions, all the error messages that I found, and how did I solve them.

This ChatBot program is capable to:
- Understand messages send
- Give answer according to the messages
- Learn with data base
- Be a Live chat message

## Install Virtualenv 
Install with the command `pip install virtualenv`. After that, give a name `virtualenv venv` for example.

## Install the Spacy Library
Install [Spacy library](https://spacy.io/usage) with the commands below

```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
## Install the Chatterbot Python Library 
Install with the command `pip install chatterbot` -> [Chatterbot Documentation](https://pypi.org/project/ChatterBot/)

If this error occur: `subprocess-exited-with-error`, try the command `python -m pip install pip==21.3.1`. Your venv pip version has benn downgraded. Now, try the command again `pip install chatterbot`. This process takes some minutes and can produce warnings.

After that, install the module named pytz: `pip install pytz` and if this error appear -> *AttributeError: module 'time' has no attribute 'clock'*, open the **compat.py** code page and searching for `time_func = time.clock`, replace this command for `time_func = time.perf_counter`

Until now, the code to make a simple conversation seems like this:

```
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Chat_Bot_Name')

conversation = ['Hi', 'Hello', 'How are you?', 'I am great!', 'Are you a robot?', 'Yes, I am a robot made in Python']


trainer = ListTrainer(bot)
trainer.train(conversation)

while True:
    question = input("User: ")
    answer = bot.get_response(question)
    if float(answer.confidence) > 0.5:
        print('Chat_Bot_Name: ', answer)
    else:
        print('Chat_Bot_Name: Sorry, I cannot answer this question yet')
```

## Make your data base learning
Now, you are able to try your chatbot with the **main.py** code. All the times you running this code, you are creating a data base file and trainning your bot! You will see the conversation in the terminal like this:

![alt text][image]

[image]: https://user-images.githubusercontent.com/74323079/197056368-a37cc994-5f6a-40b2-b9ba-1b1a9e7821df.png "Prompt Image"

This program is able to understand many languages. In this case, I will use this ChatBot to recive and send messages in Portuguese.

To improve your bot, you can import a data base with some examples that will help you. In this example, I am creating a Bot that need to understand Portuguese, but a lot of another languages could be find [here](https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data)


## Making a rich conversation
Now, it is time to improve the conversation, to make this, we just need to substitute the variable *conversation* to the [greatings data base](https://github.com/gunthercox/chatterbot-corpus/blob/master/chatterbot_corpus/data/english/greetings.yml)


## I hope that I could help you, enjoy your new friend bot! 😉






