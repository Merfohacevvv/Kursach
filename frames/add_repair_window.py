import customtkinter as ctk
from helpers import write_csv, read_csv

class AddRepairWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Добавить факт ремонта")
        self.geometry("400x400")
        self.previous_window = previous_window  # Предыдущее окно (окно техника)

        # Поля для ввода данных
        self.machine_label = ctk.CTkLabel(self, text="ID станка")
        self.machine_label.pack(pady=10)
        self.machine_entry = ctk.CTkEntry(self)
        self.machine_entry.pack(pady=10)

        self.duration_label = ctk.CTkLabel(self, text="Продолжительность (в днях)")
        self.duration_label.pack(pady=10)
        self.duration_entry = ctk.CTkEntry(self)
        self.duration_entry.pack(pady=10)

        self.cost_label = ctk.CTkLabel(self, text="Стоимость ремонта")
        self.cost_label.pack(pady=10)
        self.cost_entry = ctk.CTkEntry(self)
        self.cost_entry.pack(pady=10)

        self.save_button = ctk.CTkButton(self, text="Добавить ремонт", command=self.save_repair)
        self.save_button.pack(pady=20)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()  # Скрываем предыдущее окно техника

    def save_repair(self):
        repair_data = [
            self.machine_entry.get(),
            self.duration_entry.get(),
            self.cost_entry.get()
        ]
        
        repairs = read_csv('Report.csv')
        repairs.append(repair_data)
        write_csv('Report.csv', repairs)

        # После добавления ремонта вернемся в меню техника
        self.previous_window.deiconify()  # Показать окно техника
        self.withdraw()  # Скрываем текущее окно

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать предыдущее окно техника
        self.withdraw()  # Скрываем текущее окно
