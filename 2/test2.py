'''a1 = input("Input First Number : \n")
a2 = input("Input Second Number : \n")
print(a1,"==",a2, ":",a1==a2)
print(a1,">",a2,":",a1>a2)
print(a1,"<",a2,":",a1<a2)'''

'''a = 60
b = 13
c = 0

c = a & b
print(c)

c = a | b
print(c)

c = ~a
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)'''

'''d1 = int (input(" Day Converter Program \n Input number fo Days --> "))
print(d1,"Day --> Hour",24*d1,"Hours")
print(d1,"Day --> Minutes",60*24*d1,"Minutes")
print(d1,"Day --> Seconds",60*60*24*d1,"Seconds")'''

'''animal ={"cat","dog","rat","pig","ant"}
animal.add("mokey")
animal.update(["python","capibara","spider","wombat","penguin","crocodile"])
print(animal)'''

print("โปรแกรมหยิบสินค้าใส่ตะกร้า")
a1 = []
for x in range(1,6):
    food = input("หยิบสินค้าชิ้นที่ %d : "%x)
    a1.append(food)
print("สินค้าที่หยิบใส่ตะกร้ามีดังนี้")
print("1.",a1[0])
print("2.",a1[1])
print("3.",a1[2])
print("4.",a1[3])
print("5.",a1[4])

'''print("\tโปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์")
print("-"*50)
print("\tรถยนต์ 4 ล้อ กด 1")
print("\tรถยนต์ 6 ล้อ กด 2")
print("\tรถยนต์มากกว่า 6 ล้อ กด 3")
car4_list = ["ลาดกระบัง-->บางบ่อ : 25 บาท","ลาดกระบัง-->บางประกง : 30 บาท","ลาดกระบัง-->พนัสนิคม : 45 บาท","ลาดกระบัง-->บ้านบึง : 55 บาท","ลาดกระบัง-->บางพระ : 60 บาท"]
car6_list = ["ลาดกระบัง-->บางบ่อ : 40 บาท","ลาดกระบัง-->บางประกง : 45 บาท","ลาดกระบัง-->พนัสนิคม : 75 บาท","ลาดกระบัง-->บ้านบึง : 90 บาท","ลาดกระบัง-->บางพระ : 100 บาท"]
car8_list = ["ลาดกระบัง-->บางบ่อ : 60 บาท","ลาดกระบัง-->บางประกง : 70 บาท","ลาดกระบัง-->พนัสนิคม : 110 บาท","ลาดกระบัง-->บ้านบึง : 130 บาท","ลาดกระบัง-->บางพระ : 140 บาท"]
car = int(input("\tเลือกประเภทยานพาหนะ : """))
if car == 1:
    print("\tค่าบริการรถยนต์ 4 ล้อ")
    for x in car4_list:
        print("\n",x)
elif car == 2:
    print("\tค่าบริการรถยนต์ 6 ล้อ")
    for x in car6_list:
        print("\n",x)
elif car == 3:
    print("\tค่าบริการรถยนต์ 6 ล้อขึ้นไป")
    for x in car8_list:
        print("\n",x)'''