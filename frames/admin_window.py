import customtkinter as ctk
from frames.add_edit_machine_window import AddEditMachineWindow
from frames.view_machines_window import ViewMachinesWindow
from frames.delete_machine_window import DeleteMachineWindow
from frames.edit_machine_window import EditMachineWindow

class AdminWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Личный кабинет администратора")
        self.geometry("600x400")
        self.previous_window = previous_window

        self.view_machines_button = ctk.CTkButton(self, text="Просмотр станков", command=self.view_machines)
        self.view_machines_button.pack(pady=10)

        self.add_machine_button = ctk.CTkButton(self, text="Добавить станок", command=self.add_machine)
        self.add_machine_button.pack(pady=10)

        self.edit_machine_button = ctk.CTkButton(self, text="Редактировать станок", command=self.edit_machine)
        self.edit_machine_button.pack(pady=10)

        self.delete_machine_button = ctk.CTkButton(self, text="Удалить станок", command=self.delete_machine)
        self.delete_machine_button.pack(pady=10)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()

    def view_machines(self):
        ViewMachinesWindow(previous_window=self).mainloop()

    def add_machine(self):
        AddEditMachineWindow(previous_window=self).mainloop()

    def edit_machine(self):
        EditMachineWindow(previous_window=self).mainloop()  # Открываем окно для ввода ID станка

    def delete_machine(self):
        DeleteMachineWindow(previous_window=self).mainloop()

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать предыдущее окно
        self.withdraw()  # Скрываем текущее окно
