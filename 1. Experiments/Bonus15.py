
# Lesson 146 -- Bonus 15.

# This line imports the json file that is inside the same folder as this codeblock.

import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choise = int(input("Enter your answer: "))
    question["user_choise"] = user_choise


score = 0
for index, question in enumerate(data):
    if question["user_choise"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = f"{index + 1} {result} - Yur answer: {question['user_choise']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(score, "/", len(data))

