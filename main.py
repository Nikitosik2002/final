import psycopg2
from config import host, user, password, db_name


def createTable():
    pet = input("Какое животное вы хотите добавить?\n"
                "Если вы хотите добавить домашнее "
                "живаотное напишите: pet\n"
                "Если вы хотите добавить вьючное животное напишите: pack\n"
                "Вы ввели: ")
    name = input("Введите имя животного: ")
    type = input("Введите тип животного: ")
    birthday = input("Введите день рождение животного: ")
    commands = input("Перечислите команды которые "
                     "умеет выполнять животное: ")
    if pet == 'pet':
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO pets (name, type, birthday, commands) VALUES
                ('{name}', '{type}', '{birthday}', '{commands}');"""
            )

            print("[INFO] Data was succefully inserted")
    elif pet == 'pack':
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO packanimals (name, type, birthday, commands) VALUES
                ('{name}', '{type}', '{birthday}', '{commands}');"""
            )

            print("[INFO] Data was succefully inserted")
    else:
        return createTable()


def commands():
    pet = input("Про какое животное вы хотите узнать?\n"
                "Если вы хотите узнать про домашнее "
                "живаотное напишите: pet\n"
                "Если вы хотите узнать про вьючное животное напишите: pack\n"
                "Вы ввели: ")
    if pet == 'pet':
        name = input(
            "Введите имя животного чтобы узнать что оно умеет: ")
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT commands FROM pets WHERE name = '{name}'"""
            )
            print(cursor.fetchone())
    elif pet == "pack":
        name = input(
            "Введите имя животного чтобы узнать что оно умеет: ")
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT commands FROM packanimals WHERE name = '{name}'
        """
            )
            print(cursor.fetchone())
    else:
        return commands()


def add_command():
    pet = input("Какое животное вы хотите обучить новой команде?\n"
                "Если вы вы хотите обучить домашнее  "
                "живаотное напишите: pet\n"
                "Если вы хотите вы хотите обучить вьючное "
                "животное напишите: pack\n"
                "Вы ввели: ")
    name = input("Введите имя животного чтобы обучить его: ")
    comm = input("Введите новую команду: ")
    if pet == 'pet':
        with connection.cursor() as cursor:
            cursor.execute(
                f"""UPDATE pets 
                        SET commands = CONCAT(commands, ', {comm}') 
                        WHERE name = '{name}'"""
            )
            print("[INFO] Data was succefully update")

    elif pet == "pack":
        with connection.cursor() as cursor:
            cursor.execute(
                f"""UPDATE packanimals 
                        SET commands = CONCAT(commands, ', {comm}') 
                        WHERE name = '{name}'"""
            )
            print("[INFO] Data was succefully update")
    else:
        return add_command()


def main_menu():
    while True:
        print("Выберите действие:")
        print("1. Добавить новое животное")
        print("2. Узнать команды животного")
        print("3. Обучить животное новой команде")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            createTable()
        elif choice == "2":
            commands()
        elif choice == "3":
            add_command()
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    try:
        # connect to the existing database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            print(f"Server version {cursor.fetchone()}")

        main_menu()

    except Exception as ex:
        print("Ошибка при работе с PostgreSQL:", ex)
    finally:
        if connection:
            connection.close()
            print("Соединение с PostgreSQL закрыто.")