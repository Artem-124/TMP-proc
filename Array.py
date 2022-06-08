from Film import *

class Array:
    def __init__(self, max_size):
        self.size = 0
        self.content = []
        self.max_size = max_size

def Array_append(Array, element):
    if Array.size < Array.max_size:
        Array.size += 1
        Array.content.append(element)
    else:
        print("Массив уже заполнен! Элемент не будет записан")

def Array_clear(Array):
    Array.size = 0
    Array.data = []

def Array_fill(Array, file):
    type = file.readline()
    while type != '' and type != '\n':
        type = int(type)
        film = Film_get_from_file(type, file)
        Array_append(Array, film)
        type = file.readline()

def Array_record_to_file(array, file):
    file.write(f"Записано {array.size} фильмов\n\n")
    for i in range(array.size):
        Film_record_to_file(array.content[i], file)

def Array_only_one_type_record_to_file(array, file, type):
        if type == 0:
            Array_record_to_file(array, file)
            return
        num = 0
        for i in range(array.size):
            if array.content[i].type == type:
                Film_record_to_file(array.content[i], file)
                num += 1
        if num == 1:
            file.write(f"\nЗаписан {num} фильм\n")
        if num > 1 and num <= 4:
            file.write(f"\nЗаписано {num} фильма\n")
        if num >= 5:
            file.write(f"\nЗаписано {num} фильмов\n")

def Array_sort(array):
    for j in range(1, array.size):
        for i in range(array.size - j):
            if comparator(array.content[i], array.content[i + 1]):
                array.content[i], array.content[i + 1] = array.content[i + 1], array.content[i]
