import sys
from Array import Array, Array_fill, Array_record_to_file, Array_clear

if len(sys.argv) != 3:
    print('\nФайлы ввода/вывода не выбраны! Будут использованы стандартные in.txt и out.txt\n')
    infile = 'in.txt'
    outfile = 'out.txt'
else:
    infile = sys.argv[1]
    outfile = sys.argv[2]

infile = open(infile, 'r', encoding = "utf-8")
a = Array(12)
Array_fill(a, infile)
print(f"В контейнер записано {a.size} фильмов\n")
infile.close()

outfile = open(outfile, 'w', encoding = "utf-8")
Array_record_to_file(a, outfile)
outfile.close()
Array_clear(a)