def fun1_bmi(person,height,weight):
    '''
    功能:根据身高和体重计算BMI指数
    person:姓名
    height:身高
    weight:体重
    '''
    print(person+'的身高为:'+str(height)+'cm'+',体重为:'+str(weight)+'kg')
    bmi=weight/(height**2)
    print(person+'的BMI指数为:'+str(bmi))

def path():
    return path