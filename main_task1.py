from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    # Валідація номеру телефону
    def __init__(self, phone_number):
        if not (len(phone_number) == 10 and phone_number.isdigit()):
            raise ValueError('Number is not correct!')
        super().__init__(phone_number)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Метод для додавання номеру телефону
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    # Метод для видалення номеру телефону
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)

    # Метод для редагування номеру телефону
    def edit_phone(self, old_phone_number, new_phone_number):
        try:
            for phone in self.phones:
                if phone.value == old_phone_number:
                    phone.value = Phone(new_phone_number).value
                else:
                    raise ValueError('Number is not exist')
        except ValueError as e:
            return f'{e}'

    # Метод для пошуку об'єктів Phone
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

 # Магічний метод для красивого виводу об’єкту класу
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"


class AddressBook(UserDict):
    # Метод який додає запис до self.data
    def add_record(self, record_name):
        self.data[record_name.name.value] = record_name

    # Метод який знаходить запис за ім'ям.
    def find(self, find_name):
        return self.data.get(find_name)

    # Метод який видаляє запис за ім'ям.
    def delete(self, delete_name):
        if delete_name in self.data:
            del self.data[delete_name]

    # Магічний метод для красивого виводу об’єктів класу
    def __str__(self):
        if not self.data:
            return "Address Book is empty."

        result = "Address Book:\n"
        result += "-" * 40 + "\n"
        for name, record in self.data.items():
            result += f"{record}\n"
            result += "- " * 20 + "\n"
        return result


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

