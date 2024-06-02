import tkinter as tk
from tkinter import filedialog, messagebox

def create_file():
    # Функція для створення нового файлу з заданим іменем
    filename = filedialog.asksaveasfilename(defaultextension=".txt", title="Створити файл", filetypes=[("Text files", "*.txt")])
    if filename:
        open(filename, 'w').close()
        messagebox.showinfo("Success", "Файл успішно створено.")
    else:
        messagebox.showerror("Помилка", "Створення файлу скасовано.")

def save_to_file(entries, title, message):
    # Запитуємо ім'я файлу для збереження даних
    file_path = filedialog.askopenfilename(title="Виберіть файл для збереження", defaultextension=".txt", filetypes=[("Text files", "*.txt")], initialdir=".")
    if file_path:
        data = [entry.get() for entry in entries]
        with open(file_path, 'a', encoding='utf-8') as file:  # Відкриваємо файл в режимі додавання (append)
            for item in data:
                file.write(item + '\n')
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Помилка", "Файл не було обрано.")

def load_from_file(entries, title, message):
    file_path = filedialog.askopenfilename(title=title, filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for i, entry in enumerate(entries):
            entry.delete(0, tk.END)
            if i < len(data):
                entry.insert(0, data[i].strip())
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Помилка", "Файл не було обрано.")

root = tk.Tk()
root.title("Програма для передачі запитань колегам з групи")

labels_questions = ["Питання 1", "Питання 2", "Питання 3", "Питання 4", "Питання 5"]
labels_answers = ["Відповідь 1", "Відповідь 2", "Відповідь 3", "Відповідь 4", "Відповідь 5"]
entries_questions = []
entries_answers = []

for i in range(5):
    tk.Label(root, text=labels_questions[i]).grid(row=i*2, column=0)
    entry_question = tk.Entry(root, width=50)
    entry_question.grid(row=i*2, column=1)
    entries_questions.append(entry_question)
    
    tk.Label(root, text=labels_answers[i]).grid(row=i*2+1, column=0)
    entry_answer = tk.Entry(root, width=50)
    entry_answer.grid(row=i*2+1, column=1)
    entries_answers.append(entry_answer)

btn_create_file = tk.Button(root, text="Створити новий файл", command=create_file)
btn_create_file.grid(row=10, column=0, pady=10)

btn_save_questions = tk.Button(root, text="Зберегти питання", command=lambda: save_to_file(entries_questions, "Зберегти питання", "Запитання успішно збережені"))
btn_save_questions.grid(row=10, column=1, pady=10)

btn_load_questions = tk.Button(root, text="Завантажити питання", command=lambda: load_from_file(entries_questions, "Відкрити файл з питаннями", "Запитання успішно завантажені"))
btn_load_questions.grid(row=11, column=0, pady=10)

btn_save_answers = tk.Button(root, text="Зберегти відповіді", command=lambda: save_to_file(entries_answers, "Зберегти відповіді", "Відповіді успішно збережені"))
btn_save_answers.grid(row=11, column=1, pady=10)

btn_load_answers = tk.Button(root, text="Завантажити відповіді", command=lambda: load_from_file(entries_answers, "Відкрити файл з відповідями", "Відповіді успішно завантажені"))
btn_load_answers.grid(row=12, column=0, pady=10)

root.mainloop()
