import customtkinter as ctk
import time

WIDTH = 200
HEIGHT = 100


class Question:
    def __init__(self, root, **kw):
        self.root = root
        self.question = kw.get("question")
        self.answer = kw.get("answer")
        self.row = kw.get("row")
        self.column = kw.get("column")
        self.button = ctk.CTkButton(self.root, command=self.show_question)
        self.button.grid(row=self.row, column=self.column)
        self.button.configure(text=(self.row + 1) * 100, width=WIDTH, height=HEIGHT)

    def show_question(self):
        self.button.destroy()
        self.question = ctk.CTkLabel(
            master=self.root,
            text=self.question,
            wraplength=200,
            font=("Arial", 14),
            corner_radius=10,
            fg_color="blue",
            width=WIDTH,
            height=HEIGHT,
        )
        self.question.grid(row=self.row, column=self.column)
        self.question.bind("<Button-1>", self.show_answer)

    def show_answer(self, event):
        time.sleep(0.016)
        self.question.configure(text=self.answer)
