def execute(text):
    import pywhatkit

    query = text.split(' ', 1)[1]
    pywhatkit.playonyt(query, False, True)

    input('😀 Take your time on Youtube. Press enter when you\'ve returned!')

metadata = {
    "name": "youtube",
    "description": "Plays a video on Youtube.",
    "args": " (search)"
}

__all__ = ['execute', 'metadata']