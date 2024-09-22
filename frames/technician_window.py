import customtkinter as ctk
from frames.add_repair_window import AddRepairWindow
from frames.finish_repair_window import FinishRepairWindow
from frames.view_machines_window import ViewMachinesWindow

class TechnicianWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Личный кабинет техника")
        self.geometry("600x400")
        self.previous_window = previous_window

        self.view_repairs_button = ctk.CTkButton(self, text="Просмотр ремонтов", command=self.view_repairs)
        self.view_repairs_button.pack(pady=10)

        self.add_repair_button = ctk.CTkButton(self, text="Добавить факт ремонта", command=self.add_repair)
        self.add_repair_button.pack(pady=10)

        self.finish_repair_button = ctk.CTkButton(self, text="Закончить ремонт", command=self.finish_repair)
        self.finish_repair_button.pack(pady=10)

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()

    def view_repairs(self):
        ViewMachinesWindow(previous_window=self).mainloop()

    def add_repair(self):
        AddRepairWindow(previous_window=self).mainloop()

    def finish_repair(self):
        FinishRepairWindow(previous_window=self).mainloop()

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать предыдущее окно
        self.withdraw()  # Скрываем текущее окно
