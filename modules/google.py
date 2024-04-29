def execute(text):
    import webbrowser

    thing = text.split(' ', 1)[1]
    url = "https://www.google.com/search?q=" + "+".join(thing.split())

    webbrowser.open_new_tab(url)
    input('😀 Take your time on Google. Press enter when you\'ve returned!')

metadata = {
    "name": "google",
    "description": "Searches your query on Google.",
    "args": " (search)"
}

__all__ = ['execute', 'metadata']