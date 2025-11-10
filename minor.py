import tkinter as tk
from tkinter import messagebox
import random


questions = [
    {
        "question": "What is the output of 3 + 2 * 2 in Python?",
        "options": ["10", "7", "9", "8"],
        "answer": "7"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": ["tuple", "list", "string", "int"],
        "answer": "list"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["input()", "print()", "enter()", "read()"],
        "answer": "input()"
    },
    {
        "question": "What will be the output of len('Python')?",
        "options": ["5", "7", "6", "8"],
        "answer": "6"
    },
    {
        "question": "What does the random module do in Python?",
        "options": ["Math operations", "Generate random numbers", "Sort lists", "None of these"],
        "answer": "Generate random numbers"
    }
]

random.shuffle(questions)  

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Python Quiz Game")
        self.master.geometry("600x400")
        self.master.configure(bg="#E8F0FE")

        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(
            master,
            text="",
            font=("Arial", 16, "bold"),
            wraplength=500,
            bg="#E8F0FE",
            justify="center"
        )
        self.question_label.pack(pady=30)

        self.var = tk.StringVar(value="")

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                master,
                text="",
                variable=self.var,
                value="",
                font=("Arial", 14),
                bg="#E8F0FE",
                anchor="w",
                padx=20,
                indicatoron=0,
                width=30,
                relief="ridge",
                selectcolor="#D6EAF8"
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.submit_btn = tk.Button(
            master,
            text="Submit Answer",
            font=("Arial", 13, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.check_answer
        )
        self.submit_btn.pack(pady=20)

        self.next_btn = tk.Button(
            master,
            text="Next Question",
            font=("Arial", 13, "bold"),
            bg="#2196F3",
            fg="white",
            command=self.next_question,
            state="disabled"
        )
        self.next_btn.pack()

        self.show_question()


    def show_question(self):
        self.var.set("")
        question_data = questions[self.q_index]
        self.question_label.config(text=question_data["question"])

        for i in range(4):
            self.option_buttons[i].config(
                text=question_data["options"][i],
                value=question_data["options"][i]
            )

   
    def check_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Select an option", "Please select an answer!")
            return

        correct = questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Result", "✅ Correct!")
        else:
            messagebox.showerror("Result", f"❌ Wrong!\nCorrect Answer: {correct}")

        self.submit_btn.config(state="disabled")
        self.next_btn.config(state="normal")

    
    def next_question(self):
        self.q_index += 1
        if self.q_index < len(questions):
            self.show_question()
            self.submit_btn.config(state="normal")
            self.next_btn.config(state="disabled")
        else:
            self.show_result()

    
    def show_result(self):
        percentage = (self.score / len(questions)) * 100
        result_msg = (
            f"🎯 Quiz Completed!\n\n"
            f"Your Score: {self.score}/{len(questions)}\n"
            f"Percentage: {percentage:.2f}%\n\n"
        )

        if percentage == 100:
            result_msg += "🏆 Excellent! Perfect score!"
        elif percentage >= 60:
            result_msg += "👏 Good job! You passed!"
        else:
            result_msg += "📖 Keep practicing!"

        messagebox.showinfo("Quiz Result", result_msg)
        self.master.destroy()



root = tk.Tk()
app = QuizApp(root)
root.mainloop()
