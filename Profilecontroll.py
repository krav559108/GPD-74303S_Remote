file = open("Cmdline.txt", "r")

commandline = []

for line in file:
    splitline = line.split(",")
    commandline.append(splitline[0])


#for ch_n in commandline[0]:
#    split_ch_n = ch_n.split("=")
#    split_ch_n.append(split_ch_n[0])
#Получил номер канала


for ai in commandline:
    print(ai)
#    if ai == 'ch={ch}'.format(ch = ch_n):
#        print("Канал №" + ch_n)
#    else:
#        print("WTF")
#while (True):
if line in commandline == 'ch={ch}'.format(ch = ch_n):
    print(ch_n)




#print(commandline)
print(ch_n)
file.close()
