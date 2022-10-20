# Python_chatbot

## Install Virtualenv 
Install with ith the command `pip install virtualenv`. After that, give a name `virtualenv venv` for example.

## Install the Spacy Library
Inntall [Spacy library](https://spacy.io/usage) with the command below

```
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
## Install the Chatterbot Python Library 
Install with the command `pip install chatterbot` -> [Chatterbot Documentation](https://pypi.org/project/ChatterBot/)

If this error occur: `subprocess-exited-with-error`, try the command `pip install pip==21.3.1`. Your venv pip version has benn downgraded.
Ater that, instal module pytz `pip install pytz` and if this error appear -> *AttributeError: module 'time' has no attribute 'clock'*, open the **compat.py** code page and searching for `time_func = time.clock`, replace this command for `time_func = time.perf_counter`

## Make you data base learning
Now, you are ablle to try your chatbot with the **main.py** code. All times you running this code you are creating a data base file trainning your bot! You will see the conversation in the terminal like this:

![alt text][image]

[image]: https://user-images.githubusercontent.com/74323079/197012173-bb917e7f-43ff-41b5-9378-c625273652a5.png "Prompt Image"







