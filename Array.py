from Film import film_get_from_file, film_record_to_file

class Array:
    def __init__(self, maxSize):
        self.size = 0
        self.content = []
        self.maxSize = maxSize

def Array_append(Array, element):
    if Array.size < Array.maxSize:
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
        film = film_get_from_file(type, file)
        Array_append(Array, film)
        type = file.readline()

def Array_record_to_file(array, file):
    file.write(f"Записано {array.size} фильмов\n\n")
    for i in range(array.size):
        film_record_to_file(array.content[i], file)