#-*-coding:utf-8-*-
#!/usr/bin/python

import simplejson as json

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

STRIP_TAB = [u' ', u'\t', u'\r', u'\n']

CLRF = u'\r\n'

##############################################################
'''
工具函数
'''

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def disable():
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''

def infog( msg):
    print OKGREEN + msg + ENDC

def info( msg):
    print OKBLUE + msg + ENDC

def warn( msg):
    print WARNING + msg + ENDC

def err( msg):
    print FAIL + msg + ENDC

def print_caller(func):
    def func_wrap(*args, **kwargs):
        infog('===> %s' % func.func_name)
        return func(*args, **kwargs)
    return func_wrap;

##############################################################
'''
主要的解析函数
'''

_lineno = 0

def _skip_blank(s, pos):
    try:
        while s[pos] in STRIP_TAB:
            _meet_clrf(s, pos)
            pos += 1
    except IndexError:
        raise JsonEndInvalidException(u'字符')
    return pos

def _meet_clrf(s, pos):
    global _lineno
    if s.startswith(CLRF, pos, pos+2):
        _lineno += 1
        info(u'行号: %s' % _lineno)


def _is_digit(s, pos):
    if s[pos] >= u'0' and s[pos] <= u'9':
        return True
    return False


@print_caller
def parse_string(s, pos):
    '''
    匹配一个string s必须以‘"’开始
    返回匹配的字符串和与起始'"'匹配的后一位
    '''
    #跳过空白
    pos = _skip_blank(s, pos)

    assert s[pos] == u'"'

    result = []
    esc = False

    try:
        pos += 1
        while True:
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
    except IndexError:
        raise JsonEndInvalidException()
    return ''.join(result), pos+1

def parse_int(s, pos):
    '''
    匹配一个int
    '''
    pass

def parse_float(s, pos):
    '''
    匹配一个float
    '''
    pass

@print_caller
def parse_key(s, pos):
    '''
    匹配字典项的键
    '''
    val, pos = parse_scan(s, pos)

    return val, pos

@print_caller
def parse_val(s, pos):
    '''
    匹配字典项的值
    '''
    val, pos = parse_scan(s, pos)
    return val, pos

@print_caller
def parse_object(s, pos):
    '''
    匹配一个dict s必须以‘{’开始
    '''

    #除掉空白
    pos = _skip_blank(s, pos)

    assert s[pos] == u'{'

    d = {}
    pos += 1

    while True:
        key, pos = parse_key(s, pos)
        info(u'\tkey: %s' % key)

        #除掉空白
        pos = _skip_blank(s, pos)
        #必须是':'号
        if s[pos] != u':':
            raise JsonUnexpectCharException(u':', s[pos]);
        pos += 1    #跳过':'

        val, pos = parse_val(s, pos)
        info(u'\tval: %s' % (val))

        d[key] = val    #加入字典
        print d

        #跳过空白
        pos = _skip_blank(s, pos)

        #如果出现的',', 说明还有键值对
        if s[pos] == u',':
            pos += 1
        else:
            #意味着字典结束，下一个字符必须是'}'
            if s[pos] != u'}':
                raise JsonUnexpectCharException(u'}', s[pos])

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
    #跳过空白
    pos = _skip_blank(s, pos)
    assert s[pos] == u'['
    pos += 1

    result = []
    while True:
        #跳过空白
        pos = _skip_blank(s, pos)

        val, pos = parse_scan(s, pos)
        info('\tval: %s' % val)
        result.append(val)

        pos = _skip_blank(s, pos)
        if s[pos] == u',':
            pos += 1
        if s[pos] == u']':
            break
    return result, pos + 1


def parse_number(s, pos):
    '''
    匹配一个数字串
    '''
    neg = False

    pos = _skip_blank(s, pos)

    if s[pos] == u'-':
        neg = True
        pos += 1
    if s[pos] == u'+':
        neg = False
        pos += 1

    result = 0
    #整数部分
    while _is_digit(s, pos):
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
    while _is_digit(s, pos):
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

        while _is_digit(s, pos):
            exp_val *= 10
            exp_val += eval(s[pos])
            pos += 1
        if exp_neg:
            exp_val = -exp
        result = base * (10 ** exp_val)
    return result, pos

@print_caller
def parse_scan(s, pos):
    #跳过空白
    pos = _skip_blank(s, pos)

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
    elif s[pos] == u'n' and s.startswith('null', pos, pos + 4):
        return None, pos + 4
    else:
        pass

    if _is_digit(s, pos) or s[pos] in [u'-', u'+']:
        print '可能是数字'
        num, pos = parse_number(s, pos)
        return num, pos

    raise JsonUnexpectCharException(u'(", [, {, false, true, null, number)', u'(%s)' % s[pos])

##############################################################
'''
打印

'''

def print_val(buf, v, indent = 0):
    if isinstance(v, (list)):
        print_list(buf, v, indent)
    elif isinstance(v, (dict)):
        print_dict(buf, v, indent)
    elif isinstance(v, (int, float)):
        print_num(buf, v, indent)
    elif isinstance(v, (str, unicode)):
        print_str(buf, v, indent)
    elif isinstance(v, (bool)):
        print_bool(buf, v, indent)
    elif type(v) == type(None):
        print_null(buf, v, indent)
    else:
        print type(v)
        raise JsonInvalidException(u'不支持的类型')

def print_null(buf, v, indent=0):
    buf.append('%s' % v)

def print_bool(buf, v, indent=0):
    buf.append('%s' % v)

def print_str(buf,v, indent=0):
    buf.append(u'"%s"' % v)

def print_num(buf, v, indent=0):
    buf.append('%s' % v)

def print_list(buf, l, indent = 0):
    cnt = 0
    buf.append(u'[\r\n')
    for item in l:
        cnt += 1
        buf.append(u' ' * (indent+1))
        print_val(buf, item, 2)
        if cnt != len(l):
            buf.append(u',\r\n')

    buf.append(u'\r\n%s%s' % (u' ' * indent, u']'))


def print_dict(buf, d, indent = 0):
    cnt = 0
    buf.append(u'{\r\n')
    for k, v in d.iteritems():
        cnt += 1
        buf.append(u'%s"%s" : ' % (u' ' * (indent+1), k))
        print_val(buf, v, 2),
        if cnt != len(d):
            buf.append(u',\r\n')
    buf.append(u'\r\n%s%s' % (u' ' * indent, u'}'))




##############################################################
##############################################################
'''
各种异常
'''
class JsonInvalidException(Exception):
    '''
    Json格式错误
    '''

class JsonNumberInvalidException(JsonInvalidException):
    '''
    数字格式不正确
    '''
    def __init__(self, s_number):
        JsonInvalidException.__init__(self,
                u"错误的数字： %s" % s_number)


class JsonUnexpectCharException(JsonInvalidException):
    '''
    遇到为期望的字符
    '''
    def __init__(self, exp_ch, unexp_ch):
        JsonInvalidException.__init__(self,
                u"期望'%s' 得到的却是'%s'" % (exp_ch, unexp_ch))

class JsonEndInvalidException(JsonInvalidException):
    '''
    非法结尾
    '''
    def __init__(self, s_expect):
        JsonEndInvalidException.__init__(self,
                u"希望遇到'%s' 但是遇到字符串尾" % s_expect)

##############################################################

'''
深度拷贝
'''
def deepcopy(v):
    #print type(v)
    if isinstance(v, (list)):
        return deepcopy_list(v)
    elif isinstance(v, (dict)):
        return deepcopy_dict(v)
    elif isinstance(v, (int, float)):
        return deepcopy_number(v)
    elif isinstance(v, (str, unicode)):
        return deepcopy_unicode(v)
    elif isinstance(v, (bool)):
        return deepcopy_bool(v)
    elif type(v) == type(None):
        return deepcopy_null()
    else:
        print type(v)
        raise JsonInvalidException(u'不支持的类型')


def deepcopy_dict(d):
    '''
    字典深度拷贝
    '''
    #print type(d)
    assert type(d) == type({})

    ret = {}
    for k, v in d.iteritems():
        ret[deepcopy(k)] = deepcopy(v)
    return ret


def deepcopy_list(l):
    assert isinstance(l, list)

    ret = []
    for item in l:
        ret.append(deepcopy(item))
    return ret

def deepcopy_unicode(s):
    assert isinstance(s, unicode)

    return ''.join(s[:])

def deepcopy_number(n):
    assert isinstance(n, (int, float))

    return n

def deepcopy_bool(b):
    assert type(s) in [type(bool)]

    return b

def deepcopy_null():
    return None

##############################################################

class JsonParser:
    def __init__(self):
        self.dict = None

    def load(self, s):
        '''
        读取json格式数据，输入s为一个json字符串，无返回值
        若遇到格式错误的应该抛出异常，json中数字如果超出了python里的浮点数上限的，也可以抛出异常
        所有字符串（键和值）转化为python中的unicode类型字符串，特别注意转义符的转化
        为简便考虑，json的最外层假定只为 object
        '''
        s = s.decode('utf-8')
        self.dict, pos  = parse_object(s, 0)

    def dump(self):
        '''
        根据类中数据返回json字符串
        '''
        pass

    def loadJson(self, f):
        '''
        从文件中读入json格式数据，f为文件路径，格式错误抛出异常
        '''
        self.load(open(f).read().decode('utf-8'))

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

    @print_caller
    def dumpDict(self):
        '''
        返回一个字典
        '''
        return deepcopy(self.dict)

if __name__ == '__main__':
    print 'main'

    jsonfile = u'test3.json'
    print open(jsonfile).read()

    a = JsonParser()
    try:
        a.load(open(jsonfile).read())
        d1 = a.dumpDict()
        print d1
        buf = []
        print_dict(buf, d1)
        print ''.join(buf), u'\r\n'
    except JsonUnexpectCharException as e:
        err( u'捕获异常: %s' % unicode(e))
    except JsonNumberInvalidException as e:
        err( u'捕获异常: %s' % unicode(e))
    except JsonEndInvalidException as e:
        err( u'捕获异常: %s' % unicode(e))
    except JsonInvalidException as e:
        err( u'捕获异常: %s' % unicode(e))

    '''
    simplejson对比测试
    '''
    print '#' * 40
    print 'simplejson测试'

    d2 = json.loads(open(jsonfile).read())
    print d2
    print json.dumps(open(jsonfile).read())

    infog(u'd1 == d2 : %s' % (d1 == d2))
