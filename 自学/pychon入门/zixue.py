from cProfile import label
from cmath import pi
import datetime
from email import message
from json.tool import main
import numbers
import re
import numpy as np
import pandas as pd
# a=datetime.datetime.now()
# print(type(a))
# print(a)
# print(id(a))
# print(8%2)
# print(12&8)
# print(123)
# nuim=['1','2','3','4','5','6']
# # print(type(nuim))
# # nui=[X for X  in nuim if X>4]
# # print(nui)
# # print(list(i+10 for i in nui))
# print(nuim[0:1].count('1'))

# # 正则表达式
# pattern=r'mr_\w+'
# string='MR_SHOP mr_shop'
# string1='项目名称MR_SHOP mr_shop'
#     # match()
# match=re.match(pattern,string,re.I)
# print(match)
# print('匹配值的起始位置为:',match.start())
# print('匹配值的结束位置为:',match.end())
# print('匹配位置的元组为:',match.span())
# print('匹配值的字符串:',match.string)
# print('匹配的数据为:',match.group())
# match=re.match(pattern,string1,re.I)
# print(match)
#     #search
# match=re.search(pattern,string,re.I)
# print(match)
# match=re.search(pattern,string1,re.I)
# print(match)
#     #findall
# match=re.findall(pattern,string,re.I)
# print(match)
# match=re.findall(pattern,string1) #re.I是否区分大小写
# print(match)
#     #findall查找
# pattern=r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
# string='127.0.0.1 192.0.0.168'
# match=re.findall(pattern,string)
# print(match)
#     #sub替换
# pattern=r'1[34578]\d{9}' #起始为13 or 14 or 15 or 17 or 18 ,再来9个随机数字
# string='中奖号码为:10088 联系电话为:18000000000'
# result=re.sub(pattern,'1XXXXXXXXXX',string)
# print(result)
#     #split分隔
# pattern=r'[?|&]'
# url='https://cn.bing.com/chrome/newtab?ensearch=1&FORM=BEHPTB'
# result=re.split(pattern,url)
# print(url)
# print(''.join(result))

# #异常概述
# def devision():
#     a=int(input("输入的数:"))
#     b=int(input("小朋友数量"))
#     c=a/b
#     assert a>b,'不够分'
#     return c

# if __name__ == '__main__':
#     try:
#         devision()
#     except ZeroDivisionError:
#         print("被除数为0")
#     except AssertionError as e:
#         print('输入有误',e)
#     else:
#         print('成功分配')
#     finally:
#         print('进行了一次分配')

# def filterchar(string):
#     import re
#     pattern=r'黑客|抓包|监听|Torjan'
#     sub=re.sub(pattern,'**',string)
#     print(sub)
# da=filterchar('我是一名黑客,喜欢抓包和监听,研究Torjan')


# #局部变量与全局变量
# message='路慢慢而修远兮'
# def qb():
#     message='吾将上下而求索'
#     print(message)
# print(message)
# qb()
# #使用global的局部变量
# message='路慢慢而修远兮'
# def qb():
#     global message
#     message='吾将上下而求索'
#     print(message)
# print(message)
# qb()
# print(message)

# import math
# def mianji(name,r):
#     print('名字为:'+name+'的圆面积为:'+str(math.pi*r*r))
# mianji('阿萨德',2)

# r=2;result=lambda r:math.pi*r*r;print(result(r))

# #实例属性
# class Geese:
#     '''大雁类'''
#     def __init__(self):
#         self.neck='脖子长'
#         self.wind='振翅频率高'
#         self.leg='腿位于身体的中心点'
#         print('大雁的特征为:')
#         print(self.neck)
#         print(self.wind)
#         print(self.leg)
# Geese()


# #类属性
# class Geese:
#     '''大雁类'''
#     neck='脖子长'
#     wind='振翅频率高'
#     leg='腿位于身体的中心点'
#     def __init__(self):
#         print('大雁的特征为:')
#         print(Geese.neck)
#         print(Geese.wind)
#         print(Geese.leg)
# Geese()

# #类属性转实例属性
# class Geese:
#     '''大雁类'''
#     neck='脖子长'
#     wind='振翅频率高'
#     leg='腿位于身体的中心点'
#     def __init__(self):
#         print('大雁的特征为:')
#         print(self.neck)
#         print(self.wind)
#         print(self.leg)
# Geese()

# #修改实例属性
# class Geese:
#     '''大雁类'''
#     def __init__(self) -> None:
#         self.neck='脖子长'
#         print(self.neck)
# ge1=Geese()
# ge2=Geese()
# ge1.neck='脖子不长'
# #输出实例属性
# print(ge1.neck)
# print(ge2.neck)


# class Geese:
#     '''大雁类'''
#     neck='脖子长'
#     def __init__(self) -> None:
#         self.neck='是什么'
#         print(Geese.neck)
# ge1=Geese()
# ge2=Geese()
# print(ge1.neck)#实例1属性
# print(Geese.neck)#类属性
# ge1.neck='脖子不长'#修改实例1属性
# print(ge2.neck)
# print(ge1.neck)#修改后的实例1属性
# Geese().neck='脖子长吗'#修改类属性
# print(ge1.neck)#修改后的实例1属性
# print(Geese.neck)#类属性
# print(ge2.neck)


# #保护属性
# class Swan:
#     '''天鹅类'''
#     _neck_swan='天鹅五跳天鹅舞'#定义类属性
#     def __init__(self) -> None:
#         print('__init__()',Swan._neck_swan)
# swan=Swan()
# print(swan._neck_swan)
# #一个下划线的保护属性,可以通过类名.属性调用,也可以通过实例.属性调用

# #私有属性
# class Swan:
#     '''天鹅类'''
#     __neck_swan='天鹅五跳天鹅舞'#定义类属性
#     def __init__(self) -> None:
#         print('__init__()', Swan.__neck_swan)
# swan=Swan()
# print(swan._Swan__neck_swan)
# print(swan._neck_swan)
# #私有属性可以通过【实例._类__属性】访问，还可以通过【类.属性】访问,不能直接通过【实例.属性】访问

# class Rect:
#     def __init__(self,width,height) -> None:
#         self.width=width
#         self.height=height
#     # @property      可以将方法转换为属性   即可以让area()方法变为area属性
#     def area(self):
#         return self.height*self.width
# rect=Rect(100,100)
# print(rect.area())



# class TVshow:
#     def __init__(self,show) -> None:
#         self.__show=show
#     @property
#     def show(self):
#         return self.__show
# tvshow=TVshow("正在播放《战狼2》")
# print(tvshow.show)
# #此时的show()方法变成了show属性,是只读不可写的
# tvshow.show="正在播放《红海行动》"
# print(tvshow.show)



# #类的继承                                                       封装
# class Fruit:                                #定义水果类
#     def __init__(self,color='绿色') -> None:
#         Fruit.color=color                   #定义类属性
#     def harvest(self):
#         print('水果是:'+Fruit.color+'的')


# class Apple(Fruit):
#     def __init__(self) -> None:
#         super().__init__()                  #继承基类的init
#         print('我是苹果')
# apple=Apple()
# apple.harvest()
# import bmi
# print(bmi.fun1_bmi('刘政江',174,68))

# print(dir())
# import sys
# print(sys.path)

# import chrismastree as chir
# chir.fun_chrismastree()
# if __name__ == '__main__':
#     chir.fun_chrismastree()
# print('='*50,'嗨嗨嗨','='*50)
# with open('message.txt','w') as file:
#     pass


# file1=open('message.txt','a')
# file1.write('黑发不知勤学早,白首方悔读书迟')
# file1.close()#关闭文件


# file1=open('message.txt','r')
# print(file1.read())
# file1.seek(10)#移动指针到新的位置,中文在seek占两个字符,所以此时在单数的时候报错。
# print(file1.read(3))#在这个指针上读取三个字符，在read里中英文和符号都占一个字符
# file1.close()
# # file1.read()#关闭文件后在此read报错[ValueError: I/O operation on closed file]
# with open('message.txt','r') as file:
#     print(file.read())
#     print(file.readline())
#     #with语句结束自动关闭文件
#     i=1
#     seek=0
#     while True:         #开始无条件循环
#         file.seek(seek)
#         word=file.read(i)
#         i+=1
#         if word[-1]=='书':
#             break       #跳出循环
#     print(word)


#os
# import os
# print(os.name)
# #nt表示window,posix是linux、Unix或MacOs
# print(os.sep)
# #当前系统所用的路径分隔符
# print(os.getcwd())#当前文件的路径
# print(os.listdir(os.getcwd()))#返回的指定目录下的文件和目录信息
#     # os.path
# print(os.path.exists('1.py'))#返回当前目录下 是否 存在1.py这个文件
# print(os.path.abspath('1.py'))#获取文件的绝对路径
# print(os.path.isdir(os.getcwd()))#判断是否为路径
# # os.mkdir('demo')#创建一个叫做demo的目录文件
# with open('..\pychon入门\message.txt'):
#     pass
# #在路径之前加上r或者R时可以不对路径分隔符“\”进行转义
# a=os.walk(os.getcwd())#遍历这个路径下的所有文件
# for i in a:
#     print(i)
# # os.makedirs('./demo1/aoligei')
# print(os.path.exists('./demo1/aoligei'))#判断是否存在路径

# if os.path.exists('./demo1/aoligei'):
#     os.rmdir('./demo1/aoligei')#删除目录使用rmdir       删除文件使用remove
#     print('删除成功')
# print(os.path.exists('./demo1/aoligei'))

# src='./demo1'
# dst='./demo2'
# # os.rename(src,dst)#重命名demo1为demo2
# if os.path.exists('./demo1'):
#     print('重命名失败')
# else:
#     print('重命名成功')

# print(os.stat('C:/'))




#创建wx.app子类
# import wx
# class App(wx.App):#继承父类wx.app
#     #初始化方法
#     def OnInit(self):
#         frame=wx.Frame(parent=None,title='Hello wxpython')#创建窗口
#         frame.Show()#显示窗口
#         return True #返回值
# app=App()
# app.MainLoop()#主循环方法


#直接使用wx.App
# app=wx.App()#初始化wx.App
# frame=wx.Frame(None,title='Hello wyPython')#定义了一个顶级窗口
# frame.Show()#显示窗口
# app.MainLoop()#调用wx.App类的MainLoop()主循环方法
#如果不适用MainLoop主循环方法，窗口则会一闪即逝


#创建wx.Frame的子类
# class MyFrame(wx.Frame):
#     def __init__(self, parents, id):
#         wx.Frame.__init__(self,parents,id,title="创建 Frame",pos=(100,100),size=(300,300))
# app=wx.App()
# frame=MyFrame(parents=None,id=-1)#实例化MyFrame类,并传递参数(parents=None为创建顶级窗口,id=-1为让wxpython自动生成id，一般都为-1)
# frame.Show()
# app.MainLoop() 


# 使用StaticText输出
# import wx
# 输出Python之禅
# class MyFrame(wx.Frame):
#     def __init__(self,parent,id):
#         wx.Frame.__init__(self,parent,id,title='创建StaticText类',pos=(100,100),size=(600,400))
#         panel=wx.Panel(self)    #创建画板
#         #创建标题,并设置字体
#         title=wx.StaticText(panel,label='Python 之禅————Tim Peters',pos=(100,20))
#         font=wx.Font(16,wx.FONTFAMILY_ROMAN,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
#         title.SetFont(font)
#         #创建文本
#         wx.StaticText(panel,label='优美胜与丑陋',pos=(50,50))
#         wx.StaticText(panel,label='明了胜于晦涩',pos=(50,70))
#         wx.StaticText(panel,label='简介胜于复杂',pos=(50,90))
#         wx.StaticText(panel,label='复杂胜于凌乱',pos=(50,110))
#         wx.StaticText(panel,label='扁平胜于嵌套',pos=(50,130))
#         wx.StaticText(panel,label='间隔胜于紧凑',pos=(50,150))
#         wx.StaticText(panel,label='可读性很重要',pos=(50,170))
#         wx.StaticText(panel,label='即便假借特例的实用性之名',pos=(50,190))
#         wx.StaticText(panel,label='不要包含素有错误,除非你确定需要这样做',pos=(50,210))
#         wx.StaticText(panel,label='当存在多种可能,不要尝试去猜测',pos=(50,230))
#         wx.StaticText(panel,label='而是尽量昭一中,最好是唯一一种明显的解决方案',pos=(50,250))
#         wx.StaticText(panel,label='虽然这并不容易,因为你不是PYthon之父',pos=(50,270))
#         wx.StaticText(panel,label='做也许好过不做,但不假思索就动手还不如不做',pos=(50,290))
#         wx.StaticText(panel,label='如果你无法相人描述你的方案,那肯定不是一个好方案;反之亦然',pos=(50,310))
#         wx.StaticText(panel,label='命名空间是一种绝妙的理念,我们应当多加利用',pos=(50,330))
# if __name__ == '__main__':
#     app=wx.App()
#     frame=MyFrame(parent=None,id=-1)
#     frame.Show()
#     app.MainLoop()


#TextCtrl类
# import wx
# #实现登录界面
# class MyFrame(wx.Frame):
#     def __init__(self,parent,id):
#         wx.Frame.__init__(self,parent,id,title='创建TextCtrl类',size=(400,300))
#         panel=wx.Panel(self)#创建面板、画板

#         self.title=wx.StaticText(panel,label='请输入用户名和密码',pos=(140,20))
#         self.label_user=wx.StaticText(panel,label='用户名:',pos=(50,50))
#         self.label_pwd=wx.StaticText(panel,label='密  码:',pos=(50,90))
#         self.text_user=wx.TextCtrl(panel,pos=(100,50),size=(235,25),style=wx.TE_LEFT)
#         self.text_password=wx.TextCtrl(panel,pos=(100,90),size=(235,25),style=wx.TE_PASSWORD)
# if __name__ == '__main__':
#     app=wx.App()
#     frame=MyFrame(parent=None,id=-1)
#     frame.Show()
#     app.MainLoop()


#BUTTON类
# import wx
# #为登录界面添加'确认'和'取消'按钮
# class MyFrame(wx.Frame):
#     def __init__(self,parent,id):
#         wx.Frame.__init__(self,parent,id,title='创建BUTTON类',size=(400,300))
#         panel=wx.Panel(self)
#         self.title=wx.StaticText(panel,label='请输入用户名和密码',pos=(140,20))
#         self.label_user=wx.StaticText(panel,label='用户名:',pos=(50,50))
#         self.label_pwd=wx.StaticText(panel,label='密  码:',pos=(50,90))
#         self.text_user=wx.TextCtrl(panel,pos=(100,50),size=(235,25),style=wx.TE_LEFT)
#         self.text_password=wx.TextCtrl(panel,pos=(100,90),size=(235,25),style=wx.TE_PASSWORD)
#         #创建确定和取消按钮
#         self.bt_confirm=wx.Button(panel,label='确定',pos=(125,130))
#         self.bt_cancle=wx.Button(panel,label='取消',pos=(215,130))
# if __name__ == '__main__':
#     app=wx.App()
#     frame=MyFrame(parent=None,id=-1)
#     frame.Show()
#     app.MainLoop()


#BoxSizer布局
# import wx
# #使用BoxSizer布局
# class MyFrame(wx.Frame):
#     def __init__(self,parent,id):
#         wx.Frame.__init__(self,parent,id,title='用户登录',size=(400,400))
#         #创建面板
#         panel=wx.Panel(self)
#         self.title=wx.StaticText(panel,label='请输入用户名和密码')
#         #添加容器,容器中控件按纵向排列
#         vsizer=wx.BoxSizer(wx.VERTICAL)
        # vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER)
#         panel.SetSizer(vsizer)
# if __name__ == '__main__':
#     app=wx.App()
#     frame=MyFrame(parent=None,id=-1)
#     frame.Show()
#     app.MainLoop()


#使用BoxSizer设置登录界面(不含事件)
# import wx
# class MyFrame(wx.Frame):
#     def __init__(self,parent,id):
#         wx.Frame.__init__(self,parent,id,title='登录界面',size=(400,300))
#         panel=wx.Panel(self)

#         #创建确定和取消按钮
#         self.bt_confirm=wx.Button(panel,label='确定')
#         self.bt_cancel=wx.Button(panel,label='取消')

#         #创建文本,左对齐
#         self.title=wx.StaticText(panel,label='请输入用户名和密码')
#         self.label_user=wx.StaticText(panel,label='用户名')
#         self.label_pwd=wx.StaticText(panel,label='密   码')
#         self.text_user=wx.TextCtrl(panel,style=wx.TE_LEFT)#用户名文本框
#         self.text_pwd=wx.TextCtrl(panel,style=wx.TE_PASSWORD)#密码文本框

#         #添加容器,容器横向布局
#         hsizer_user=wx.BoxSizer(wx.HORIZONTAL)#横向排列
#         hsizer_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
#         hsizer_user.Add(self.text_user,proportion=1,flag=wx.ALL,border=5)

#         #添加容器,容器横向布局
#         hsizer_pwd=wx.BoxSizer(wx.HORIZONTAL)
#         hsizer_pwd.Add(self.label_pwd,proportion=0,flag=wx.ALL,border=5)
#         hsizer_pwd.Add(self.text_pwd,proportion=1,flag=wx.ALL,border=5)

#         #添加容器,容器横向布局
#         hsizer_button=wx.BoxSizer(wx.HORIZONTAL)
#         hsizer_button.Add(self.bt_confirm,proportion=1,flag=wx.ALIGN_CENTER,border=5)
#         hsizer_button.Add(self.bt_cancel,proportion=1,flag=wx.ALIGN_CENTER,border=5)

#         #添加容器，容器纵向布局
#         vsizer_all=wx.BoxSizer(wx.VERTICAL)
#         vsizer_all.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
#         vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
#         vsizer_all.Add(hsizer_pwd,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
#         vsizer_all.Add(hsizer_button,proportion=0,flag=wx.ALIGN_CENTER|wx.TOP,border=15)
#         panel.SetSizer(vsizer_all)

# if __name__ == '__main__':
#     app=wx.App()
#     frame=MyFrame(parent=None,id=-1)
#     frame.Show()
#     app.MainLoop()



#在BoxSizer基础上添加事件
# import wx
# class MyFrame(wx.Frame):
#     def __init__(self,parent,id):
#         wx.Frame.__init__(self,parent,id,title='登录界面',size=(400,300))
#         panel=wx.Panel(self)

#         #创建确定和取消按钮,并绑定点击事件
#         self.bt_confirm=wx.Button(panel,label='确定')
#         self.bt_confirm.Bind(wx.EVT_BUTTON,self.qdclick)
#         self.bt_cancel=wx.Button(panel,label='取消')
#         self.bt_cancel.Bind(wx.EVT_BUTTON,self.qxclick)

#         #创建文本,左对齐
#         self.title=wx.StaticText(panel,label='请输入用户名和密码')
#         self.label_user=wx.StaticText(panel,label='用户名')
#         self.label_pwd=wx.StaticText(panel,label='密   码')
#         self.text_user=wx.TextCtrl(panel,style=wx.TE_LEFT)#用户名文本框
#         self.text_pwd=wx.TextCtrl(panel,style=wx.TE_PASSWORD)#密码文本框

#         #添加容器,容器横向布局
#         hsizer_user=wx.BoxSizer(wx.HORIZONTAL)#横向排列
#         hsizer_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
#         hsizer_user.Add(self.text_user,proportion=1,flag=wx.ALL,border=5)

#         #添加容器,容器横向布局
#         hsizer_pwd=wx.BoxSizer(wx.HORIZONTAL)
#         hsizer_pwd.Add(self.label_pwd,proportion=0,flag=wx.ALL,border=5)
#         hsizer_pwd.Add(self.text_pwd,proportion=1,flag=wx.ALL,border=5)

#         #添加容器,容器横向布局
#         hsizer_button=wx.BoxSizer(wx.HORIZONTAL)
#         hsizer_button.Add(self.bt_confirm,proportion=1,flag=wx.ALIGN_CENTER,border=5)
#         hsizer_button.Add(self.bt_cancel,proportion=1,flag=wx.ALIGN_CENTER,border=5)

#         #添加容器，容器纵向布局
#         vsizer_all=wx.BoxSizer(wx.VERTICAL)
#         vsizer_all.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
#         vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
#         vsizer_all.Add(hsizer_pwd,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
#         vsizer_all.Add(hsizer_button,proportion=0,flag=wx.ALIGN_CENTER|wx.TOP,border=15)
#         panel.SetSizer(vsizer_all)

#         # 添加事件
#     def qdclick(self,event):#确定按钮事件
#         '''单击确定按钮,执行方法'''
#         message=""
#         username=self.text_user.GetValue()#获取用户名文本框输入的数值
#         password=self.text_pwd.GetValue()#获取密码文本框输入的数值
#         if username=="" or password=="":
#             message='用户名或密码不能为空'
#         elif username=='mr' and password=='mrsoft':
#             message='登录成功'
#         else:
#             message='用户名或密码不正确'
#         wx.MessageBox(message)#弹出提示框MessageBox
    
#     def qxclick(self,event):#取消按钮事件
#         '''单机取消按钮,执行方法'''
#         self.text_user.SetValue("")#清空用户名框文本
#         self.text_pwd.SetValue("")#清空密码框文本

# if __name__ == '__main__':
#     app=wx.App()
#     frame=MyFrame(parent=None,id=-1)
#     frame.Show()
#     app.MainLoop()



#PYQT框架的使用
