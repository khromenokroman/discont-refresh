#!/usr/bin/python3
import os

FILE = 'Pos01.spr' #файл с данными
FILE_FLAG = 'Pos01.flz' #файл флаг
PATH = '/home/roma/Coding/atol-zapret-skidki' #путь до папки
FOLDER = 'datasource' #папка в которой должны оказаться файлы
FIND = ['Сигареты', 'Пиво'] # товары которые ограничить

def get_data_file(path): #читаем содержимое файла
    with open(path, 'r', encoding='cp1251') as file:
        data_file = file.readlines()
        return data_file
    
def remake_file(str_text): #переделываем строку добавляем в 29 параметр значение 0
    count_str = 1
    with open(f'{PATH}/{FOLDER}/{FILE}', 'w', encoding='cp1251') as file:
        for line in str_text:
            if count_str == 2:
               file.write('#\n')
               count_str += 1
               continue 
            if len(line) < 150: #лишнее отбросим группы, шк ит.д
                file.write(line)
            else:
                for i in FIND:
                    if i in line:
                        # print(line.strip())
                        line_original = line.strip()
                        line_detail = line_original.split(';')
                        count = 1
                        new_str = ''
                        for value in line_detail:
                            if count == 67:
                                new_str += f'{value}'
                            elif count == 29:
                                new_str += '0;'
                            else:
                                new_str += f'{value};'
                            count+=1
                        file.write(new_str)
                    else:
                        file.write(line)
            count_str += 1
    
    #создадим файл флаг
    with open(f'{PATH}/{FOLDER}/{FILE_FLAG}', 'w') as f:
        f.write('')

def remove_1c_data():
    os.system(f'rm {PATH}/{FILE}')
    os.system(f'rm {PATH}/{FILE_FLAG}')

if __name__ == '__main__':
    if os.path.isfile(f'{PATH}/{FOLDER}/{FILE_FLAG}'):
        print('Не могу обработать файл потому что еть задание для загрузки...')
    else:
        try:
            text_file = get_data_file(f'{PATH}/{FILE}')
            remake_file(text_file)
        except:
            print('Нет документов для изменения')
        remove_1c_data()