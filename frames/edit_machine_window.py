import customtkinter as ctk
from helpers import read_csv
from frames.add_edit_machine_window import AddEditMachineWindow

class EditMachineWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Редактировать станок")
        self.geometry("400x300")
        self.previous_window = previous_window  # Окно администратора

        # Поле для ввода ID станка
        self.machine_id_label = ctk.CTkLabel(self, text="Введите ID станка для редактирования")
        self.machine_id_label.pack(pady=10)
        self.machine_id_entry = ctk.CTkEntry(self)
        self.machine_id_entry.pack(pady=10)

        # Кнопка "Редактировать"
        self.edit_button = ctk.CTkButton(self, text="Редактировать", command=self.check_and_edit_machine)
        self.edit_button.pack(pady=20)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()

    def check_and_edit_machine(self):
        machine_id = self.machine_id_entry.get()

        machines = read_csv('Machines.csv')

        # Ищем станок с таким ID
        machine_to_edit = None
        for machine in machines:
            if machine[0] == machine_id:
                machine_to_edit = machine
                break

        if machine_to_edit:
            # Если станок найден, открываем окно редактирования
            AddEditMachineWindow(previous_window=self.previous_window, edit=True, machine_data=machine_to_edit).mainloop()
            self.withdraw()  # Скрыть текущее окно
        else:
            # Если станок не найден, выводим сообщение об ошибке
            ctk.CTkLabel(self, text="Станок с таким ID не найден", text_color="red").pack(pady=10)

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать окно администратора
        self.withdraw()  # Скрыть текущее окно
