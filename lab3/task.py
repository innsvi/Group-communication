import tkinter as tk
from tkinter import filedialog, messagebox

# Визначення алфавіту та зіставлення символів із номерами
alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
alphabet_numbers = {char: i for i, char in enumerate(alphabet)}

def create_empty_files():
    """Створює три порожніх файлу Svichkar1.txt, Svichkar2.txt, Svichkar3.txt"""
    filenames = ['Svichkar1.txt', 'Svichkar2.txt', 'Svichkar3.txt']
    for filename in filenames:
        open(filename, 'w').close()
    messagebox.showinfo("Success", "Порожні файли були створені.")

def encrypt_decrypt_file(is_encrypt):
    """Шифрує або дешифрує файл в залежності від параметра is_encrypt"""
    file1_path = filedialog.askopenfilename(title="Виберіть Svichkar1.txt", filetypes=[("Text files", "*.txt")])
    file2_path = filedialog.askopenfilename(title="Виберіть Svichkar2.txt", filetypes=[("Text files", "*.txt")])
    file3_path = filedialog.asksaveasfilename(title="Зберегти результат", defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file1_path and file2_path and file3_path:
        text = open(file1_path, 'r', encoding='utf-8').read()
        password = open(file2_path, 'r', encoding='utf-8').read().strip()
        if len(password) < 10:
            messagebox.showwarning("Помилка", "Пароль має бути не менше 10 символів!")
            return
        
        processed_text = []
        for i, char in enumerate(text):
            if char in alphabet_numbers:
                text_index = alphabet_numbers[char]
                password_char = password[i % len(password)]
                password_index = alphabet_numbers[password_char]
                new_index = (text_index + password_index * (1 if is_encrypt else -1)) % len(alphabet)
                processed_text.append(alphabet[new_index])
            else:
                processed_text.append(char)
        
        with open(file3_path, 'w', encoding='utf-8') as file:
            file.write(''.join(processed_text))
        messagebox.showinfo("Success", "Файл успішно зашифровано." if is_encrypt else "Файл успішно дешифровано.")

root = tk.Tk()
root.title("Лабораторна робота 3")

btn_create_files = tk.Button(root, text="Створити порожні файли", command=create_empty_files)
btn_encrypt = tk.Button(root, text="Зашифрувати файл", command=lambda: encrypt_decrypt_file(True))
btn_decrypt = tk.Button(root, text="Дешифрувати файл", command=lambda: encrypt_decrypt_file(False))

btn_create_files.pack(pady=10)
btn_encrypt.pack(pady=10)
btn_decrypt.pack(pady=10)

root.mainloop()
