import os
import shutil
import sys

def copy_and_sort(source_dir, dest_dir):
    try:
        # Перевірка чи існує директорія призначення, і якщо ні - створення
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Перегляд усіх елементів у вихідній директорії
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)

            # Якщо елемент - директорія, викликати рекурсивно функцію для неї
            if os.path.isdir(item_path):
                copy_and_sort(item_path, dest_dir)

            # Якщо елемент - файл, скопіювати його у відповідну піддиректорію
            elif os.path.isfile(item_path):
                # Отримання розширення файлу
                _, extension = os.path.splitext(item)

                # Створення піддиректорії за розширенням файлу
                sub_dir = os.path.join(dest_dir, extension[1:])
                if not os.path.exists(sub_dir):
                    os.makedirs(sub_dir)

                # Копіювання файлу у відповідну піддиректорію
                shutil.copy2(item_path, sub_dir)
    
    except Exception as e:
        print(f"Помилка обробки: {e}")

if __name__ == "__main__":
    # Перевірка наявності аргументів командного рядка
    if len(sys.argv) != 3:
        print("Використання: python task_1.py <вихідна_директорія> <директорія_призначення>")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    # Виклик головної функції для копіювання та сортування
    copy_and_sort(source_dir, dest_dir)
