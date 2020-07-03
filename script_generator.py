import re
import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')
os.path.abspath(__file__)

text = input('Введите имя файла, не указывая формат. Используйте ENG расскладку: ') + '.txt'
f = open(text, "x")
f.close()

#ch=1,out=1,u1=5.3,u2=none,i1=2,i2=none,step=none,tstep=none,pause=none;
print('\nДанная программа предназначена для создания цикла (скрипта) без посвещения себя в правила оформления файла с форматом .txt \n')
print('При заполнении параметров соблюдайте правила оформления. \n1 - Дробные значения уазываются через < . >. \n2 - Все значения времени указываются в секундах\n')

def string_content():
    ch = input('Введите номер канала: ')
    out = input('Выберите состояние выхода (1 - вкл; 0 или none - выкл): ')
    u1 = input('Введите начальное значение напряжения: ')
    u2 = input('Введите конечное значение напряжения или < none > если не нужно изменение напряжение: ')
    i1 = input('Введите начальное значение тока: ')
    i2 = input('Введите конечное значение тока или < none > если не нужно изменение напряжение: ')
    step = input('Введите интервал изменения тока или напряжения: ')
    tstep = input('Введите время интервалов (указывается в секундах): ')
    pause = input('Введите время паузы в конце цикла (указывается в секундах): ')

    script_file = open(text, "a")
    script_file.write("ch={ch_n},out={out_cond},u1={u1_val},u2={u2_val},i1={i1_val},i2={i2_val},step={step_val},tstep={tstep_val},pause={pause_val};".format(ch_n = ch, out_cond = out, u1_val = u1, u2_val = u2, i1_val = i1, i2_val = i2, step_val = step, tstep_val = tstep, pause_val = pause) + '\n')
    #script_file.close()

# choise = input('Введите < STOP > для прекращения цикла и любое другое для продолжения')

while(True):
    choise = input('Введите < STOP > для прекращения цикла и любое другое или нажмите ВВОД для продолжения: ')
    if choise != 'STOP':
        string_content()
    else:
        print('Внесение данных выполнено')
        sys.exit(0)