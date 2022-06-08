from enum import Enum

class Film:
    def __init__(self, type):
        self.title = ''
        self.type = type
        self.country = ''
        self.void = None


class Feature:
    def __init__(self):
        self.director = ""


class Cartoon:
    def __init__(self):
        self.way_to_create = None


class Doсumentary:
    def __init__(self):
        self.year = 1900


class WayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3


def Film_get_from_file(type, file):
    film = Film(type)
    film.title = file.readline()
    film.country = file.readline()
    if type == 1:
        film.void = Feature()
        film.director = file.readline()
    if type == 2:
        film.void = Cartoon()
        film.way_to_create  = WayToCreate(int(file.readline()))
    if type == 3:
        film.void = Doсumentary()
        film.year = int(file.readline())
    return film

def Film_record_to_file(film, file):
    file.write(film.title)
    file.write(f"Страна: {film.country}")
    if film.type == 1:
        file.write("Художественный фильм\n")
        file.write(f"Режиссер: {film.director}")
    if film.type == 2:
        file.write("Мультфильм\n")
        if film.way_to_create == WayToCreate.drawn:
            file.write("Рисованный\n")
        if film.way_to_create == WayToCreate.puppet:
            file.write("Кукольный\n")
        if film.way_to_create == WayToCreate.plasticine:
            file.write("Пластилиновый\n")
    if film.type == 3:
        file.write("Документальный фильм\n")
        file.write(f"Год: {film.year}\n")            
    file.write(f"Количество гласных в названии: {number_of_vowels(film.title)}\n")    
    file.write('\n')

def number_of_vowels(title):
    voves = 'аеёиоуыэюяaeiouy'
    num = 0
    for letter in title:
        if letter.lower() in voves:
            num += 1
    return num

def comparator(a, b):
    return number_of_vowels(a.title) > number_of_vowels(b.title)        
       
    
