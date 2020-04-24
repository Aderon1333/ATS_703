def Preload():
    worksheet["A1"] =  'Студент'
    worksheet["B1"] =  'Группа'
    worksheet["C1"] =  'Задание'
    worksheet["D1"] =  'Результат тестирования'

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
    temp_cell = 'C'
    temp_cell = temp_cell + str(global_a[1])
    worksheet[temp_cell] =  result[2]
    temp_cell = 'D'
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

result = []
result.append('Апидова_Анастас\n')
result.append('406\n')
result.append('1_1\n')
result.append('Fail\n')
result.append('1 - Fail\n2 - Fail\n3 - Pass\n4 - Pass\n5 - Fail\n')

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