import tkinter as tk
from tkinter import filedialog, messagebox

def count_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    char_count = {}
    total_letters = 0
    for char in text:
        if char.isalpha():  # Consider only letters
            total_letters += 1
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count, total_letters

def save_results(char_count, total_letters):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            for char, count in char_count.items():
                file.write(f"'{char}': {count}\n")
            file.write(f"\nЗагальна сума букв: {total_letters}\n")
        messagebox.showinfo("Success", "Результати успішно збережені")

def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        char_count, total_letters = count_characters(file_path)
        save_results(char_count, total_letters)

root = tk.Tk()
root.title("Програма для підрахунку кількості входжень символів")

btn_process_file = tk.Button(root, text="Вибрати файл та обробити", command=process_file)
btn_process_file.pack(pady=20)

root.mainloop()
