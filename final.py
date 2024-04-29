from vosk import Model, KaldiRecognizer
from vosk import SetLogLevel

SetLogLevel(-1)

import pyttsx3 as ttx
import pyaudio
from modules import *
from getcommands import Commands

model = Model(r"") #replace with a vosk model
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()

listening_state = False

def get_command():
    listening_state = True
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    while listening_state:
        stream.start_stream()
        try:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                response = result[14:-3]
                listening_state = False
                stream.close()
                return response
        except OSError:
            print('hi')
            pass

def Speak(command):
    engine = ttx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 155)
    engine.say(command)
    engine.runAndWait()

print('👋 Hi there user! My name is Bob, I\'m your helpful chatbot.')
print('💬 I support voice commands and text commands. To best serve you, answer this prompt:')

chosentype = input('-> Voice-based assistant or text-based assistant? (Voice: voice, v, talk | Text: text, type, t): ')
typelist = {
    'voice': ['voice', 'v', 'talk'],
    'text': ['text', 'type', 't']
}

if chosentype in typelist['voice']:
    chosentype = 'voice'
elif chosentype in typelist['text']:
    chosentype = 'text'
else:
    print('Please select a valid option with the input.')
    exit()

print('🙂 Great choice! Now, you\'re free to ask me any questions.')
print('🤔 Need help? Say "help" and I\'ll send a list of features.')

while True:
    answered = False
    if chosentype == 'voice':
        print('Speak...')
        command = get_command()
    else:
        command = input('Input your query: ')

    text = str(command).lower()
    for c, a in Commands.items():
        if text.startswith(str(c)):
            Commands[c].execute(command)
            answered = True
    if text == '':
        print('I didn\'t quite understand. Try again!')
        pass
    elif "stop" in text:
        print('👋 Goodbye!')
        Speak('Goodbye')
        exit()
    elif text == 'help':
        print('🤔 HELP? No worries, I\'m here to help!')
        print('-')
        print('How do I ask a question? No worries, you can ask a question by typing your query in the "Insert your query" prompt.')
        print('How do I access ChatGPT? Type chat (your query) in the query prompt, you will be connected to the AI chatbot.')
        print('How do I stop the program? Sorry to see you go, just type "stop" in the prompt.')
        print('-')
        print('🤖 Supported Commands:')
        for command_name, module in Commands.items():
            metadata = module.metadata
            args = metadata.get('args', '')  # Get the arguments from metadata, if available
            description = metadata.get('description', '')  # Get the description from metadata, if available
            print(f'-> {command_name}{args}: {description}')
    else:
        if not answered:
            print(f'You said: {command.capitalize()}')
            Speak(command) 