#แบบฝึกหัดที่ 3.1
"""print("\tเลือกเมนูเพื่อทำรายการ")
print("#"*50)
print("\tกด 1 เลือกจ่ายเพิ่ม")
print("\tกด 2 เลือกเหมาจ่าย")

choose = int(input(" ")) #เลือกจ่ายเพิ่มหรือเหมาจ่าย
km = int(input("กรุณากรอกระยะทาง กิโลเมตร\n")) #กรอกระยะทาง
if choose == 1 : #เลือกแบบจ่ายเพิ่ม
    if km <= 25: #ถ้าไม่ถึง 25 km จ่าย 25 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท") 
    elif km > 25: #ถ้าเกิน 25 km จ่าย 25+55 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 80 บาท")
if choose == 2 : #เลือกแบบเหมาจ่าย
    if km <= 25: #ถ้าไม่เกิน 25 km จ่าย 25 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    elif km > 25: #ถ้าเกิน 25 km จ่าย 55 บาท
        print("ค่าใช้จ่ายรวมทั้งหมด 55 บาท")"""

#แบบฝึกหัดที่ 3.2
'''a1=int(input("กรุณากรอกจำนวนครั้งการรับค่า\n"))
a2 = 0
a3 = 1
while(a3 <= a1) :
    num = int(input("กรอกตัวเลข : "))
    a2 += num
    a3+=1
print("ผลรวมค่าที่รับมาทั้งหมด = %d"%a2)'''

#แบบฝึกหัด 3.3
"""print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exitเพื่อออกจากโปรแกรม")
a1 = []
i = 0
while(True) :
    i += 1
    food = input("อาหารโปรดอันดับที่ {} คือ \t".format(i))
    a1.append(food)
    if food == "exit" :
        break
print("อาหารสุดโปรดของคุณมีดังนี้ ",end= "")
for x in range(1,i):
        print(x,".",a1[x-1],end=" ")"""

#แบบฝึกหัด 3.4
a = []
while True :
    b = input('----ร้านคุณหลินบิวตี้----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b == 'a' : 
        c = input('ป้อนรายชื่อลูกค้า(รหัส : ชื่อ : จังหวัด)')
        a.append(c)
        print('\n*******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n')
    elif b == 's' : 
        print('{0:-<30}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a : 
            e = d.split(":")
            print('{0[0]:<6} {0[1]:<10}({0[2]:<10})'.format(e))
            continue
    elif b == 'x' : 
        c=input("ต้องการปิดโปรแกรมใช่หรือไม่ : ")
        if c =="ใช่":
            print("จบการทำงาน")
            break
        else : 
            continue

#แบบฝึกหัด3.5
'''student = int(input('please enter student :'))
print('-'*30)
total = [0 , 0 , 0 , 0 , 0 , 0]
score = ['90-100 :','80-89 :','70-79 :','60-69 :','50-59 : ','0-49 :']
x = 1
while x <= student :
    point = int(input('please enter score :'))
    if point <= 100 and point >= 90 :
        total[0] += 1
    elif point < 90 and point >= 80 :
        total[1] += 1
    elif point < 80 and point >= 70 :
        total[2] += 1
    elif point < 70 and point >= 60 :
        total[3] += 1
    elif point < 60 and point >= 50 :
        total[4] += 1
    elif point < 50 and point >= 0 :
        total[5] +=1
    x = x+1
for x in range(0,6) :
    print(score[x],'*'*total[x])'''