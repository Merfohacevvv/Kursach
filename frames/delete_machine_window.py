import customtkinter as ctk
from helpers import write_csv, read_csv

class DeleteMachineWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Удалить станок")
        self.geometry("400x300")
        self.previous_window = previous_window  # Окно администратора

        # Поле для ввода ID станка
        self.machine_id_label = ctk.CTkLabel(self, text="Введите ID станка для удаления")
        self.machine_id_label.pack(pady=10)
        self.machine_id_entry = ctk.CTkEntry(self)
        self.machine_id_entry.pack(pady=10)

        # Кнопка "Удалить"
        self.delete_button = ctk.CTkButton(self, text="Удалить", command=self.delete_machine)
        self.delete_button.pack(pady=20)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()

    def delete_machine(self):
        machine_id = self.machine_id_entry.get()

        machines = read_csv('Machines.csv')

        # Проверка, существует ли станок с таким ID
        machine_exists = False
        for machine in machines:
            if machine[0] == machine_id:
                machine_exists = True
                machines.remove(machine)  # Удаляем станок
                break

        if machine_exists:
            write_csv('Machines.csv', machines)
            ctk.CTkLabel(self, text="Станок успешно удалён", text_color="green").pack(pady=10)
        else:
            ctk.CTkLabel(self, text="Станок с таким ID не найден", text_color="red").pack(pady=10)

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать окно администратора
        self.withdraw()  # Скрыть текущее окно
