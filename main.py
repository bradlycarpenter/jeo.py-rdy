import customtkinter as ctk
from question import Question
import requests
import time
import html


GRID_PAD = 20

categories = [18, 9, 15, 31, 32]

questions = []
answers = []

for i in range(5):
    cat_request = requests.get(
        f"https://opentdb.com/api.php?amount=5&category={categories[i]}"
    )
    cat_request.raise_for_status()
    print(f"Attempting request {i+1}, status: {cat_request}")
    cat_results = cat_request.json()["results"]
    cat_questions = [html.unescape(result["question"]) for result in cat_results]
    cat_answers = [html.unescape(result["correct_answer"]) for result in cat_results]
    questions.append(cat_questions)
    answers.append(cat_answers)
    time.sleep(5)


wn = ctk.CTk()
wn.resizable(False, False)
wn.geometry("1280x720")

buttons = []
for i in range(5):
    question_row = []
    for j in range(5):
        question = questions[j][i]
        answer = answers[j][i]
        question_row.append(
            Question(wn, answer=answer, question=question, row=i, column=j)
        )
    wn.grid_columnconfigure(i, pad=GRID_PAD)
    wn.grid_rowconfigure(i, pad=GRID_PAD)
    buttons.append(question_row)


wn.mainloop()
