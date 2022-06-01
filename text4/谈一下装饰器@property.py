# -*- coding: utf-8 -*-
"""
装饰器@property
"""
class Test(object):
    
    #含有装饰器
    @property
    def use_property(self):
        print('带有装饰器')
    #不含装饰器
    def no_property(self): 
        print('不含装饰器')
        
#实例化Test类
model = Test()
#加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
model.use_property
#没有加@property , 必须使用正常的调用方法的形式，即在后面加()
model.no_property()



class Test(object):
    def __init__(self):
        #定义属性
        self._name = '李华'
        self._age = 18 
    #方法加入@property后，这个方法相当于一个属性，
    #这个属性可以让用户进行使用，而且用户有没办法随意修改。
    @property
    def name(self): 
        return self._name 
    @property
    def age(self):
        return self._age
model = Test()
#用户进行属性调用的时候，直接调用name即可，而不用知道属性名_name
#因此用户无法更改属性，从而保护了类的属性。
print(model.name)
print(model.age)


















































