class Student():
    #定义四个属性
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score

    #定义输出方法
    def info(self):
        print(f'Name:{self.name},Age:{self.age},gender:{self.gender},score:{self.score}')

for i in range(1,6):
    lst=(input(f'请输入第{i}个学生的信息：').split('#'))
    exec(f'stu_{i}=Student(lst[0],lst[1],lst[2],lst[3])')  #exec函数会把字符串变成一句代码并执行

for i in range(1, 6):
    locals()[f'stu_{i}'].info()


