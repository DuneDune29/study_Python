#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bicycle(): #클래스선언
    pass


# In[3]:


my_bicycle = Bicycle() #객체 생성


# In[4]:


my_bicycle


# In[5]:


my_bicycle.wheel_size = 26
my_bicycle.color = 'block'


# In[6]:


print("바퀴 크기:", my_bicycle.wheel_size) #객체의 속성 출력
print("색상:", my_bicycle.color)


# In[15]:


class Bicycle():
    
    def move(self, speed):
        print("자전거: 시속 {0}킬로미터 전진".format(speed))
        
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
        
    def stop(self):
        print("자전거({0},{1}): 정지".format(self.wheel_size, self.color))


# In[16]:


my_bicycle = Bicycle() #B클래스의 인스턴스인 my_b객체 생성

my_bicycle.wheel_size=26 #객체 속성 설정
my_bicycle.color = 'black'

my_bicycle.move(30) #객체의 메서드 호출
my_bicycle.turn('좌')
my_bicycle.stop()


# In[19]:


class Car():
    instance_count = 0 #클래스 변수 생성 및 초기화
    
    def __init__(self,size,color): #생성자(초기화) 함수
        self.size = size #인스턴스 변수 생성 및 초기화
        self.color = color #인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count + 1 #클래스 변수 이용
        print("자동차 객체의 수: {0}".format(Car.instance_count))
        
    def move(self):
        print("자동차({0} & {1})가 움직입니다.".format(self.size , self.color))


# In[23]:


car1 = Car('small','white')
car2 = Car('big','black')


# In[28]:


print("Car 클래스의 총 인스턴스 개수:{}".format(Car.instance_count))


# In[31]:


print("Car 클래스의 총 인스턴스 개수:{}".format(car1.instance_count))
print("Car 클래스의 총 인스턴스 개수:{}".format(car2.instance_count))


# In[32]:


class Car():
    instance_count = 0 #클래스 변수 생성 및 초기화
    
    def __init__(self,size,color): #생성자(초기화) 함수
        self.size = size #인스턴스 변수 생성 및 초기화
        self.color = color #인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count + 1 #클래스 변수 이용
        print("자동차 객체의 수: {0}".format(Car.instance_count))
        
    def move(self,speed):
        self.speed = speed #인스턴스 변수
        print("자동차({0} & {1})가 움직입니다.".format(self.size , self.color),end='')
        print("시속 {0} 킬로미터로 전진".format(self.speed))
        
    def auto_cruise(self):
        print("자율 주행 모드")
        self.move(self.speed) #move()함수의 인자로 인스턴스 변수를 입력
        
    #정적 메서드
    @staticmethod
    def check_type(model_code):
        if(model_code >= 20):
            print("이 자동차는 전기 차")
        elif(10 <= model_code <20):
            print("이 자동차는 가솔린 차")
        else:
            print("이 자동차는 디젤 차")


# In[33]:


Car.check_type(25)
Car.check_type(2)


# In[34]:


class Car():
    instance_count = 0 #클래스 변수 생성 및 초기화
    
    def __init__(self,size,color): #생성자(초기화) 함수
        self.size = size #인스턴스 변수 생성 및 초기화
        self.color = color #인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count + 1 #클래스 변수 이용
        print("자동차 객체의 수: {0}".format(Car.instance_count))
        
    def move(self,speed):
        self.speed = speed #인스턴스 변수
        print("자동차({0} & {1})가 움직입니다.".format(self.size , self.color),end='')
        print("시속 {0} 킬로미터로 전진".format(self.speed))
        
    def auto_cruise(self):
        print("자율 주행 모드")
        self.move(self.speed) #move()함수의 인자로 인스턴스 변수를 입력
    
    #클래스 메서드        
    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수: {0}".format(cls.instance_count))


# In[35]:


Car.count_instance() #객체 생성 전에 클래스 메서드 호출

car1 = Car("small","red") #객체 생성
Car.count_instance() #클래스 메서드 호출

car2 = Car("big","green") #객체 생성
Car.count_instance() #클래스 메서드 호출


# In[47]:


class Bicycle():
    
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color
        
    def move(self, speed):
        print("자전거: 시속 {0}km으로 전진".format(speed))
        
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
    
    def stop(self):
        print("자전거{0},{1}: 정지".format(self.wheel_size,self.color))


# In[48]:


class FoldingBicycle(Bicycle):

    def __init__(self, wheel_size, color, state): #폴딩B초기화
        Bicycle.__init__(self, wheel_size, color) #B초기화재사용
        #super().__init__(wheel_size, color) #super()도 사용가능
        self.state = state #자식 클래스에서 새로 추가한 변수
        
    def fold(self):
        self.state = 'folding'
        print("자전거: 접기, state={0}".format(self.state))

    def unfold(self):
        self.state = 'unfolding'
        print("자전거: 펴기, state={0}".format(self.state))


# In[50]:


folding_bicycle = FoldingBicycle(27, 'white', 'unfoloding') #객체생성

folding_bicycle.move(20) #부모 클래스의 함수메서드 호출
folding_bicycle.fold() #자식 클래스에서 정의한 함수 호출
folding_bicycle.unfold()


# In[ ]:




