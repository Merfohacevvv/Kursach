import customtkinter as ctk
from frames.admin_window import AdminWindow
from frames.technician_window import TechnicianWindow
from frames.client_window import ClientWindow
from helpers import read_csv

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Авторизация")
        self.geometry("400x300")

        self.login_label = ctk.CTkLabel(self, text="Логин")
        self.login_label.pack(pady=10)
        self.login_entry = ctk.CTkEntry(self)
        self.login_entry.pack(pady=10)

        self.password_label = ctk.CTkLabel(self, text="Пароль")
        self.password_label.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Войти", command=self.authenticate)
        self.login_button.pack(pady=10)

    def authenticate(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        accounts = read_csv('Accounts.csv')

        for account in accounts:
            if account[2] == login and account[3] == password:
                if account[4] == 'Admin':
                    self.open_admin_window()
                elif account[4] == 'Technician':
                    self.open_technician_window()
                elif account[4] == 'Client':
                    self.open_client_window()
                self.destroy()
                return
        
        error_label = ctk.CTkLabel(self, text="Неверный логин или пароль", text_color="red")
        error_label.pack(pady=10)

    def open_admin_window(self):
        AdminWindow(previous_window=self).mainloop()

    def open_technician_window(self):
        TechnicianWindow(previous_window=self).mainloop()

    def open_client_window(self):
        ClientWindow(previous_window=self).mainloop()
