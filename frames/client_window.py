import customtkinter as ctk
from frames.view_machines_window import ViewMachinesWindow

class ClientWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Личный кабинет клиента")
        self.geometry("600x400")
        self.previous_window = previous_window

        self.view_status_button = ctk.CTkButton(self, text="Статус ремонтных работ", command=self.view_status)
        self.view_status_button.pack(pady=10)

        self.view_history_button = ctk.CTkButton(self, text="История ремонтных работ", command=self.view_history)
        self.view_history_button.pack(pady=10)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()

    def view_status(self):
        ViewMachinesWindow(previous_window=self).mainloop()

    def view_history(self):
        ViewMachinesWindow(previous_window=self).mainloop()

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать предыдущее окно
        self.withdraw()  # Скрываем текущее окно
