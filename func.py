import time

def readFile(filename, fields): # Чтение файла и сохранение построчно в список из словарей

    with open(filename, 'r', encoding='utf-8') as phb:
        contacts = phb.readlines()  # Двумерный список - список состоящий из списоков в которых находится одна строка из файла(каждая строка это данные о контакте)
        phone_book = [] # Список словарей record по каждому контакту

        for contact in contacts:
            record = dict(zip(fields, contact.split(', '))) # Словарь формата (название колонки : данные контакта)
            phone_book.append(record)
    return phone_book

def createMainColumn(fields): # Создание меню для выбора столбцов при поиска
    columnForFind = {}  # Словарь меню колонок для выбора

    for i in range(len(fields)-1):
        columnForFind[i + 1] = fields[i]
    columnForFind[len(fields)] = 'Завершить выбор столбцов'

    return columnForFind

def selectMainColumn(columnForFind): # Вывод меню выбора столбцов для поиска
    columnFind = []  # Список выбранных колонок для поиска
    column = ''

    while column != 5:
        print('Выберите колонку для поиска:')
        [print(i, j) for i, j in columnForFind.items()]

        try:
            column = int(input("Выберите номер нужных колонок для поиска: "))
        except ValueError: # Вылов ошибок при вводе букв
            print('Ошибка! Нужно ввести цифру!'.upper())
            time.sleep(2.5)
            continue

        try:
            if column != 5:
                if columnForFind[column] not in columnFind:
                    columnFind.append(columnForFind[column])
                    del columnForFind[column]

        except KeyError: # Вылов ошибок при выборе не существующего номена колонок
            print('Ошибка! Колонки с таким номером не существет!'.upper())
            time.sleep(2.5)
            continue
    print("Выбранные колонки: ", *columnFind)
    return columnFind

def contactChoice(phone_book, searchColumn, h):  # Выбор контакта
    fineContacts = []
    contactsForChoice = {}
    contact = []
    # Поиск кол-ва совпадений
    [fineContacts.append(list(i.values())) for i in phone_book if searchColumn.lower() == i[h.strip()].lower()]

    if fineContacts == []:  # Контактов не найдено, вывод предупреждения
        print(fineContacts[1])

    if len(fineContacts) > 1:  # Найдено несколько контактов
        for i in range(len(fineContacts)):
            contactsForChoice[i] = fineContacts[i]
        [print(i + 1, *j[:-1], j[-1].strip('\n')) for i, j in contactsForChoice.items()]  # Вывод списка контактов
        contact = input('Введите номер редактируемого контакта: ')  # Выбор нужного контакта
        if int(contact):
            contact = int(contact) - 1
            contact = contactsForChoice[contact]

    if fineContacts[0]:  # Найден только один контаткт
        contact = fineContacts[0]

    print(f"Выбранный контаткт: ", *contact)  # Вывод выбранного контакта
    return contact
def searchAndChoiceColumn(phone_book, columnFind, сhoice='update'):  # Поиск контакта по выбранным столбцам
    contacts = []
    inputData = 0

    while inputData < len(columnFind):

        for h in columnFind:
            searchColumn = input(f'Введите данные для поиска по колонке {h}: ')
            try:
                # Выбор контакта и вывод
                choiceContact = contactChoice(phone_book, searchColumn, h) # Выбранный контакт

                for i in phone_book:
                    if list(i.values()) == choiceContact and inputData == 0:
                        if i[h]:
                            if searchColumn.lower() == i[h].lower():
                                if сhoice == 'update':
                                    i[h] = input(f'Текшие данные: {h, i[h]}, введите новое значение: ').capitalize()  # Изменение данных у конкретного контакта
                                    inputData += 1
                                if сhoice == 'delete':
                                    print('Успешно удален!')
                                    inputData += 1
                                    continue
                    contacts.append(list(i.values()))  # Обновление двумерного списка со всеми контактами

            except KeyError:
                print('Ошибка! Не верные данные для поиска!')
                break
            except IndexError:
                print('Ошибка! Не верные данные для поиска!')
                break
            except ValueError:
                print('Ошибка! Введите цифру!')
                break
    return contacts

def writeToFile(filename, contacts): # Запись всех контактов из списка contacts в файл
        with open(filename, 'w', encoding='utf-8') as phb:
            for contact in contacts:
                phb.write(', '.join(contact).strip() + '\n')

