from enum import Enum

class Film:
    def __init__(self, type):
        self.title = ''
        self.type = type
        self.void = None

class Feature:
    def __init__(self):
        self.director = ""

class Cartoon:
    def __init__(self):
        self.wayToCreate = None

class Doсumentary:
    def __init__(self):
        self.year = 1900

class wayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3

def film_get_from_file(type, file):
    film = Film(type)
    film.title = file.readline()
    if type == 1:
        film.void = Feature()
        film.director = file.readline()
    if type == 2:
        film.void = Cartoon()
        film.wayToCreate = wayToCreate(int(file.readline()))
    if type == 3:
        film.void = Doсumentary()
        film.year = int(file.readline())
    return film

def film_record_to_file(film, file):
    file.write(film.title)
    if film.type == 1:
        file.write("Художественный фильм\n")
        file.write(f"Режиссер: {film.director}")
    if film.type == 2:
        file.write("Мультфильм\n")
        if film.wayToCreate == wayToCreate.drawn:
            file.write("Рисованный\n")
        if film.wayToCreate == wayToCreate.puppet:
            file.write("Кукольный\n")
        if film.wayToCreate == wayToCreate.plasticine:
            file.write("Пластилиновый\n")
    if film.type == 3:
        file.write("Документальный фильм\n")
        file.write(f"Год: {film.year}\n")    
    file.write('\n') 