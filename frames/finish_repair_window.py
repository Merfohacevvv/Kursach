import customtkinter as ctk
from helpers import write_csv, read_csv

class FinishRepairWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Завершение ремонта")
        self.geometry("400x400")
        self.previous_window = previous_window

        # Поля для завершения ремонта
        self.repair_id_label = ctk.CTkLabel(self, text="ID ремонта")
        self.repair_id_label.pack(pady=10)
        self.repair_id_entry = ctk.CTkEntry(self)
        self.repair_id_entry.pack(pady=10)

        self.finish_button = ctk.CTkButton(self, text="Завершить ремонт", command=self.finish_repair)
        self.finish_button.pack(pady=20)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()

    def finish_repair(self):
        repair_id = self.repair_id_entry.get()
        
        repairs = read_csv('Report.csv')
        for repair in repairs:
            if repair[0] == repair_id:
                repair.append("Завершен")  # Добавляем статус "Завершен"
                break
        
        write_csv('Report.csv', repairs)
        self.withdraw()  # Скрываем текущее окно

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать предыдущее окно
        self.withdraw()  # Скрываем текущее окно
