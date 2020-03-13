#여러 문장 작성
x='''
안녕하세요
제 나이는
'''

x=4 #숫자
y="4" #문자
print(str(x)+y)
print(x+int(y))

#함수, 조건문
def sayhello(name,age):
    if age<10:
        print("안녕, "+name)
    elif 10<=age<=20:
        print("안녕하세요, "+name)
    else:
        print("안녕하십니까, "+name)
sayhello("승연",22)

#반복문(for, while)
for i in range(3):
    print(i)
    print("철수 : 안녕 영희야")
    print("영희 : 안녕 철수")
int i=0
while i != 10: #i가 '(조건)일 동안'으로 해석
    print(i)
    print("철수 : 안녕 영희야")
    print("영희 : 안녕 철수")
    i +=1
i=0
while True:
    print(i)
    print("철수 : 영희 뭐해?")
    print("영희 : 그냥 있어.")
    i+=1
    if i>2:
        break
for i in range(100):
    print(i)
    print("철수 : 영희 뭐해?")
    print("영희 : 그냥 있어.")
    i+=1
    if i>2:
        break
#continu -> continue 밑의 문장은 실행되지 않고 처음으로 돌아감
#특정한 조건에서 특정 코드를 실행시키고 싶지 않을 때 continue
for i in range(3):
    print(i)
    print("철수 : 안녕 영희")
    print("영희 : 안녕 철수")
    if i==1:
        continue
    print("승연 : 안녕 철수, 영희")

###<자료구조>_리스트, 튜플, 딕셔너리
    
##_리스트(elementary 여러개 그루핑)
x=list() #리스트
y=[] #리스트

x=[1, 2, 3, 4, 5]
y=["python", "java"]
z=["python", 1, 2, 3]

print(x+y)

x[3]=10 #값 수정 4->10 (mutable)수정가능

num_elements=len(x) #리스트 길이
y=sorted(x)
z=sum(x)
print(x.index(2)) #원소'2'가 x의 몇 번째 자리에 있는지->1
print(y.index("java")
print("Hello" in y) #'Hello' 가 y에 있는지 -> False / True
if 10 in x:
      print("10이 x에 있어요")

for n in x: #x의 원소 리스트 순서대로 출력
    print(n)

for c in y:
    print(c)

##_튜플
x=tuple() #튜플
y=() #튜플

x=(1, 2, 3)
y=('a', 'b', 'c')
z=(1, "python", "java")

print(x+y)

# x[0]=10 ->error. 튜플은 엘레멘터리 수정 불가(immutable)

print(z.index(1))
print('a' in y)

##_딕셔너리 ('key'와 'value'로 구성)
x=dict() #딕셔너리
y={} #딕셔너리

x={'name':"승연", "age":20}

print(x["name"]) #x딕셔너리의 'name'이라는key value값
# key값으로 가능한 것 : 불변값(ex) 문자열, 숫자) -> 리스트는 가변(mutable)이기에 key가 될 수 없음

print("age" in x) #key값만 가능, "승연"->False

print(x.keys())
print(x.values())

for key in x:
      print(key) # key값 출력
      print(x[key]) # value값 출력

for key in x:
      print("key: " + str(key))
      print("value: " + str(x[key]))

x["name"]="워니" # key값 변환이 아닌 해당 key의 value값 변환

x["school"]="학교" #새로운 key, value 추가

#example
fruit=["사과","사과","바나나","바나나","딸기","키위","복숭아","복숭아","복숭아"]
d={}

for f in fruit:
      if f in d: #"사과"라는 key가 d라는 딕셔너리에 있는지
      d[f]=d[f]+1 # 있으면 "사과"key의 value값 +1
      else:
          d[f]=1 # 없으면 딕셔너리에 넣고 value 1로 설정

###<클래스, 오브젝트>(클래스:함수+변수), (오브젝트(인스턴스):클래스를 이용해 생성한 것) 

class Person:
    def say_hello(self):
        print("안녕!")
saram = Person()
saram.say_hello()

class Person:
    name="승연"
    def say_hello(self):
        print("안녕! 나는 " + self.name)# 만들어진 오브젝트에 변수를 활용해야 할 때 self 이용        
saram + Person()
saram.say_hello()

class Person: # 이름 바꾸는 기능 추가
    def __init__(self, name):
        self.name=name
    def say_hello(self):
        print("안녕! 나는 "+self.name)
seungyeon=Person("승연")
seungyeon.say_hello()

class Person: #인사 받는 사람의 변수 추가
    def __init__(self, name):
        self.name=name # init ->self를 첫 인자로 받고, Person에서 새로 사용할 변수를 설정
    def say_hello(self, to_name):
        print("안녕! :" + to_name + " 나는 " + self.name)
seungyon=Person("승연")
seungyeon.say_hello("철수")

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def say_hello(self, to_name):
        print("안녕! :" + to_name + "나는" + self.name)
    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

seungyeon = Person("승연",22)
seungyeon.introduce()

##상속 (공통된 클래스를 가지고있고 추가적인 세부 클래스를 만들고 싶을 경우)

class Police(Person): # Police라는 클래스가 Person이라는 클래스를 상속
    def arrest(self, to_arrest):
        print("넌 체포됐다, "+to_arrest)
class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아! 이걸 만들어야겠다: "+to_program)
seungyeon = Person("승연",22)
seungyeon = Programmer("승연",22) # Person을 상속받았기 때문에 Person의 함수 이용 가능
seugyeon.program("이메일 클라이언트")

