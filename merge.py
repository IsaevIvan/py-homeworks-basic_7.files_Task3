import os


# Определяем относительные пути к файлам
current_dir = os.path.dirname(__file__)
file1 = os.path.join(current_dir, '1.txt')
file2 = os.path.join(current_dir, '2.txt')
output_file = os.path.join(current_dir, 'merged.txt')


# Используем контекстный менеджер для открытия и чтения файлов
with open(file2) as f2, open(file1) as f1, open(output_file, 'w') as out:
    out.write(f"{os.path.basename(file2)}\n")  # Имя файла
    out.write(f"1\n")  
    line2 = f2.readline().strip()  
    out.write(f"{line2}\n")  # Записываем её в итоговый файл

    out.write(f"{os.path.basename(file1)}\n")
    out.write(f"{2}\n")
    lines1 = [f1.readline().strip() for _ in range(2)]  # Берем только первые две строки
    for line in lines1:
        out.write(f"{line}\n")  # Записываем их в итоговый файл

