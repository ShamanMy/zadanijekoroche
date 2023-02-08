def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Недотреугольник"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Прямоугольный треугольник"
    elif a == b == c:
        return "Равнобедренный треугольник"
    elif a == b or a == c or b == c:
        return "Широкоугольный треугольник"
    else:
        return "Треугольник неизвестного типа"

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

result = classify_triangle(a, b, c)
print("ООООтвЕЕЕт:", result)

#print(classify_triangle(3, 4, 5)) # Вывод "Прямоугольный треугольник"
#print(classify_triangle(3, 3, 3)) # Вывод "Равнобедренный треугольник"
#print(classify_triangle(3, 3, 4)) # Вывод "Широкоугольный треугольник"
#print(classify_triangle(3, 3, 7)) # Вывод "плохо"