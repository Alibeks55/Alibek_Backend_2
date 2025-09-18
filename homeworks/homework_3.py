from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        today = datetime.today()
        years = today.year - self.__birth_date.year
        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
            years -= 1
        return years

    def introduce(self):
        print(f'Привет, меня зовут {self.name},\n'
              f'мне {self.age} лет,\n'
              f'работаю: {self.occupation},\n'
              f'У меня {"есть" if self.higher_education else "нету"} высшее образование.\n')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f'Привет, меня зовут {self.name},\n'
              f'я одноклассник Алибека, мне {self.age} лет,\n'
              f'работаю: {self.occupation},\n'
              f'У меня {"есть" if self.higher_education else "нету"} высшее образование,\n'
              f'У нас с Алибеком была рок-группа:{self.group_name}.\n')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'Привет, меня зовут {self.name},\n'
              f'мне {self.age} лет,\n'
              f'работаю: {self.occupation},\n'
              f'У меня {"есть" if self.higher_education else "нету"} высшее образование,\n'
              f'Мы с Алибеком ходили вместе на {self.hobby}\n')

people = [
    Person('Алибек', '05.10.2007', 'Программистом', False),
    Classmate('Мирбек', '18.11.2008', 'Музыкантом', True, '"Разрыв Тишины"'),
    Friend('Умар', '01.10.2008', 'Программистом', False, '"Бокс"')
]

for person in people:
    person.introduce()









