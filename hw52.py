''' Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open('texthw52.txt') as hw:
    lines = hw.readlines()
    print("Number of lines: ", len(lines))

    for i, l in enumerate(lines):
        print(f'Number of words in line {i+1}: {len(l.split(" "))}')