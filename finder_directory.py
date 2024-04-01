import os
import shutil

# Функция отображает содержимое текущей директории
def display_contents(path="."):
    print("Содержимое текущей директории:")
    for item in os.listdir(path):
        print(item)

# Функция создает новый файл
def create_file(file_name):
    with open(file_name, 'w') as f:
        pass
    print(f"Файл {file_name} создан")

# Функция создает новую директорию
def create_directory(directory_name):
    os.makedirs(directory_name)
    print(f"Директория {directory_name} создана")

# Функция удаляет файл
def delete_file(file_name):
    os.remove(file_name)
    print(f"Файл {file_name} удален")

# Функция удаляет директорию
def delete_directory(directory_name):
    shutil.rmtree(directory_name)
    print(f"Директория {directory_name} удалена")

# Функция перемещает или переименовывает файл или директорию
def move_rename(src, dest):
    shutil.move(src, dest)
    print(f"Объект {src} успешно перемещен/переименован в {dest}")

# Функция выполняет поиск файлов по заданному пути, имени и/или расширению
def search_files(search_path, name=None, extension=None):
    found_files = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if (name is None or name in file) and (extension is None or file.endswith(extension)):
                found_files.append(os.path.join(root, file))
    return found_files


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Отобразить содержимое текущей директории")
        print("2. Создать новый файл")
        print("3. Создать новую директорию")
        print("4. Удалить файл")
        print("5. Удалить директорию")
        print("6. Переместить или переименовать файл или директорию")
        print("7. Поиск файлов по имени и/или расширению")
        print("8. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            display_contents()
        elif choice == "2":
            filename = input("Введите имя файла: ")
            create_file(filename)
        elif choice == "3":
            directory_name = input("Введите имя директории: ")
            create_directory(directory_name)
        elif choice == "4":
            filename = input("Введите имя файла для удаления: ")
            delete_file(filename)
        elif choice == "5":
            directory_name = input("Введите имя директории для удаления: ")
            delete_directory(directory_name)
        elif choice == "6":
            src = input("Введите путь исходного файла/директории: ")
            dest = input("Введите путь нового местоположения/имя файла: ")
            move_rename(src, dest)
        elif choice == "7":
            search_path = input("Введите путь для поиска: ")
            name = input("Введите имя файла (оставьте пустым, если не важно): ")
            extension = input("Введите расширение файла (оставьте пустым, если не важно): ")
            found_files = search_files(search_path, name, extension)
            print("Найденные файлы:")
            for file in found_files:
                print(file)
        elif choice == "8":
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")


# Вызов функции main() для выполнения программы через интерфейс
if __name__ == "__main__":
    main()
