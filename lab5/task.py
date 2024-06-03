import tkinter as tk
from tkinter import filedialog, messagebox

def count_characters(file_path):
    # Відкриття файлу та читання тексту з нього
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    char_count = {}  # Словник для зберігання кількості кожного символу
    total_letters = 0  # Лічильник загальної кількості букв
    for char in text:
        if char.isalpha():  # Враховувати тільки букви
            total_letters += 1
        if char in char_count:
            char_count[char] += 1  # Збільшити лічильник для вже наявного символу
        else:
            char_count[char] = 1  # Додати новий символ у словник
    
    return char_count, total_letters  # Повернення результатів

def save_results(char_count, total_letters):
    # Вибір файлу для збереження результатів
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        # Запис результатів у файл
        with open(file_path, 'w', encoding='utf-8') as file:
            for char, count in char_count.items():
                file.write(f"'{char}': {count}\n")  # Форматування та запис кожного символу та його кількості
            file.write(f"\nЗагальна сума букв: {total_letters}\n")  # Додавання загальної кількості букв на кінець файлу
        messagebox.showinfo("Success", "Результати успішно збережені")  # Повідомлення про успішне збереження

def process_file():
    # Вибір файлу для обробки
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        char_count, total_letters = count_characters(file_path)  # Отримання статистики символів і букв
        save_results(char_count, total_letters)  # Збереження результатів

root = tk.Tk()
root.title("Програма для підрахунку кількості входжень символів")

btn_process_file = tk.Button(root, text="Вибрати файл та обробити", command=process_file)
btn_process_file.pack(pady=20)

root.mainloop()  # Головний цикл GUI
