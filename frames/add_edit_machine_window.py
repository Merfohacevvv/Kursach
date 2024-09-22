import customtkinter as ctk
from helpers import write_csv, read_csv

class AddEditMachineWindow(ctk.CTk):
    def __init__(self, previous_window=None, edit=False, machine_data=None):
        super().__init__()
        self.title("Добавление/Редактирование станка")
        self.geometry("400x400")
        self.previous_window = previous_window  # Предыдущее окно (окно администратора)
        self.edit = edit
        self.machine_data = machine_data

        # Поля для ввода данных
        self.machine_types = ctk.CTkLabel(self, text="Вид")
        self.machine_types.pack(pady=10)
        self.machine_entry_types = ctk.CTkEntry(self)
        self.machine_entry_types.pack(pady=10)

        self.machine_type_label = ctk.CTkLabel(self, text="Тип станка")
        self.machine_type_label.pack(pady=10)
        self.machine_type_entry = ctk.CTkEntry(self)
        self.machine_type_entry.pack(pady=10)

        self.country_label = ctk.CTkLabel(self, text="Страна-производитель")
        self.country_label.pack(pady=10)
        self.country_entry = ctk.CTkEntry(self)
        self.country_entry.pack(pady=10)

        self.year_label = ctk.CTkLabel(self, text="Год выпуска")
        self.year_label.pack(pady=10)
        self.year_entry = ctk.CTkEntry(self)
        self.year_entry.pack(pady=10)

        self.brand_label = ctk.CTkLabel(self, text="Марка")
        self.brand_label.pack(pady=10)
        self.brand_entry = ctk.CTkEntry(self)
        self.brand_entry.pack(pady=10)

        if self.edit and self.machine_data:
            self.populate_data(self.machine_data)

        self.save_button = ctk.CTkButton(self, text="Сохранить", command=self.save_machine)
        self.save_button.pack(pady=20)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        # Скрываем предыдущее окно администратора
        if self.previous_window:
            self.previous_window.withdraw()

    def populate_data(self, machine_data):
        if len(machine_data) > 1:
            self.machine_entry_types.insert(0, machine_data[1])  # Вид станка
        if len(machine_data) > 2:
            self.machine_type_entry.insert(0, machine_data[2])  # Тип станка
        if len(machine_data) > 3:
            self.country_entry.insert(0, machine_data[3])  # Страна-производитель
        if len(machine_data) > 4:
            self.year_entry.insert(0, machine_data[4])  # Год выпуска
        if len(machine_data) > 5:
            self.brand_entry.insert(0, machine_data[5])  # Марка

    def save_machine(self):
        machine_data = [
            self.machine_entry_types.get(),
            self.machine_type_entry.get(),
            self.country_entry.get(),
            self.year_entry.get(),
            self.brand_entry.get()
        ]

        machines = read_csv('Machines.csv')

        if self.edit and self.machine_data:
            # Обновление данных машины, если редактируем существующую запись
            for idx, machine in enumerate(machines):
                if machine[0] == self.machine_data[0]:  # Проверяем ID машины
                    machines[idx] = [self.machine_data[0]] + machine_data
                    break
        else:
            # Генерация нового ID для новой машины
            new_id = str(len(machines) + 1)
            machines.append([new_id] + machine_data)

        write_csv('Machines.csv', machines)

        # После сохранения данных возвращаемся в меню администратора
        if self.previous_window:
            self.previous_window.deiconify()  # Показать окно администратора
        self.withdraw()  # Скрыть текущее окно

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать предыдущее окно администратора
        self.withdraw()  # Скрыть текущее окно
