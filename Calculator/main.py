from app.shapes import Parallelepiped, Cube

Shape.about() # Вывод информации о команде

parallelepiped = Parallelepiped(5, 10, 2)
print(f"Объем параллелепипеда: {parallelepiped.volume()}")

cube = Cube(3)
print(f"Объем куба: {cube.volume()}")
print(f"Площадь поверхности куба: {cube.surface_area()}")
