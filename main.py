from func import *
import time

def work_with_phonebook():
    choice = show_menu()
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']  # Список столбцов контактной книги
    phone_book = 'phonebook.txt'

    while (choice != 5):

        if choice == 1:
            print_result(phone_book, fields)
        elif choice == 2:
            addContact(phone_book, fields)
        elif choice == 3:
            delete_contact(phone_book, fields)
        elif choice == 4:
            update_contact(phone_book, fields)
        elif choice == 5:
            break
        choice = show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Показать справочник\n" 
          "2. Добавить контакт\n"
          "3. Удалить контакт\n"
          "4. Изменить данные контакта\n"
          "5. Закончить работу"
          )
    choice = int(input())
    return choice

# Вывод всех контактов
def print_result(filename, fields):
    phone_book = readFile(filename, fields)
    time.sleep(1)
    for i in phone_book:
        print(*i.values(), end='')

def addContact(filename, fields ):
    record = {}
    contacts = []
    phone_book = readFile(filename, fields)
    for i in fields:
        record[i] = input(f'{i}: ')  # Словарь формата (название колонки : Ввод данных контакта)
    phone_book.append(record)
    for i in phone_book:
        contacts.append(list(i.values()))  # Обновление двумерного списка со всеми контактами
    writeToFile(filename, contacts)

# Удаление контакта
def delete_contact(filename, fields):
    phone_book = readFile(filename, fields)
    columnForFind = createMainColumn(fields)
    columnFind = selectMainColumn(columnForFind)
    contacts = searchAndChoiceColumn(phone_book, columnFind, сhoice='delete')
    writeToFile(filename, contacts)

# Обновление контакта
def update_contact(filename, fields):
    phone_book = readFile(filename, fields)
    columnForFind = createMainColumn(fields)
    columnFind = selectMainColumn(columnForFind)
    contacts = searchAndChoiceColumn(phone_book, columnFind)
    writeToFile(filename, contacts)

work_with_phonebook()


