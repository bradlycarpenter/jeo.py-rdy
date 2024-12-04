# import customtkinter as ctk
# from question import Question
# import requests
# import time
# import html


# GRID_PAD = 20

# categories = [18, 9, 15, 31, 32]

# categories = {
#     "Video Games": 15,
#     "Computers": 18,
#     "General Knowledge": 9,
#     "Anime & Manga": 31,
#     "Cartoons & Animations": 32,
# }

# # TODO: Refactor this shit into functions and improve variable names
# questions = {}

# for category, value in categories.items():
#     cat_request = requests.get(f"https://opentdb.com/api.php?amount=5&category={value}")
#     cat_request.raise_for_status()
#     print(f"Attempting request {category}, status: {cat_request}")
#     cat_results = cat_request.json()["results"]
#     questions[category] = []
#     for result in cat_results:
#         questions[category].append(
#             {
#                 "question": html.unescape(result["question"]),
#                 "answer": html.unescape(result["correct_answer"]),
#             }
#         )
#     time.sleep(5)


# wn = ctk.CTk()
# wn.resizable(False, False)
# wn.geometry("1280x720")

# buttons = []
# for column, (category, question_list) in enumerate(questions.items()):
#     question_row = []

#     for row, item in enumerate(question_list):
#         question = item["question"]
#         answer = item["answer"]
#         question_row.append(
#             Question(wn, answer=answer, question=question, row=row, column=column)
#         )

#     wn.grid_columnconfigure(column, pad=GRID_PAD)
#     wn.grid_rowconfigure(column, pad=GRID_PAD)
#     buttons.append(question_row)


# wn.mainloop()

# import customtkinter as ctk
# import time

# WIDTH = 200
# HEIGHT = 100


# class Question:
#     def __init__(self, root, **kw):
#         self.root = root
#         self.question = kw.get("question")
#         self.answer = kw.get("answer")
#         self.row = kw.get("row")
#         self.column = kw.get("column")
#         self.button = ctk.CTkButton(self.root, command=self.show_question)
#         self.button.grid(row=self.row, column=self.column)
#         self.button.configure(text=(self.row + 1) * 100, width=WIDTH, height=HEIGHT)

#     def show_question(self):
#         self.button.destroy()
#         self.label = ctk.CTkLabel(
#             master=self.root,
#             text=self.question,
#             wraplength=200,
#             font=("Arial", 14),
#             corner_radius=10,
#             width=WIDTH,
#             height=HEIGHT,
#         )
#         self.label.grid(row=self.row, column=self.column)
#         self.label.bind("<Button-1>", self.show_answer)

#     def show_answer(self, event):
#         time.sleep(0.016)
#         self.label.configure(text=self.answer)
