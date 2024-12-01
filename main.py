import customtkinter as ctk
from question import Question
import requests
import time
import html
import json


GRID_PAD = 20

categories = [18, 9, 15, 31, 32]

categories = {
    "Video Games": 15,
    "Computers": 18,
    "General Knowledge": 9,
    "Anime & Manga": 31,
    "Cartoons & Animations": 32,
}

#TODO: Refactor this shit into functions and improve variable names
questions = {}

for category, value in categories.items():
    cat_request = requests.get(f"https://opentdb.com/api.php?amount=5&category={value}")
    cat_request.raise_for_status()
    print(f"Attempting request {category}, status: {cat_request}")
    cat_results = cat_request.json()["results"]
    questions[category] = []
    for result in cat_results:
        questions[category].append(
            {
                "question": html.unescape(result["question"]),
                "answer": html.unescape(result["correct_answer"]),
            }
        )
    time.sleep(5)

print(json.dumps(questions, indent=4))


wn = ctk.CTk()
wn.resizable(False, False)
wn.geometry("1280x720")

buttons = []
i = 0
for (category, question_list) in questions.items():
    question_row = []
    j = 0
    for item in question_list:
        question = item["question"]
        answer = item["answer"]
        question_row.append(
            Question(wn, answer=answer, question=question, row=i, column=j)
        )
        j+=1
    wn.grid_columnconfigure(i, pad=GRID_PAD)
    wn.grid_rowconfigure(i, pad=GRID_PAD)
    buttons.append(question_row)
    i += 1


wn.mainloop()
