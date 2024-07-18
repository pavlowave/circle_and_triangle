from geometry import Circle, Triangle

circle = Circle(5)
print(f"Площадь круга: {circle.area()}")

triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.area()}")

if triangle.is_right_triangle():
    print("Треугольник является прямоугольным.")
else:
    print("Треугольник не является прямоугольным.")

