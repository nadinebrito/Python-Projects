import tkinter as tk  # tkinter: ferramenta responsável pelas interfaces gráficas para programas em Python.
from tkinter import messagebox
from cryptography.fernet import Fernet # Fernet: módulo do pacote de criptografia.

def generate_key(): # Função que gera a chave de criptografia.
    return Fernet.generate_key()

def encrypt_password(key, password): # Função que criptografa a senha passada pelo usuário.
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password): # Função que descriptografa a senha passada pelo usuário.
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

passwords = {} # Dicionário responsável por armazenar as senhas.

def add_password(): # Função responsável por armazenar a senha criptografada no dicionário.
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'username': username, 'password': encrypted_password}
        messagebox.showinfo("Successo", "Senha adicionada com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor preencha todos os campos.")

def get_password(): # Função responsável por recuperar a senha do serviço desejado do dicionário.
    service = service_entry.get()
    if service in passwords:
        encrypted_password = passwords[service]['password']
        decrypted_password = decrypt_password(key, encrypted_password)
        messagebox.showinfo("Senha", f"Usuário: {passwords[service]['username']}\nPassword: {decrypted_password}")
    else:
        messagebox.showwarning("Erro", "Senha não encontrada.")

key = generate_key()

instructions = '''Para adicionar senha preencha todos os campos e clique em “Add Senha”
Para visualizar a senha, digite o nome da conta e pressione "Obter senha"'''
signature = "Adaptado por Nadine Capistrano"

window = tk.Tk()
window.title("Gerenciador de Senhas")
window.configure(bg="purple")

window.resizable(False, False)


center_frame = tk.Frame(window, bg="#d3d3d3")
center_frame.grid(row=0, column=0, padx=10, pady=10)

instruction_label = tk.Label(center_frame, text=instructions, bg="#d3d3d3")
instruction_label.grid(row=0, column=1, padx=10, pady=5)

service_label = tk.Label(center_frame, text="Conta:", bg="#d3d3d3")
service_label.grid(row=1, column=0, padx=10, pady=5)
service_entry = tk.Entry(center_frame)
service_entry.grid(row=1, column=1, padx=10, pady=5)

username_label = tk.Label(center_frame, text="Nome de usuário:", bg="#d3d3d3")
username_label.grid(row=2, column=0, padx=10, pady=5)
username_entry = tk.Entry(center_frame)
username_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(center_frame, text="Senha:", bg="#d3d3d3")
password_label.grid(row=3, column=0, padx=10, pady=5)
password_entry = tk.Entry(center_frame, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)


add_button = tk.Button(center_frame, text="Add Senha", command=add_password, height=1, width=10)
add_button.grid(row=5, column=4, padx=10, pady=5)

get_button = tk.Button(center_frame, text="Obter Senha", command=get_password, height=1, width=10)
get_button.grid(row=6, column=4, padx=10, pady=5)

signature_label = tk.Label(center_frame, text=signature, bg="#d3d3d3")
signature_label.grid(row=7, column=1, padx=5, pady=5)


window.mainloop()