def execute(text):
    import webbrowser

    song = text.split(' ', 1)[1]
    url = "https://open.spotify.com/search/" + "%20".join(song.split())

    webbrowser.open_new_tab(url)
    input('😀 Take your time on Spotify. Press enter when you\'ve returned!')

metadata = {
    "name": "spotify",
    "description": "Opens spotify with your desired search.",
    "args": " (song)"
}

__all__ = ['execute', 'metadata']