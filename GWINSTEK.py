import serial
import hashlib
import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')
os.path.abspath(__file__)

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

class Main_menu():
    mode = "0"
    while mode == "0":
        print("\n1 - Ручной режим управления\n")
        print("\n2 - Ввод даных из файла сценария\n")

        mode = input("\nВыберите режим: ")

        if mode == "1":

            class Menu():
                mode = "0"
                while mode == "0":
                    print("\n1 - Установка напряжения и тока на определенном канале (Track Mode)\n")
                    print("\n2 - Тестирование определенного канала с указаным шагом\n")
                    print("\n3 - Установка напряжения и тока на 1ом и 2ом канале в паралельном режиме\n")
                    print("\n4 - Вход в локальный режим\n")


                    mode = input("\nВыберите режим: ")

                    if mode == "1":

                        class Gen_msg():

                            #a = ('VSET{ch}:{v}'.format(v=V_value.V, ch = CH_num.CH).upper().encode() + b'\n')
                            #b = ('ISET{ch}:{i}'.format(i=I_value.I, ch = CH_num.CH).upper().encode() + b'\n')
                            #print(a)
                            #print(b)

                            #Profile_all

                            #from profiles import Profile_all

                            #a = ('VSET{ch}:{v}'.format(v=Profile_all.V1, ch = Profile_all.CH1).upper().encode() + b'\n')
                            #b = ('ISET{ch}:{i}'.format(i=Profile_all.I1, ch = Profile_all.CH1).upper().encode() + b'\n')

                            #Input msgs

                            ch_1 = int(input('Выберите выходной канал: '))

                            a = ('VSET{ch}:{v}'.format(v = float(input('Введите напряжение: ')), ch = ch_1).upper().encode() + b'\n')
                            b = ('ISET{ch}:{i}'.format(i = float(input('Введите ток: ')), ch = ch_1).upper().encode() + b'\n')
                            c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                            d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                            ser.write(b'TRACK0\n')
                            time.sleep(0.2)
                            ser.write(b'OUT1\n')
                            time.sleep(0.2)
                            ser.write(a)
                            time.sleep(0.1)
                            ser.write(b)
                            time.sleep(0.1)
                            ser.write(c)
                            time.sleep(0.1)
                            ser.write(d)
                            time.sleep(0.1)


                    elif mode == "2":

                        class second_menu():
                            mode1 = "0"
                            while mode1 == "0":
                                print("\n1 - Изменяемое напряжение и стабильный ток\n")
                                print("\n2 - Изменяемый ток и стабильное напряжение\n")



                                mode1 = input("\nВыберите режим: ")
                                if mode1 == "1":

                                    class Step_setup_var_voltage():
                                        ch_1 = int(input('Выберите выходной канал: '))
                                        v1 = float(input('Введите начальное значение напряжения: '))
                                        v2 = float(input('Введите конечное значение напряжения: '))
                                        i1 = float(input('Введите значение тока: '))
                                        step_value = float(input('Введите интервал изменения: '))
                                        t = float(input('Введите время интервалов: '))

                                        c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                                        d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                                        ser.write(b'TRACK0\n')
                                        time.sleep(0.2)
                                        ser.write(b'OUT1\n')
                                        time.sleep(0.2)

                                        n = abs(v2 - v1) / step_value
                                        time_left = n * t
                                        print('Тест займет ' + str(time_left) + ' секунд.')
                                        while (v1 < v2):

                                            v_start = ('VSET{ch}:{v}'.format(v = v1, ch = ch_1).upper().encode() + b'\n')
                                            v1 = v1 + step_value
                                            time.sleep(t)
                                            ser.write(v_start)

                                        while (v1 > v2):

                                            v_start = ('VSET{ch}:{v}'.format(v = v1, ch = ch_1).upper().encode() + b'\n')
                                            v1 = v1 - step_value
                                            time.sleep(t)
                                            ser.write(v_start)

                                        time.sleep(0.2)
                                        ser.write(c)
                                        time.sleep(0.1)
                                        ser.write(d)
                                        time.sleep(0.1)



                                elif mode1 == "2":

                                    class Step_setup_var_current():
                                        ch_1 = int(input('Выберите выходной канал: '))
                                        i1 = float(input('Введите начальное значение тока: '))
                                        i2 = float(input('Введите конечное значение тока: '))
                                        v1 = float(input('Введите значение напряжения: '))
                                        step_value = float(input('Введите интервал изменения: '))
                                        t = float(input('Введите время интервалов: '))

                                        c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                                        d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                                        ser.write(b'TRACK0\n')
                                        time.sleep(0.2)
                                        ser.write(b'OUT1\n')
                                        time.sleep(0.2)

                                        n = abs(i2 - i1) / step_value
                                        time_left = n * t
                                        print('Тест займет ' + str(time_left) + ' секунд.')


                                        while (i1 < i2):

                                            i_start = ('ISET{ch}:{i}'.format(i = i1, ch = ch_1).upper().encode() + b'\n')
                                            i1 = i1 + step_value
                                            time.sleep(t)
                                            ser.write(i_start)

                                        while (i1 > i2):

                                            i_start = ('VSET{ch}:{i}'.format(i = i1, ch = ch_1).upper().encode() + b'\n')
                                            i1 = i1 - step_value
                                            time.sleep(t)
                                            ser.write(i_start)

                                        time.sleep(0.2)
                                        ser.write(c)
                                        time.sleep(0.1)
                                        ser.write(d)
                                        time.sleep(0.1)




                    elif mode == "3":

                        class Parallel_setup():
                            class second_menu():
                                mode1 = "0"
                                while mode1 == "0":
                                    print("\n1 - Изменяемое значение напряжения и стабильный ток на паралельных 1 и 2 канале\n")
                                    print("\n2 - Изменяемое значение тока и стабильное напряжение на паралельных 1 и 2 канале\n")



                                    mode1 = input("\nВыберите режим: ")
                                    if mode1 == "1":

                                        class Step_setup_var_voltage():
                                            ch_1 = int(1)
                                            v1 = float(input('Введите начальное значение напряжения: '))
                                            v2 = float(input('Введите конечное значение напряжения: '))
                                            i1 = float(input('Введите значение тока: '))
                                            step_value = float(input('Введите интервал изменения: '))
                                            t = float(input('Введите время интервалов: '))

                                            c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                                            d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                                            ser.write(b'TRACK2\n')
                                            time.sleep(0.2)
                                            ser.write(b'OUT1\n')
                                            time.sleep(0.2)

                                            n = abs(v2 - v1) / step_value
                                            time_left = n * t
                                            print('Тест займет ' + str(time_left) + ' секунд.')

                                            while (v1 < v2):

                                                v_start = ('VSET{ch}:{v}'.format(v = v1, ch = ch_1).upper().encode() + b'\n')
                                                v1 = v1 + step_value
                                                time.sleep(t)
                                                ser.write(v_start)

                                            while (v1 > v2):

                                                v_start = ('VSET{ch}:{v}'.format(v = v1, ch = ch_1).upper().encode() + b'\n')
                                                v1 = v1 - step_value
                                                time.sleep(t)
                                                ser.write(v_start)

                                            time.sleep(0.2)
                                            ser.write(c)
                                            time.sleep(0.1)
                                            ser.write(d)
                                            time.sleep(0.1)


                                    elif mode1 == "2":

                                        class Step_setup_var_current():
                                            ch_1 = int(1)
                                            i1 = float(input('Введите начальное значение тока: '))
                                            i2 = float(input('Введите конечное значение тока: '))
                                            v1 = float(input('Введите значение напряжения: '))
                                            step_value = float(input('Введите интервал изменения: '))
                                            t = float(input('Введите время интервалов: '))

                                            c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                                            d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                                            ser.write(b'TRACK2\n')
                                            time.sleep(0.2)
                                            ser.write(b'OUT1\n')
                                            time.sleep(0.2)

                                            n = abs(i2 - i1) / step_value
                                            time_left = n * t
                                            print('Тест займет ' + str(time_left) + ' секунд.')

                                            while (i1 < i2):

                                                i_start = ('ISET{ch}:{i}'.format(i = i1, ch = ch_1).upper().encode() + b'\n')
                                                i1 = i1 + step_value
                                                time.sleep(t)
                                                ser.write(i_start)

                                            while (i1 > i2):

                                                i_start = ('VSET{ch}:{i}'.format(i = i1, ch = ch_1).upper().encode() + b'\n')
                                                i1 = i1 - step_value
                                                time.sleep(t)
                                                ser.write(i_start)

                                            time.sleep(0.2)
                                            ser.write(c)
                                            time.sleep(0.1)
                                            ser.write(d)
                                            time.sleep(0.1)

                    elif mode == "4":
                        ser.write(b'OUT0\n')
                        time.sleep(0.2)
                        ser.write(b'LOCAL\n')
                        time.sleep(0.2)
                        print("\nЛокальный режим активирован. Выход из программы.")
                        sys.exit(0)
                        ser.close()


                    else:
                        print("\nНе правильный формат вводных данных\n")

        if mode == "2":
            ser.close()
            time.sleep(0.2)
            os.system('python "cmd_controll.py"')













while(True):
    shutdown = input("\nВы точно хотите ВЫКЛЮЧИТЬ ВЫХОД?? [y/n] > ")
    if shutdown == "y":
        print('\nВЫХОД выключен!\n')
        ser.write(b'OUT0\n')
        time.sleep(0.2)
    elif shutdown == "n":
        print('\nВЫХОД АКТИВЕН!')
    else:
        print('\nВЫХОД выключен!')
        ser.write(b'OUT0\n')
        time.sleep(0.2)
    break



#try:
while(True):
    #data = ser.read(size=500000).decode('utf-8').rstrip('\r\n')
    #print (data)
    restart = input("\nХотите ли вы перезапустить программу? [y/n] > ")

    if restart == "y":
         print('Перезапускаю\n')
         ser.write(b'OUT0\n')
         time.sleep(0.2)
         ser.close()
         os.system('python "GWINSTEK.py"')
    else:
        print("\nПрограмма скоро закроется\n")
        ser.write(b'OUT0\n')
        time.sleep(0.2)
        sys.exit(0)
        ser.close()
    break

    #ser.close()
#except Exception:

#    print('\n''exiting')
