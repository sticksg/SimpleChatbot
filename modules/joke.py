def execute():
    import pyjokes
    print('😁 Here\'s a great one: ', pyjokes.get_joke())

metadata = {
    "name": "joke",
    "description": "Be told a hilarious joke.",
    "args": ""
}

__all__ = ['execute', 'metadata']