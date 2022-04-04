# from pyhanlp import *
# print(HanLP. segment('你好,欢迎在Bvthon中调用HanLP的API'))
# for term in HanLP.segment('下雨天地面积水'):
#     print('{}\t{}'.format(term.word,term.nature))#获取单词与词性
# testCases=["商品和服务",
# "结婚的和尚未结婚的确实在干扰分词啊",
# "买水果然后来世博园最后去世博会",
# "中国的首都是北京",
# "欢迎新老师生前来就餐",
# "工信处女千事每月经过下属科室都要亲口交代24 口交换机等技术性器件的安装工作",
# "随着页游兴起到现在的页游繁盛,依赖于存档进行逻辑判断的设计减少了,但这块也不能完全忽略掉。"]
# for sentence in testCases:print(HanLP.segment (sentence))
# # 关键词提取
# document='水利部水资源司司长陈明忠 9 月29日在国务院新闻办举行的新闻发布会上透露,\
# 根据刚刚完成了水资源管理制度的考核,有部分省接近了红线的指标,"\
# "有部分省超过红线的指标。对一些超过红线的地方,陈明忠表示,对一些取用水项目进行\
# 区域的限批,'
# "严格地进行水资源论证和取水许可的批准。"
# print(HanLP. extractKeyword (document, 2))
# #自动摘要
# print (HanLP. extractSummary (document, 3))
# #依存句法分析
# print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))






from pyhanlp import *
#加载词典
# def load_dictionary():
IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
#     path=HanLP.Config.CoreDictionaryPath.replace('.txt','.mini.txt')
#     dic=IOUtil.loadDictionary([path])
#     return set(dic.keySet())





# # # #单词链表
# # # def fully_segment(text,dic):
# # #     word_list=[]
# # #     for i in range(len(text)):
# # #         for j in range(i +1 ,len(text)+1):
# # #             word=text[i:j]
# # #             if word in dic:
# # #                 word_list.append(word)
# # #     return word_list

# # dic=load_dictionary()
# # # print(dic)
# # # print(fully_segment('商品和服务',dic))

# # #正向最长匹配
# # def forward_segment(text,dic):
# #     word_list=[]
# #     i=0
# #     while i <len(text):
# #         logest_word=text[i]
# #         for j in range(i+1,len(text)+1):
# #             word=text[i:j]
# #             if word in dic:
# #                 if len(word)>len(logest_word):
# #                     logest_word=word
# #         if len(logest_word)!=1:
# #             word_list.append(logest_word)
# #         i=i+len(logest_word)

# #     return word_list
# # # print(forward_segment('商品和服务',dic))

# # #逆向最长匹配
# # def backward_segment(text,dic):
# #     word_list=[]
# #     i=len(text)-1
# #     while i>=0:
# #         logest_word=text[i]
# #         for j in range(0,i):
# #             word=text[j:i+1]
# #             if word in dic:
# #                 if len(word)>len(logest_word):
# #                     logest_word=word
# #         word_list.insert(0,logest_word)
# #         i-=len(logest_word)
# #     return word_list
# # # print(backward_segment('商品和服务',dic))

# # def count_single_char(word_list:list):#统计单字成词的个数
# #     return sum(1 for item in word_list if len(item)==2)
# # word_list=['商品', '和', '服务']
# # # print(count_single_char(word_list))
# # def bidirectional_segment(text,dic):
# #     f =forward_segment(text,dic)
# #     b = backward_segment(text,dic)
# #     if len(f) < len(b): #词数更少优先级更高
# #         return f
# #     elif len(f) > len(b):
# #         return b
# #     else:
# #         if count_single_char(f) < count_single_char(b):#单字更少优先级更高
# #             return f
# #         else:
# #             return b

# # # print(bidirectional_segment('单字更少优先级更高',dic))

# # from time import *
# # start_time=time()
# # # print('%.1f'%(80/time()))
# # # print('%0.1f'%(start_time))
# # print(time())#时间戳




# 构建字典树的节点
class Node(object):
    def __init__(self,value) -> None:
        self._children={}
        self._value=value
        print(self._value)

    def _add_child(self,char,value,overwrite=False):
        child=self._children.get(char)#在_children里查找char(key)对应的value
        if child is None:             #未找到这个value，为none
            child=Node(value)         #child设置为给定的value
            self._children[char]=child#在_children这个列表里设置key为char,value为child(给定的value)
        elif overwrite:               #如果此时的overwrite为True
            child._value=value        #设置child._value=value给定的value
        return child



#构建字典树
class Trie(Node):
    def __init__(self) -> None:
        super().__init__(None)              #继承基类的init

    def __contains__(self, key):
        return self[key] is not None         #暂时不知道啥用

    def __getitem__(self, key):              #改和查和删
        state = self                         #设置state为self,获取self的所有方法
        for char in key:                     #如果key里的char存在_children里,设置state为这个char的value
            state = state._children.get(char)
            if state is None:                #如果存在char但是value=none(不存在),state为value
                return  None
        return state._value                  #输出这个节点的value

    def __setitem__(self, key, value):       #增
        state=self
        for i ,char in enumerate(key):       #设置
            if i<len(key)-1:
                state=state._add_child(char, None,False)
                print(i,char,key,len(key),value)
            else:
                state=state._add_child(char, value,True)
                print(i,char,len(key))
if __name__ == '__main__':
    trie = Trie()
    # 增
    trie['自然'] = 'nature'
    trie['自然人'] = 'human'
    trie['自然语言'] = 'language'
    trie['自语'] = 'talkto oneself'
    trie['入门'] = 'introduction'
    assert '自然' in trie
    # 删
    trie['自然'] = None
    assert '自然' not in trie
    # 改
    trie['自然语言'] = 'human language'
    assert trie['自然语言'] == 'human language'
    # 查
    assert trie['入门'] == 'introduction'
    pass