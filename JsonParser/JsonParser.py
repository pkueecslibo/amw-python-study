#-*-coding:iso-8859-1-*-
#!/usr/bin/python

'''

'''

class JsonParser:
    def __init__(self):
        self.dict = {}

    def load(self, s):
        '''
        读取json格式数据，输入s为一个json字符串，无返回值
        若遇到格式错误的应该抛出异常，json中数字如果超出了python里的浮点数上限的，也可以抛出异常
        所有字符串（键和值）转化为python中的unicode类型字符串，特别注意转义符的转化
        为简便考虑，json的最外层假定只为 object
        '''
        print s, len(s)
        s = s.strip()
        s = s[1:len(s)-1]
        print s
        kv = s.split(',')
        print 'kv:', kv, len(kv)
        pass

    def dump(self):
        '''
        根据类中数据返回json字符串
        '''
        pass

    def loadJson(self, f):
        '''
        从文件中读入json格式数据，f为文件路径，格式错误抛出异常
        '''
        pass

    def dumpJson(self, f):
        '''
        将类中的内容以json格式存入文件中，文件若存在则覆盖，文件操作失败抛出异常
        '''
        pass

    def loadDict(self, d):
        '''
        读取dict中的数据，存入类中，若遇到不是字符串的key则忽略
        '''
        pass

    def dumpDict(self):
        '''
        返回一个字典
        '''
        pass

if __name__ == '__main__':
    print 'main'
    a = JsonParser()
    a.load(open('test.json').read())
