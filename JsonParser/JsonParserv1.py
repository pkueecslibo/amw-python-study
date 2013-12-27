#-*-coding:utf-8-*-
#!/usr/bin/python

'''
JSON    Python
object  dict
array   list
string  unicode
number (int)    int, long
number (real)   float
true    True
false   False
null    None

'''

ESCAPE_TAB = {
        u'"': u'\\"',
        u'\\': u'\\\\',
        u'/': u'\\/',
        u'\b': u'\\b',
        u'\f': u'\\f',
        u'\n': u'\\n',
        u'\r': u'\\r',
        u'\t': u'\\t',
        }

STRIP_TAB = [u' ', u'\r', u'\n']


def print_caller(func):
    def func_wrap(*args, **kwargs):
        print '\033[1;31;40m'
        print '===> %s' % func.func_name
        print '\033[0m'
        return func(*args, **kwargs)
    return func_wrap;

@print_caller
def parse_string(s, pos):
    '''
    匹配一个string s必须以‘"’开始
    返回匹配的字符串和与起始'"'匹配的后一位
    '''
    print type(s)

    while s[pos] in STRIP_TAB:
        pos += 1

    assert s[pos] == u'"'

    result = []
    esc = False

    pos += 1
    while True:
        print pos
        if esc == False and s[pos] == u'"':
            break
        if s[pos] == u'\\':
            esc  =True
        elif esc == True and s[pos] in ESCAPE_TAB.keys():
            result.append(ESCAPE_TAB[s[pos]])
            esc = False
        else:
            result.append(s[pos])
        pos += 1
    return ''.join(result), pos+1

def parse_int(s, pos):
    '''
    匹配一个int s必须以‘{’开始
    '''
    pass

def parse_float(s, pos):
    '''
    匹配一个float s必须以‘{’开始
    '''
    pass

@print_caller
def parse_key(s, pos):

    val, pos = parse_scan(s, pos)

    return val, pos

@print_caller
def parse_val(s, pos):

    val, pos = parse_scan(s, pos)
    return val, pos

@print_caller
def parse_object(s, pos):
    '''
    匹配一个dict s必须以‘{’开始
    '''

    while s[pos] in STRIP_TAB:
        pos += 1

    assert s[pos] == u'{'

    d = {}
    pos += 1

    while True:
        key, pos = parse_key(s, pos)
        print key, pos

        #除掉':'号
        while s[pos] != u':':
            pos += 1
        pos += 1

        val, pos = parse_val(s, pos)
        print val, pos

        d[key] = val

        while s[pos] in STRIP_TAB:
            pos += 1

        if s[pos] == u',':
            pos += 1

        while s[pos] in STRIP_TAB:
            pos += 1

        print u'======================== (%s)' % s[pos]

        if s[pos] == u'}':
            break
    return d, pos+1




def parse_item(s, pos):
    pass

def parse_array(s, pos):
    '''
    匹配一个array s必须以‘[’开始
    '''

    assert s[pos] == u'['
    pos += 1

    result = []
    while True:
        while s[pos] in STRIP_TAB:
            pos += 1
        val, pos = parse_scan(s, pos)
        result.append(val)

        while s[pos] in STRIP_TAB:
            pos += 1
        if s[pos] == u',':
            pos += 1
        if s[pos] == u']':
            break
    return result, pos + 1


def parse_number(s, pos):
    neg = False

    while s[pos] in STRIP_TAB:
        pos += 1

    if s[pos] == u'-':
        neg = True
        pos += 1
    if s[pos] == u'+':
        neg = False
        pos += 1

    result = 0
    #整数部分
    while s[pos] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        result *= 10
        result += eval(s[pos])
        pos += 1

    #小数点
    if s[pos] == u'.':
        pos += 1
        result = float(result)

    if neg:
        result = -result

    base = -1
    while s[pos] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        tmp = eval(s[pos]) * (10 ** base)
        result += tmp
        base -= 1
        pos += 1

    if s[pos] in [u'e', u'E']:
        pos += 1
        exp_val = 0
        exp_neg = False
        if s[pos] == u'+':
            exp_neg = False
            pos += 1
        elif s[pos] == u'-':
            exp_neg = True
            pos += 1

        while s[pos] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            exp_val *= 10
            exp_val += eval(s[pos])
            pos += 1
        if exp_neg:
            exp_val = -exp
        result = base * (10 ** exp_val)

    return result, pos+1








@print_caller
def parse_scan(s, pos):
    pass

    while s[pos] in STRIP_TAB:
        pos += 1

    print u'第一个字符:(%s)' % s[pos]

    if s[pos] == u'"':
        return parse_string(s, pos)
    elif s[pos] == u'[':
        return parse_array(s, pos)
    elif s[pos] == u'{':
        return parse_object(s, pos)
    elif s[pos] == u'f' and s.startswith('false', pos,pos+5):
        return False, pos + 5
    elif s[pos] == u't' and s.startswith('true', pos,pos+4):
        return True, pos + 4
    else:
        pass
    print '可能是数字'
    return parse_number(s, pos)


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
        s = s.decode('utf-8')
        self.dict, pos  = parse_object(s, 0)
        print self.dict

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
    a.load(open('test3.json').read())
