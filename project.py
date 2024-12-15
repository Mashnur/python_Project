import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.questions = [
            ("What is the capital of France?", "Paris"),
            ("What is 5 + 3?", "8"),
            ("What is the color of the sky?", "Blue"),
            ("What is 2 * 6?", "12"),
            ("Which planet is known as the Red Planet?", "Mars"),
            ("What is the largest mammal?", "Blue Whale"),
            ("What is the square root of 64?", "8"),
            ("Who wrote 'Hamlet'?", "Shakespeare"),
            ("What is the freezing point of water in Celsius?", "0"),
            ("What is the currency of Japan?", "Yen"),
        ]
        self.current_question = 0
        self.score = 0

        # Create UI elements
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)

        # Load the first question
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question, _ = self.questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {question}")
            self.answer_entry.delete(0, tk.END)
        else:
            self.display_result()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.questions[self.current_question][1]

        if user_answer.lower() == correct_answer.lower():
            self.score += 5
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.score -= 1
            self.result_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red")

        self.current_question += 1
        self.root.after(1000, self.load_question)  # Load the next question after 1 second

    def display_result(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(self.questions) * 5}")
        self.root.quit()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
