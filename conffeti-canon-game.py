import tkinter as tk
import random

class ConfettiCannonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Confetti Cannon")
        
        
        self.root.configure(bg='lightgreen')
        
        self.objects = ["🍕", "🎉", "🎈", "🍔", "🍭", "🍦", "🎃", "🚀", "🎁", "🦄", "🌈", "👑"]
        
        self.title_label = tk.Label(root, text="Virtual Confetti Cannon!", font=("Helvetica", 16), bg='skyblue')
        self.title_label.pack(pady=20)
        
        self.fire_button = tk.Button(root, text="Fire Cannon", command=self.fire_cannon, font=("Helvetica", 14))
        self.fire_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg='yellow')
        self.result_label.pack(pady=20)
        
    def fire_cannon(self):
        confetti = ''.join(random.choices(self.objects, k=10))
        self.result_label.config(text=confetti)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConfettiCannonApp(root)
    root.mainloop()
