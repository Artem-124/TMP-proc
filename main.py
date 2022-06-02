import sys
from Array import *

if len(sys.argv) != 3:
    print('\nФайлы ввода/вывода не выбраны! Будут использованы стандартные in.txt и out.txt\n')
    infile = 'in.txt'
    outfile = 'out.txt'
else:
    infile = sys.argv[1]
    outfile = sys.argv[2]

infile = open(infile, 'r', encoding = "utf-8")
a = Array(15)
Array_fill(a, infile)
print(f"В контейнер записано {a.size} фильмов\n")
infile.close()

outfile = open(outfile, 'w', encoding = "utf-8")

outfile.write('    ╔════════════════════╗\n')
outfile.write('    ║ Исходный контейнер ║\n')
outfile.write('    ╚════════════════════╝\n\n')
Array_record_to_file(a, outfile)

Array_sort(a)

outfile.write('    ╔═══════════════════════════╗\n')
outfile.write('    ║ Отсортированный контейнер ║\n')
outfile.write('    ╚═══════════════════════════╝\n\n')
Array_record_to_file(a, outfile)

outfile.write('    ╔═══════════════════════════╗\n')
outfile.write('    ║ Отфильтрованный контейнер ║\n')
outfile.write('    ╚═══════════════════════════╝\n\n')
Array_only_one_type_record_to_file(a, outfile, 3) #0 - все фильмы

outfile.close()

Array_clear(a)