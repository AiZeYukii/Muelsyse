import tkinter as tk
from calculator import calculate_cost


class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Калькулятор стоимости рекламных материалов")

        # Настройки шрифтов
        font_size = 14
        font = ("Arial", font_size)

        # Надпись и поле ввода площади
        area_label = tk.Label(self, text="Площадь (кв.м):", font=font)
        area_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")
        self.area_entry = tk.Entry(self, font=font)
        self.area_entry.grid(row=0, column=1, padx=10, pady=15)

        # Надпись и поле ввода стоимости материала
        material_cost_label = tk.Label(self, text="Стоимость материала (руб./кв.м):", font=font)
        material_cost_label.grid(row=1, column=0, padx=10, pady=15, sticky="w")
        self.material_cost_entry = tk.Entry(self, font=font)
        self.material_cost_entry.grid(row=1, column=1, padx=10, pady=15)

        # Надпись и поле ввода стоимости монтажа
        installation_cost_label = tk.Label(self, text="Стоимость монтажа (руб.):", font=font)
        installation_cost_label.grid(row=2, column=0, padx=10, pady=15, sticky="w")
        self.installation_cost_entry = tk.Entry(self, font=font)
        self.installation_cost_entry.grid(row=2, column=1, padx=10, pady=15)

        # Надпись и поле ввода дополнительных услуг
        additional_services_cost_label = tk.Label(self, text="Дополнительные услуги (руб.):", font=font)
        additional_services_cost_label.grid(row=3, column=0, padx=10, pady=15, sticky="w")
        self.additional_services_cost_entry = tk.Entry(self, font=font)
        self.additional_services_cost_entry.grid(row=3, column=1, padx=10, pady=15)

        # Кнопка "Рассчитать"
        calculate_button = tk.Button(self, text="Рассчитать", command=self.calculate_total_cost, font=font)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Поле вывода результата
        self.result_label = tk.Label(self, text="", font=font)
        self.result_label.grid(row=5, column=0, columnspan=2)

    def calculate_total_cost(self):
        try:
            area = self.area_entry.get()
            material_cost = self.material_cost_entry.get()
            installation_cost = self.installation_cost_entry.get()
            additional_services_cost = self.additional_services_cost_entry.get()

            result = calculate_cost(area, material_cost, installation_cost, additional_services_cost)
            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Пожалуйста, введите числовые значения.")