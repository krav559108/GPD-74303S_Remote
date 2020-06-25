import re
import time
import sys
import os
import serial
from itertools import repeat
import tkinter as tk
from tkinter import filedialog


# #из основной программы
#
os.system('cls' if os.name == 'nt' else 'clear')
os.path.abspath(__file__)
# #
COM_port_q = int(input("Укажите номер COM Port к которому подключен прибор: "))
COM_port = 'COM{com_number}'.format(com_number = COM_port_q)

ser = serial.Serial(port = COM_port, baudrate = 9600, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, timeout = 0.3)
try:
    ser.isOpen()
    ser.write(b'*IDN?\n')
    ser.write(b'OUT0\n')
    time.sleep(0.2)
    ser.write(b'TRACK0\n')
    time.sleep(0.2)

    print('COM открыт\nПроверьте что устройство не находится в локальном режиме')
except:
    print('\nОшибка открытия порта')

    exit()
#
root = tk.Tk()
root.withdraw()
# file_name = input('Введите название файла: ')
# file = open(file_name, "r")
file1 = filedialog.askopenfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
file = open(file1, "r")



pattern = re.compile("ch=+(\d+(.)\d|\d+|\w\w\w\w|)+,out=+(\d+(.)\d|\d+|\w\w\w\w|)+,u1=+(\d+(.)\d|\d+|\w\w\w\w|)+,u2=+(\d+(.)\d|\d+|\w\w\w\w|)+,i1=+(\d+(.)\d|\d+|\w\w\w\w|)+,i2=+(\d+(.)\d|\d+|\w\w\w\w|)+,step=+(\d+(.)\d|\d+|\w\w\w\w|)+,tstep=+(\d+(.)\d|\d+|\w\w\w\w|)+,pause=+(\d+(.)\d|\d+|\w\w\w\w|)+;")


while(True):
    if re.match(pattern, file.readline()):
        print("line is correct")
    else:
        #print("line is not correct")
        #file.close()
        break
file.seek(0)
time.sleep(0.5)


n_times = int(input('Количество повторений программы: '))
print("Программа будет выполнена " + str(n_times) + " раз.")

for _ in repeat(None, n_times):


    while(True):
        #search_pattern = re.compile('=(\d|\d|\w\w\w\w)')
        search_pattern = re.compile('=(\d+(.)\d|\d+|\w\w\w\w|)')

        v = search_pattern.findall(file.readline())
        if v:
            #print(v)
            # print("ch = "+ v[0][0])
            # print("out = "+ v[1][0])
            # print("u1 = "+ v[2][0])
            # print("u2 = "+ v[3][0])
            # print("i1 = "+ v[4][0])
            # print("i2 = "+ v[5][0])
            # print("step = "+ v[6][0])
            # print("tstep = "+ v[7][0])
            # print("pause = "+ v[8][0])

            # Данные забираются из строк успешно

            ch=v[0][0]
            out=v[1][0]
            u1=v[2][0]
            u2=v[3][0]
            i1=v[4][0]
            i2=v[5][0]
            step=v[6][0]
            tstep=v[7][0]
            pause=v[8][0]

            if ch == 'none':
                time.sleep(0)
            else:
                ch_converted = int(ch)

            if out == 'none' and out == '0':
                ser.write(b'OUT0\n')
                time.sleep(0.2)
            else:
                ser.write(b'OUT1\n')
                time.sleep(0.2)

            if u1 == 'none':
                time.sleep(0)
            else:
                u1_converted = float(u1)

            if u2 == 'none':
                time.sleep(0)
            else:
                u2_converted = float(u2)

            if i1 == 'none':
                time.sleep(0)
            else:
                i1_converted = float(i1)

            if i2 == 'none':
                time.sleep(0)
            else:
                i2_converted = float(i2)

            if step == 'none':
                time.sleep(0)
            else:
                step_converted = float(step)

            if tstep == 'none':
                time.sleep(0)
            else:
                tstep_converted = float(tstep)

            if u2 == 'none' and i2 == 'none':
                a = ('VSET{ch}:{v}'.format(v = u1_converted, ch = ch_converted).upper().encode() + b'\n')
                b = ('ISET{ch}:{i}'.format(i = i1_converted, ch = ch_converted).upper().encode() + b'\n')
                ser.write(a)
                time.sleep(0.1)
                ser.write(b)
                time.sleep(0.1)
            else:
                if i2 == 'none':
                    ser.write(b'TRACK0\n')
                    time.sleep(0.2)

                    while (u1_converted < u2_converted):
                        u_start = ('VSET{ch}:{v}'.format(v = u1_converted, ch = ch_converted).upper().encode() + b'\n')
                        u1_converted = u1_converted + step_converted
                        time.sleep(tstep_converted)
                        ser.write(u_start)
                    time.sleep(0.2)
                    while (u1_converted > u2_converted):
                        u_start = ('VSET{ch}:{v}'.format(v = u1_converted, ch = ch_converted).upper().encode() + b'\n')
                        u1_converted = u1_converted - step_converted
                        time.sleep(tstep_converted)
                        ser.write(u_start)
                    time.sleep(0.2)
                elif u2 == 'none':
                    ser.write(b'TRACK0\n')
                    time.sleep(0.2)
                    while (i1_converted < i2_converted):
                        i_start = ('VSET{ch}:{i}'.format(i = i1_converted, ch = ch_converted).upper().encode() + b'\n')
                        i1_converted = i1_converted + step_converted
                        time.sleep(tstep_converted)
                        ser.write(i_start)
                    time.sleep(0.2)
                    while (i1_converted > i2_converted):
                        i_start = ('VSET{ch}:{i}'.format(i = i1_converted, ch = ch_converted).upper().encode() + b'\n')
                        i1_converted = i1_converted - step_converted
                        time.sleep(tstep_converted)
                        ser.write(i_start)
                    time.sleep(0.2)
                else:
                    time.sleep(0)


            if pause == 'none':
                time.sleep(0)
            else:
                time.sleep(float(pause))
    #always turn output OFF before next step
            # ser.write(b'OUT0\n')
            # time.sleep(0.2)

        else:
            time.sleep(0)
            file.seek(0)
            ser.write(b'OUT0\n')
            time.sleep(0.2)
            #print('Программа выполнена № раз')
            # ser.write(b'OUT0\n')
            # time.sleep(0.2)
            # sys.exit(0)
            # ser.close()
            break
        print('Программа выполнена успешно')
