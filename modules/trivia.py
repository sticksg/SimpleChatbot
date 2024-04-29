def execute():
    import requests
    import json
    import random

    response = requests.get("https://opentdb.com/api.php?amount=3")
    data = json.loads(response.text)

    questions = data['results']

    c = 0
    for q in questions:
        print(q['question'])
        print('-> Options:')
        
        answers = q['incorrect_answers'] + [q['correct_answer']]
        random.shuffle(answers)

        for i, answer in enumerate(answers):
            print(f'--> {i + 1}. {answer}')
        selected = int(input('What is your answer? '))

        if selected == answers.index(q['correct_answer']) + 1:
            print("Correct!")
            c += 1
        else:
            print("Answer incorrect. :(")
    print('-----')
    print(f"🎉 Congrats, you got {c} of {len(questions)} questions correct!")

metadata = {
    "name": "trivia",
    "description": "Play a simple trivia game with random questions!",
    "args": ""
}

__all__ = ['execute', 'metadata']