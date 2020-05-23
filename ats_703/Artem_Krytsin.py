import os
import json
import codecs
import subprocess

#Крыцин Артём
#-----------------------------------------------------------------------------------
#начальная конфигурация
gcc = "gcc"

gcc_path = "C:/MinGW/bin/gcc.exe"
gcc_command = "%s *.c *.h" % gcc_path

gpp_path = "C:/MinGW/bin/g++.exe"
gpp_command = "%s *.c *.h" % gpp_path

msbuild_path = "C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/msbuild.exe"
msbuild_command = "msbuild"
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
#достаем Ф.И. всех заданий из json файла
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
        compiler_check = 0
        each_exercise_folder_path = student_directory + "\\" + exercises_folder[loc_e]
        exercise_directory_tree = os.walk(each_exercise_folder_path)
        for loc_g in each_exercise_folder_path:
            exercise_folder.append(loc_g)
        for address, dirs, files in student_folder:
            for file in files:
                base, file_extension = os.path.splitext(file)
                if(base == 'main'):
                    file_parser(loc_i, file, each_exercise_folder_path)
                #переменная compiler_check:
                #1-msbuild
                #2-g++
                if(file_extension == '.sln'):
                    compiler_check += 1

        curr_path = os.getcwd()
        os.chdir(each_exercise_folder_path)

        #вызов компилятора с++ (вставить switch)
        if(compiler_check != 0):
            process = subprocess.Popen(msbuild_command)
        else:
            process = subprocess.Popen(gpp_command)

        returncode = process.wait()
        print(returncode)
        os.chdir(curr_path)