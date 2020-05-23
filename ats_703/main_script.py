#этот файл - объединение Artem_Krytsin.py и Yakushenkov_Konstantin.py
import os
import json
import codecs
import subprocess
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl import load_workbook

#Крыцин Артём
#-----------------------------------------------------------------------------------
#начальная конфигурация
gcc = "gcc"

gcc_path = "C:/MinGW/bin/gcc.exe"
gcc_command = "%s *.c *.h" % gcc_path

gpp_path = "C:/MinGW/bin/g++.exe"
#-----------------------------------------------------------------------------------
#парсер файла main
data_from_file = [] #подумать как расположить поудобнее

def file_parser(student_index, file_name, file_path):  
    data_from_file.append([])    
    with codecs.open(file_path + "\\" + file_name, 'r', "utf-8") as read_file:
        for line in read_file:
            my_string = line
            if ((my_string[0] == 'С') and (my_string[1] == 'т')):
                my_string = line.strip("Студент: \r\n")
                data_from_file[student_index].append(my_string)
            if ((my_string[0] == 'Г') and (my_string[1] == 'р')):
                if data_from_file: #доделать проверку
                    my_string = line.strip("Группа № \r\n")
                    data_from_file[student_index].append(my_string)
            if ((my_string[0] == 'З') and (my_string[1] == 'а')):
                if data_from_file: #доделать проверку
                    my_string = line.strip("Задание № \r\n")
                    data_from_file[student_index].append(my_string)

    print(data_from_file)
#-----------------------------------------------------------------------------------
#достаем Ф.И. всех студентов из json файла
with open(os.getcwd() + "\\ats_703\\students_database.json") as json_file:
    students_database = json.load(json_file)
#-----------------------------------------------------------------------------------
#достаем Ф.И. всех студентов из json файла
with open(os.getcwd() + "\\ats_703\\exercises_database.json") as json_file:
    exercises_database = json.load(json_file)
#-----------------------------------------------------------------------------------
#тут обход директорий и запуск парсера
main_directory_tree = os.walk('ats_703')

students = [] #массив с именами студентов, папки которых хранятся в директории SOURCE

source_folder_directory = os.getcwd() + "\\ats_703\\SOURCE"

g_main_folder = []
g_source_folder = []

for loc_i in main_directory_tree:
    g_main_folder.append(loc_i)

for address, dirs, files in g_main_folder:
    for dir in dirs:
        if(dir == 'SOURCE'):
            source_tree = os.walk(source_folder_directory)
            for loc_j in  source_tree:
                g_source_folder.append(loc_j)

for address, dirs, files in g_source_folder:
    for dir in dirs:
        for loc_k in range(len(students_database)):
            if(dir == students_database[loc_k]):
                students.append(students_database[loc_k])

for loc_i in range(len(students)):
    student_folder = [] #содержимое папки конкретного студента
    exercises_folder = [] #задания в папке студента 
    student_directory = source_folder_directory + "\\" + students[loc_i]
    student_directory_tree = os.walk(student_directory)
    for loc_j in student_directory_tree:
        student_folder.append(loc_j)
    for address, dirs, files in student_folder:
        for dir in dirs:
            for loc_k in range(len(exercises_database)):
                if(dir == exercises_database[loc_k]):
                    exercises_folder.append(exercises_database[loc_k])

    for loc_e in range(len(exercises_folder)):
        exercise_folder = []
        each_exercise_folder_path = student_directory + "\\" + exercises_folder[loc_e]
        exercise_directory_tree = os.walk(each_exercise_folder_path)
        for loc_g in each_exercise_folder_path:
            exercise_folder.append(loc_g)
        for address, dirs, files in student_folder:
            for file in files:
                base = os.path.splitext(file)[0]
                if(base == 'main'):
                    file_parser(loc_i, file, each_exercise_folder_path)

        curr_path = os.getcwd()
        #os.chdir(each_exercise_folder_path)
        change_dir_command = "cd " + each_exercise_folder_path
        subprocess.Popen(change_dir_command)
        print(os.getcwd())

        process = subprocess.Popen(gcc_command)
        returncode = process.wait()
        print(returncode)

#===================================================================================
#===================================================================================
#Якушенков Константин

result = []
result.append('Апидова_Анастас\n')
result.append('406\n')
result.append('1_1\n')
result.append('Fail\n')
result.append('1 - Fail\n2 - Fail\n3 - Pass\n4 - Pass\n5 - Fail\n')

def Preload():
    worksheet["A1"] =  'Студент'
    worksheet["B1"] =  'Группа'
    worksheet["C1"] =  '1.1'
    worksheet["D1"] =  '1.2'
    worksheet["E1"] =  '1.3'
    worksheet["F1"] =  '1.4'
    worksheet["G1"] =  '1.5'
    worksheet["H1"] =  '2.1'
    worksheet["I1"] =  '2.2'
    worksheet["J1"] =  '2.3'
    worksheet["K1"] =  '2.4'
    worksheet["L1"] =  '2.5'
    worksheet["M1"] =  '3.1'
    worksheet["N1"] =  '3.2'
    worksheet["O1"] =  '3.3'
    worksheet["P1"] =  '3.4'
    worksheet["Q1"] =  '3.5'
    worksheet["R1"] =  '4.6'
    worksheet["S1"] =  '4.7'
    worksheet["T1"] =  '4.8'
    worksheet["U1"] =  '4.9'
    worksheet["V1"] =  '5.4'
    worksheet["W1"] =  '5.5'
    worksheet["X1"] =  '5.6'
    worksheet["Y1"] =  '5.7'
    worksheet["Z1"] =  '5.8'
    worksheet["AA1"] =  '5.9'
    worksheet["AB1"] =  '5.10'
    worksheet["AC1"] =  '6.1'
    worksheet["AD1"] =  '6.2'

#расстояние Левенштейна
def Levenshtein(comparedString1, comparedString2):
    n, m = len(comparedString1), len(comparedString2)
    if n > m:
        comparedString1, comparedString2 = comparedString2, comparedString1
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if comparedString1[j - 1] != comparedString2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]

#применение этого расстояния
def CompareStrings(name_counter):
    i = 0
    comparedName = ''
    comparedSurname = ''
    while result[0][i] != '_':
        comparedSurname = comparedSurname + result[0][i]
        i = i + 1
    i = i + 1
    while result[0][i] != '\n':
        comparedName = comparedName + result[0][i]
        i = i + 1
    i = 0
    perfectName = ''
    perfectSurname = ''
    while studentsList[name_counter][i] != '_':
        perfectSurname = perfectSurname + studentsList[name_counter][i]
        i = i + 1
    i = i + 1
    while studentsList[name_counter][i] != '\n':
        perfectName = perfectName + studentsList[name_counter][i]
        i = i + 1
    i = 0
    dist1 = Levenshtein(comparedName,perfectName)
    dist2 = Levenshtein(comparedSurname, perfectSurname)
    dist3 = Levenshtein(comparedName, perfectSurname)
    dist4 = Levenshtein(comparedSurname, perfectName)
    if ((global_a[0] != '9') and (global_a[0] != '1')):
        if((dist1 != 0) and (dist2 != 0)):
            if(dist1 < dist3):
                if(dist2 < dist4):
                    print('Возможно вы имели в виду:', perfectSurname, perfectName, '? | 1 - да, 0 - нет, 9 - выход')
                    tmp_a = input()
                    global_a.remove(global_a[0])
                    global_a.insert(0, tmp_a)
                    if (global_a[0] == '1'):
                        global_a[1] = name_counter + 2
                else:
                    pass
            else:
                if(dist2 < dist4):
                    pass
                else:
                    print('Возможно вы имели в виду:', perfectSurname, perfectName, '? | 1 - да, 0 - нет, 9 - выход')
                    tmp_a = input()
                    global_a.remove(global_a[0])
                    global_a.insert(0, tmp_a)
                    if (global_a[0] == '1'):
                        global_a[1] = name_counter + 2
    else:
        pass
    if (studentsList[name_counter] != 'Якушенков_Константин\n'):
        name_counter = name_counter + 1
        CompareStrings(name_counter)


def WriterXLSX():
    temp_cell = 'A'
    temp_cell = temp_cell + str(global_a[1])
    worksheet[temp_cell] =  studentsList[global_a[1] - 2]
    temp_cell = 'B'
    temp_cell = temp_cell + str(global_a[1])
    worksheet[temp_cell] =  result[1]
    if result[2] == '1_1':
        temp_cell = 'C'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '1_2':
        temp_cell = 'D'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '1_3':
        temp_cell = 'E'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '1_4':
        temp_cell = 'F'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '1_5':
        temp_cell = 'G'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '2_1':
        temp_cell = 'H'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '2_2':
        temp_cell = 'I'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '2_3':
        temp_cell = 'J'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '2_4':
        temp_cell = 'K'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '2_5':
        temp_cell = 'L'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '3_1':
        temp_cell = 'M'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '3_2':
        temp_cell = 'N'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '3_3':
        temp_cell = 'O'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '3_4':
        temp_cell = 'P'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '3_5':
        temp_cell = 'Q'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '4_6':
        temp_cell = 'R'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '4_7':
        temp_cell = 'S'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '4_8':
        temp_cell = 'T'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '4_9':
        temp_cell = 'U'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '5_4':
        temp_cell = 'V'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '5_5':
        temp_cell = 'W'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '5_6':
        temp_cell = 'X'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '5_7':
        temp_cell = 'Y'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '5_8':
        temp_cell = 'Z'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '5_9':
        temp_cell = 'AA'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '5_10':
        temp_cell = 'AB'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '6_1':
        temp_cell = 'AC'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment
    if result[2] == '6_2':
        temp_cell = 'AD'
        temp_cell = temp_cell + str(global_a[1])
        worksheet[temp_cell] =  result[3]
        comment = Comment(result[4], "Results")
        worksheet[temp_cell].comment = comment



workbook = load_workbook('Test_406_407_16_7sem.xlsx')
worksheet = workbook.active

#заменить на массив из json
studentsList = []
studentsList.append('Аспидова_Анастасия\n')
studentsList.append('Касько_Кирилл\n')
studentsList.append('Копосова_Софья\n')
studentsList.append('Курганов_Дмитрий\n')
studentsList.append('Тавказаков_Магомет\n')
studentsList.append('Хоружий_Илья\n')
studentsList.append('Хромова_Кристина\n')
studentsList.append('Чертков_Владимир\n')
studentsList.append('Шигина_Марина\n')
studentsList.append('Ананков_Денис\n')
studentsList.append('Бурмистров_Фёдор\n')
studentsList.append('Галиханов_Сергей\n')
studentsList.append('Железнов_Илья\n')
studentsList.append('Козленко_Татьяна\n')
studentsList.append('Крыцин_Артём\n')
studentsList.append('Мамкин_Егор\n')
studentsList.append('Миронов_Максим\n')
studentsList.append('Рудой_Николай\n')
studentsList.append('Панкин_Сергей\n')
studentsList.append('Сенив_Дарья\n')
studentsList.append('Смирных_Олеся\n')
studentsList.append('Хлебалин_Никита\n')
studentsList.append('Суриков_Илья\n')
studentsList.append('Чуфирин_Валентин\n')
studentsList.append('Шматов_Артём\n')
studentsList.append('Юдаев_Владимир\n')
studentsList.append('Якушенков_Константин\n')

Preload()



name_counter = 0

global_a = []
global_a.append(5)
global_a.append(0)

CompareStrings(name_counter) 
if(global_a[1] != 0):   
    WriterXLSX()

workbook.save('Test_406_407_16_7sem.xlsx')
workbook.close()

print("Complete")


