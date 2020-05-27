import serial
import hashlib
import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')
os.path.abspath(__file__)

ser = serial.Serial(port = 'COM3', baudrate = 9600, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, timeout = 0.3)
try:
    ser.isOpen()
    ser.write(b'*IDN?\n')
    ser.write(b'OUT0\n')
    time.sleep(0.2)
    ser.write(b'TRACK0\n')
    time.sleep(0.2)

    print('COM port is open\nCheck that your device not in local mode')
except:
    print('\nError open port')

    exit()

class Menu():
    mode = "0"
    while mode == "0":
        print("\n1 - Set Voltage and Current for 1 specific chanel in Track Mode\n")
        print("\n2 - Test specific chanel with the step from chosen values of V and I\n")
        print("\n3 - Set Voltage and Current for parallel 1st and 2nd chanel\n")
        print("\n4 - Enter Local Mode\n")


        mode = input("\nChoose Mode: ")

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

                ch_1 = int(input('Choose output chanel: '))

                a = ('VSET{ch}:{v}'.format(v = float(input('Enter Voltage value: ')), ch = ch_1).upper().encode() + b'\n')
                b = ('ISET{ch}:{i}'.format(i = float(input('Enter Current value: ')), ch = ch_1).upper().encode() + b'\n')
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
                    print("\n1 - Variable Voltage and Stable Current\n")
                    print("\n2 - Variable Current and Stable Voltage\n")



                    mode1 = input("\nChoose Mode: ")
                    if mode1 == "1":

                        class Step_setup_var_voltage():
                            ch_1 = int(input('Choose output chanel: '))
                            v1 = float(input('Enter starting Voltage value: '))
                            v2 = float(input('Enter ending Voltage value: '))
                            i1 = float(input('Enter Current value: '))
                            step_value = float(input('Enter Step value: '))

                            c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                            d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                            ser.write(b'TRACK0\n')
                            time.sleep(0.2)
                            ser.write(b'OUT1\n')
                            time.sleep(0.2)

                            n = (v2 - v1) / step_value


                            while (v1 <= v2):

                                v_start = ('VSET{ch}:{v}'.format(v = v1, ch = ch_1).upper().encode() + b'\n')
                                v1 = v1 + step_value
                                time.sleep(0.1)
                                ser.write(v_start)

                            time.sleep(0.2)
                            ser.write(c)
                            time.sleep(0.1)
                            ser.write(d)
                            time.sleep(0.1)


                    elif mode1 == "2":

                        class Step_setup_var_current():
                            ch_1 = int(input('Choose output chanel: '))
                            i1 = float(input('Enter starting Current value: '))
                            i2 = float(input('Enter ending Current value: '))
                            v1 = float(input('Enter Voltage value: '))
                            step_value = float(input('Enter Step value: '))

                            c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                            d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                            ser.write(b'TRACK0\n')
                            time.sleep(0.2)
                            ser.write(b'OUT1\n')
                            time.sleep(0.2)

                            n = (i2 - i1) / step_value


                            while (i1 <= i2):

                                i_start = ('ISET{ch}:{i}'.format(i = i1, ch = ch_1).upper().encode() + b'\n')
                                i1 = i1 + step_value
                                time.sleep(0.1)
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
                        print("\n1 - Variable Voltage and Stable Current on Parallel 1 and 2 chanels\n")
                        print("\n2 - Variable Current and Stable Voltage on Parallel 1 and 2 chanels\n")



                        mode1 = input("\nChoose Mode: ")
                        if mode1 == "1":

                            class Step_setup_var_voltage():
                                ch_1 = int(1)
                                v1 = float(input('Enter starting Voltage value: '))
                                v2 = float(input('Enter ending Voltage value: '))
                                i1 = float(input('Enter Current value: '))
                                step_value = float(input('Enter Step value: '))

                                c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                                d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                                ser.write(b'TRACK2\n')
                                time.sleep(0.2)
                                ser.write(b'OUT1\n')
                                time.sleep(0.2)

                                n = (v2 - v1) / step_value


                                while (v1 <= v2):

                                    v_start = ('VSET{ch}:{v}'.format(v = v1, ch = ch_1).upper().encode() + b'\n')
                                    v1 = v1 + step_value
                                    time.sleep(0.1)
                                    ser.write(v_start)

                                time.sleep(0.2)
                                ser.write(c)
                                time.sleep(0.1)
                                ser.write(d)
                                time.sleep(0.1)


                        elif mode1 == "2":

                            class Step_setup_var_current():
                                ch_1 = int(1)
                                i1 = float(input('Enter starting Current value: '))
                                i2 = float(input('Enter ending Current value: '))
                                v1 = float(input('Enter Voltage value: '))
                                step_value = float(input('Enter Step value: '))

                                c = ('VSET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')
                                d = ('ISET{ch}?'.format(ch = ch_1).upper().encode() + b'\n')

                                ser.write(b'TRACK2\n')
                                time.sleep(0.2)
                                ser.write(b'OUT1\n')
                                time.sleep(0.2)

                                n = (i2 - i1) / step_value


                                while (i1 <= i2):

                                    i_start = ('ISET{ch}:{i}'.format(i = i1, ch = ch_1).upper().encode() + b'\n')
                                    i1 = i1 + step_value
                                    time.sleep(0.1)
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
            print("\nLocal Mode is active. Exiting.")
            sys.exit(0)
            ser.close()


        else:
            print("\nWrong Input\n")

while(True):
    shutdown = input("\nDo you want to TURN OFF THE OUTPUT?? [y/n] > ")
    if shutdown == "y":
        print('\nShuting down the output!\n')
        ser.write(b'OUT0\n')
        time.sleep(0.2)
    elif shutdown == "n":
        print('\nOUTPUT IS ACTIVE!Type [y] to turn OFF! > ')
    else:
        print('\nShuting down the output!')
        ser.write(b'OUT0\n')
        time.sleep(0.2)
    break



#try:
while(True):
    data = ser.read(size=500000).decode('utf-8').rstrip('\r\n')
    print (data)
    restart = input("\nDo you want to restart the program? [y/n] > ")

    if restart == "y":
         print('\nRestarting\n')
         ser.write(b'OUT0\n')
         time.sleep(0.2)
         ser.close()
         os.system('python "test.py"')
    else:
        print("\nThe programm will be closed shortly\n")
        ser.write(b'OUT0\n')
        time.sleep(0.2)
        sys.exit(0)
        ser.close()


    #ser.close()
#except Exception:

#    print('\n''exiting')
