class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'Привет, меня зовут {self.name}\n'
              f'я родился {self.birth_date}\n'
              f'работаю {self.occupation}\n'
              f'Высшее образование: {"Да есть " if self.higher_education else "Нету"}\n')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education,group_name):
     super().__init__(name, birth_date, occupation, higher_education)
     self.group_name = group_name

    def introduce(self):
        print(f'Привет, меня зовут {self.name}\n'
            f'я одноклассник Алибека учились вместе в 11 B, родился {self.birth_date}\n'
            f'работаю: {self.occupation}\n'
            f'Высшее образование: {"Да есть " if self.higher_education else "Нету"}\n'
            f'У нас с Алибеком была рок-группа в школе называлась: {self.group_name}\n')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education,hobby):
     super().__init__(name, birth_date, occupation, higher_education)
     self.hobby = hobby

    def introduce(self):
        print(f'Привет, меня зовут {self.name},\n'
            f'я друг Алибека, я родился {self.birth_date},\n'
            f'работаю: {self.occupation}\n'
            f'Высшее образование: {"Да есть" if self.higher_education else "Нету"}\n'
            f'Мы с Алибеком ходили вместе на {self.hobby}')

people =[
Person('Алибек','05.10.2007','Программистом',False),
Classmate('Мирбек','18.11.2008','Музыкантом',True,'"Разрыв Тишины"'),
Friend('Умар','01.10.2008','Пограммистом',False,'"Бокс"')
]


for person in people:
    person.introduce()


