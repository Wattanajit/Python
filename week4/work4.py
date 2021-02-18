'''import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.Open Calculator\n 2.Open Notepad\n 3.Open edge\n 4.Exit')
    choice = input('Select Menu :')


def opennotepad(): 
    filename = 'C:\\Windows\\SysWOW64\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\SysWOW64\\calc.exe'
    print('Calculate Number %s' %filename) 
    os. system(filename) 

def openmsedge():
    filename = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    print('Open msedge %s' %filename) 
    os. system(filename) 

while True: 
    menu()
    if choice == '1': 
        opencalculator() 
    elif choice == '2': 
        opennotepad()
    elif choice == '3':
        openmsedge()
    else: 
        break'''

#แบบฝึกหัด4.1
'''import os
choice = 0
listcoffee = [0,0,0,0,0,]
pick = 0
def menu():
    global choice
    print('\tโปรแกรมร้านค้ากาแฟ\n','-'*50,'\n','1.แสดงรายการสินค้า\n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม\n')
    choice = input('กรุณาเลือกทำรายการ : ')
    ###screen_clear()

def showmenu(): 
    print('\t[1]รายการสินค้ากาแฟ\n','-'*50)
    print('\t1.เอสเปรสโซ 55 บาท\n','\t2.คาปูชิโน 60 บาท\n','\t3.ลาเต้ 65 บาท\n','\t4.ชาเขียว 55 บาท\n','\t5.ชามะนาว 50 บาท')

def pickmenu():
    global pick
    print('\t[2]รายการสินค้า\n','-'*50,'\n','\t1.เอสเปรสโซ\n \t2.คาปูชิโน\n \t3.ลาเต้\n \t4.ชาเขียว\n \t5.ชามะนาว\n','-'*50)
    pick = int(input('เลือกหยิบสินค้าหมายเลข :'))
    if pick == 1:
        listcoffee[0] += 1
    elif pick == 2:
        listcoffee[1] += 1
    elif pick == 3:
        listcoffee[2] += 1
    elif pick == 4:
        listcoffee[3] += 1
    elif pick == 5:
        listcoffee[4] += 1
    screen_clear()

def showuserpick():
    print('[3]สินค้าที่คุณได้หยิบไปมีดังนี้\n')
    list_score = ['เอสเปรสโซ','คาปูชิโน','ลาเต้','ชาเขียว','ชามะนาว']
    list_price = [55,60,65,55,50]
    print('{0:-<13}{1:-<13}{2:-<13}{3}'.format('สินค้า','ราคา','จำนวน','ราคารวม'))
    for i in range(0,5):
        print('{0:-<13}{1:-<13}{2:-<13}{3}'.format(list_score[i],list_price[i],listcoffee[i],listcoffee[i]*list_price[i]))

def deletuserpick():
    print('\t\n[4]รายการสินค้า\n 1.เอสเปรสโซ\n 2.คาปูชิโน\n 3.ลาเต้\n 4.ชาเขียว\n 5.ชามะนาว')
    depick = int(input('เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก '))
    if depick == 1:
        listcoffee[0] -= 1
    elif depick == 2:
        listcoffee[1] -= 1
    elif depick == 3:
        listcoffee[2] -= 1
    elif depick == 4:
        listcoffee[3] -= 1
    elif depick == 5:
        listcoffee[4] -= 1

def screen_clear():
    clearscreen = os.system('cls')

while True:
    menu()
    if choice == '1':
        screen_clear()
        showmenu()
    elif choice == '2':
        screen_clear()
        pickmenu()
    elif choice == '3':
        screen_clear()
        showuserpick()
    elif choice == '4':
        deletuserpick()
        screen_clear()
    elif choice == '5':
        c = input('[5]ต้องการใช้โปรแกรมต่อหรือไม่ y/n: ')
        if c.lower() == 'y':
            screen_clear()
        elif c.lower() == 'n':
            screen_clear()
            break'''

#แบบฝึกหัด 4.2
'''import os
word_dictionary = {}
def menu():
    global choice
    print("-"*40+'\nพจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์ทั้งหมด\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n'+"-"*40)
    choice = input('Input Choice : ')
def adddict():
    word = input("\nเพิ่มคำศัพท์ :\t")
    typeword = input("ชนิดของคำ(n. , v. , adj. , adv.): ")
    mean = input("ความหมาย :  ")
    word_dictionary[word] = typeword,mean
    print("เพิ่มคำศัพท์เรียบร้อยแล้ว ")
def showdict():
    print("\n\tคำศัพท์ทั้งหมด\n{0: <11}{1: <8}{2}".format('คำศัพท์','ประเภท','ความหมาย'))
    for key in word_dictionary:
        print("{}{:<3}{}".format(key,'',word_dictionary[key]))
def deletee():
    delete_word = input("\nพิมพ์คำศัพท์ที่ต้องการลบ: ")
    yes_no = input("ต้องการลบ {} ใช่หรือไม่ (y/n): ".format(delete_word))
    if yes_no == 'y':
        del word_dictionary[delete_word]
        print("ลบ "+delete_word+" เรียบร้อยแล้ว")
while True:
    menu()
    if choice == '1':
        adddict()
    elif choice =='2':
        showdict()
    elif choice =='3':
        deletee()
    elif choice =='4':
        c = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
        if c.lower() == 'y':
            os.system('cls')
        elif c.lower() == 'n':
            os.system('cls')
            break'''

#แบบฝึกหัด 4.3
import datetime
name,pts,time,hit=[],[],[],[]
num =int(input('Enter number of Competitor     : '))
for i in range(num):
    print(i+1,'of Comprtitor')
    regname =input('Name of Competitor             : ')
    regpts =int(input('Enter your PTS                 : '))
    regtime =float(input('Enter your time                : '))
    name.insert(i,regname),pts.insert(i,regpts),time.insert(i,regtime),hit.insert(i,regpts/regtime)
for i in range(num):
    j = i
    for j in range(num):
        if pts[i] > pts[j]:
            a,b,c,d = hit[i],name[i],pts[i],time[i]
            hit[i],name[i],pts[i],time[i]=hit[j],name[j],pts[j],time[j]
            hit[j],name[j],pts[j],time[j]=a,b,c,d
date = datetime.datetime.now()
datenew = date.strftime('%G-%m-%d %H:%M:%S')
print('\nShotgun',date.strftime('%A'),'Training',date.strftime('%Y'))
print(datenew)
print('-'*110+'\n{0:-<15}{1:-<15}{2:-<15}{3:-<20}{4:-<15}{5:-<15}{6:-<15}'.format('No.','PTS','TIME','COMPETITOR','HIT FACTOR','STATE POINTS','STATE PERCENT\n'+'-'*110))
for i in range(num):
    print('{0: <15}{1: <15}{2: <15}{3: <20}{4: <15}{5: <15}{6: <1}'.format(i+1,pts[i],time[i],name[i],'%.4f'%hit[i],'%.4f'%float(hit[i]/hit[0]*50),'%.4f'%float((hit[i]/hit[0]*50)/(hit[0]/hit[0]*50)*100)))