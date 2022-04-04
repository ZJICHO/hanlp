from json.tool import main
from lib2to3.pgen2.grammar import opmap_raw


pinetree='我是一颗松树'
def fun_chrismastree():
    '''
    功能:一个梦
    无返回值
    '''
    pinetree='挂上彩灯、礼物'
    print(pinetree)
    if __name__ == '__main__':
        print('\n下雪了······\n')
        print('--开始函数--')
        # fun_chrismastree()
        print('--结束函数--')
        pinetree='我是一颗槐树:'+pinetree
        print(pinetree)
if __name__ == '__main__':
    fun_chrismastree()
