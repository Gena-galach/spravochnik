# Основные функции
def load_data(filename):
    """Загрузка данных из файла"""
    phonebook = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    surname, name, phone, description = parts
                    phonebook.append([surname.strip(), name.strip(), phone.strip(), description.strip()])
    except FileNotFoundError:
        print("Файл не найден. Создается новый файл.")
        open(filename, 'w').close()
    return phonebook

def save_data(filename, phonebook):
    """Сохранение данных в файл"""
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(', '.join(entry) + '\n')

def display_data(phonebook):
    """Вывод данных"""
    if not phonebook:
        print("Справочник пуст.")
    else:
        for entry in phonebook:
            print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Телефон: {entry[2]}, Описание: {entry[3]}")

def search_data(phonebook, query):
    """Поиск данных"""
    results = [entry for entry in phonebook if query in entry]
    if results:
        for entry in results:
            print(f"Фамилия: {entry[0]}, Имя: {entry[1]}, Телефон: {entry[2]}, Описание: {entry[3]}")
    else:
        print("Запись не найдена.")

def add_entry(phonebook, surname, name, phone, description):
    """Добавление записи"""
    phonebook.append([surname, name, phone, description])

# Основная часть программы
def main():
    filename = 'phon.txt'
    phonebook = load_data(filename)
    
    while True:
        print("\nТелефонный справочник:")
        print("1. Показать все записи")
        print("2. Добавить запись")
        print("3. Найти запись")
        print("4. Сохранить и выйти")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            display_data(phonebook)
        elif choice == '2':
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            description = input("Введите описание: ")
            add_entry(phonebook, surname, name, phone, description)
        elif choice == '3':
            query = input("Введите имя, фамилию, номер телефона или описание для поиска: ")
            search_data(phonebook, query)
        elif choice == '4':
            save_data(filename, phonebook)
            print("Данные сохранены. Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
