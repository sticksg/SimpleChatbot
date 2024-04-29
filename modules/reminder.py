def execute():
    def Speak(command):
        import pyttsx3 as ttx
        engine = ttx.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 155)
        engine.say(command)
        engine.runAndWait()

    reminder = input('What do you need to be reminded of? ')
    wait = float(input('In how many minutes should I remind you of this? '))

    import time
    time.sleep(wait * 60)
    print('⏰ Here\'s your reminder for ', reminder)
    Speak('Your reminder is done')

metadata = {
    "name": "reminder",
    "description": "Remind you of something.",
    "args": ""
}

__all__ = ['execute', 'metadata']