from homeworks.distance import Distance

d1 = Distance(10, "m")
d2 = Distance(200, "cm")
d3 = Distance(1, "km")

print("----- Проверка str -----")
print(d1)
print(d2)
print(d3)

print("\n----- Сложение -----")
print(d1 + d2)
print(d1 + d3)

print("\n----- Вычитание -----")
print(d3 - d1)
print(d2 - d1)

print("\n----- Сравнение -----")
print(Distance(100, "m") == Distance(0.1, "km"))
print(Distance(999, "m") < Distance(1, "km"))
print(Distance(1, "m") > Distance(500, "cm"))







