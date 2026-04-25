import tkinter as tk
import random

git_hub = "https://github.com/berdinrr/practica_4.5/tree/main"

facts = [
   "Бананы радиоактивны и излучают небольшое количество гамма-излучения.",
   "Человек может обойтись без пищи до 2 месяцев, а без воды — всего несколько дней.",
   "Голубые киты ежедневно потребляют около 4 тонн пищи.",
   "Пчёлы могут распознавать лица людей.",
   "Существует 6 000 видов бананов, а не только один.",
   "Практика 4.5 выполнена"
]

def show_fact():
        random_fact = random.choice(facts)
        fact_label.config(text=random_fact)

window = tk.Tk()
window.title("Случайный факт")
window.geometry("500x250")

tk.Label(window, text="Нажми на кнопку, чтобы получить рандомный факт").pack(pady=10)

fact_button = tk.Button(
        window,
        text="Показать факт",
        command=show_fact
)
fact_button.pack(pady=10)

fact_label = tk.Label(window, text="Здесь появится факт")
fact_label.pack(pady=20)

window.mainloop()