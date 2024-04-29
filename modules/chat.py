def execute(text):
    def Speak(command):
        import pyttsx3 as ttx
        engine = ttx.init()
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 155)
        engine.say(command)
        engine.runAndWait()

    messages = []
    from openai import OpenAI
    client = OpenAI(api_key = '')
    messages = [{"role": "system", "content": "You are a helpful intelligent assistant"}]

    query = text.split(' ', 1)[1]
    if query:
        messages.append({"role": "user", "content": query})
        chat = client.chat.completions.create(
            model = "gpt-3.5-turbo", messages = messages
        )
        reply = chat.choices[0].message.content
        print(reply)
        messages.append({"role": "assistant", "content": reply})
        Speak(reply)
    else:
        print('Hey, sorry, chat couldn\'t get your query. :(')

metadata = {
    "name": "chat",
    "description": "Send your query to ChatGPT.",
    "args": " (query)"
}

__all__ = ['execute', 'metadata']