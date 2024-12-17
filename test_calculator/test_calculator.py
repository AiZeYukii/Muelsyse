import unittest
from calculator import calculate_cost

class TestCalculateCost(unittest.TestCase):

    def test_calculate_cost(self):
        # Тестирование корректного расчета стоимости
        area = 10.0
        material_cost = 50.0
        installation_cost = 200.0
        additional_services_cost = 100.0
        result = calculate_cost(area, material_cost, installation_cost, additional_services_cost)
        self.assertEqual(result, "Общая стоимость: 800.00 руб.")

    def test_empty_input(self):
        # Тестирование пустых данных
        area = 0.0
        material_cost = 0.0
        installation_cost = 0.0
        additional_services_cost = 0.0
        result = calculate_cost(area, material_cost, installation_cost, additional_services_cost)
        self.assertEqual(result, "Общая стоимость: 0.00 руб.")

    def test_invalid_input(self):
        # Тестирование некорректных данных (например, текст вместо чисел)
        with self.assertRaises(ValueError):
            area = "abc"  # Некорректный ввод
            material_cost = 50.0
            installation_cost = 200.0
            additional_services_cost = 100.0
            # Попытка преобразовать строку в число вызовет ошибку
            calculate_cost(float(area), material_cost, installation_cost, additional_services_cost)

    def test_zero_input(self):
        # Тестирование с нулевыми значениями
        area = 0.0
        material_cost = 100.0
        installation_cost = 200.0
        additional_services_cost = 100.0
        result = calculate_cost(area, material_cost, installation_cost, additional_services_cost)
        self.assertEqual(result, "Общая стоимость: 300.00 руб.")

    def test_large_input(self):
        # Тестирование с большими значениями
        area = 10000.0
        material_cost = 1000.0
        installation_cost = 2000.0
        additional_services_cost = 1000.0
        result = calculate_cost(area, material_cost, installation_cost, additional_services_cost)
        self.assertEqual(result, "Общая стоимость: 12000000.00 руб.")

    def test_negative_values(self):
        # Тестирование с отрицательными значениями
        with self.assertRaises(ValueError):
            area = -10.0  # Отрицательная площадь
            material_cost = 50.0
            installation_cost = 200.0
            additional_services_cost = 100.0
            calculate_cost(area, material_cost, installation_cost, additional_services_cost)

if __name__ == "__main__":
    unittest.main()
