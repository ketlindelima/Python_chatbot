# Python_chatbot

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

If this error occur: `subprocess-exited-with-error`, try the command `pip install pip==21.3.1`. Your venv pip version has benn downgraded.

Ater that, install the module named pytz: `pip install pytz` and if this error appear -> *AttributeError: module 'time' has no attribute 'clock'*, open the **compat.py** code page and searching for `time_func = time.clock`, replace this command for `time_func = time.perf_counter`

## Make your data base learning
Now, you are able to try your chatbot with the **main.py** code. All the times you running this code, you are creating a data base file and trainning your bot! You will see the conversation in the terminal like this:

![alt text][image]

[image]: https://user-images.githubusercontent.com/74323079/197012173-bb917e7f-43ff-41b5-9378-c625273652a5.png "Prompt Image"

To improve your bot, you can import a data base with some examples that will help you. In this example, I am creating a Bot that need to understand Portuguese, but a lot of another languages could be find [here](https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/portuguese)






