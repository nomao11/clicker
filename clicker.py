import tkinter as tk

class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Кликер Игра")
        self.score = 0
        self.score_label = tk.Label(root, text="Счет: 0", font=("Helvetica", 24))
        self.score_label.pack(pady=20)
        self.click_button = tk.Button(root, text="Кликни меня!", command=self.increment_score, font=("Helvetica", 24))
        self.click_button.pack(pady=20)
        self.reset_button = tk.Button(root, text="Сбросить счет", command=self.reset_score, font=("Helvetica", 24))
        self.reset_button.pack(pady=20)

    def increment_score(self):
        self.score += 1
        self.score_label.config(text=f"Счет: {self.score}")

    def reset_score(self):
        self.score = 0
        self.score_label.config(text="Счет: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()