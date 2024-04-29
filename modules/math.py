def execute(text):
    toeval = text.split(' ', 1)[1]
    print(eval(toeval))

metadata = {
    "name": "math",
    "description": "Evaluates your problem and gives you the answer.",
    "args": " (problem)"
}

__all__ = ['execute', 'metadata']