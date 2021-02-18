#แบบฝึกหัด 5.1
'''class nisit :
    def __init__(self,name,surname,year,branch,sex) : 
        self.name = name
        self.surname = surname
        self.year = year
        self.branch = branch
        self.sex = sex

    def shownisit(self) :
        print('Nisit properties')
        print('name : ',self.name)
        print('surname : ',self.surname)
        print('year : ',self.year)
        print('branch : ',self.branch)
        print('sex : ',self.sex)

x = nisit('Wattanajit','Jitsabai','1','Computer Education','mule')
x.shownisit()'''

#แบบฝึกหัด 5.1
class nisit:
    def __init__(self,name,province,year,department,sex):
        self.name = name
        self.province = province
        self.year = year
        self.department = department
        self.sex = sex

    def show(self):
        if self.sex == 'ชาย':
            print('สวัสดีครับ ผมชื่อ '+self.name +' มาจากจังหวัด'+self.province+' เพศ'+self.sex+ ' นักศึกษาชั้นปีที่ '+self.year + ' สาขา '+self.department)
        elif self.sex == 'หญิง':
            print('สวัสดีค่ะ ฉันชื่อ'+self.name +' มาจากจังหวัด'+self.province+' เพศ'+self.sex+ ' นักศึกษาชั้นปีที่ '+self.year + ' สาขา '+self.department)
        else:
            print('ERROR!')

    @classmethod
    def info(self):
        print('-'*15,'แนะนำตัว','-'*15)
        #print('ชื่อ-สกุล:เพศ:ชั้นปี:สาขาวิชา:')
        name = input('ชื่อ : ')
        province = input('จังหวัด : ')
        year = input('ชั้นปี : ')
        department = input('สาขา : ')
        sex = input('เพศ : ')
        return self(name,province,year,department,sex)

x = nisit.info()
x.show()