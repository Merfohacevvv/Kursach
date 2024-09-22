import customtkinter as ctk
import tkinter as tk  # Для использования стандартного Listbox
from helpers import read_csv

class ViewMachinesWindow(ctk.CTk):
    def __init__(self, previous_window=None):
        super().__init__()
        self.title("Просмотр станков")
        self.geometry("600x400")
        self.previous_window = previous_window

        # Используем стандартный Listbox для отображения списка станков
        frame = ctk.CTkFrame(self)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        self.machine_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=15, width=50)
        self.machine_listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.machine_listbox.yview)

        self.load_machines()

        # Кнопка "Назад"
        self.back_button = ctk.CTkButton(self, text="Назад", command=self.go_back)
        self.back_button.pack(pady=10)

        if self.previous_window:
            self.previous_window.withdraw()

    def load_machines(self):
        machines = read_csv('Machines.csv')
        for machine in machines:
            machine_str = f"{machine[0]} - {machine[1]} - {machine[2]} - {machine[3]}"
            self.machine_listbox.insert("end", machine_str)

    def go_back(self):
        if self.previous_window:
            self.previous_window.deiconify()  # Показать предыдущее окно
        self.withdraw()  # Скрываем текущее окно
