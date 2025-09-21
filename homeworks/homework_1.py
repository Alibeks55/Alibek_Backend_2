class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(
            f"Имя: {self.name}\n"
            f"Дата рождения: {self.birth_date}\n"
            f"Профессия: {self.occupation}\n"
            f"Высшее образование: {'Да' if self.higher_education else 'Нет'}\n")



person1 = Person("Алибек", "05.10.2007", "Программист", False)
person2 = Person("Айдай",  "31.05.2000", "Кондитер",    True)
person3 = Person("Жусуп", "29.07.1999", "Программист", False)

person1.introduce()
person2.introduce()
person3.introduce()