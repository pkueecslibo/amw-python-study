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

ESC_CONTROL_CHAR = {
        u'"':   u'"',
        u'\\':   u'\\',
        u'/':   u'/',
        u'b':   u'\b',
        u'f':   u'\f',
        u'n':   u'\n',
        u'r':   u'\r',
        u't':   u'\t',
        }

RE_ESC_CONTROL_CHAR = {
        u'"': u'\\"',
        u'\\': u'\\\\',
        u'/': u'\\/',
        u'\b': u'\\b',
        u'\f': u'\\f',
        u'\n': u'\\n',
        u'\r': u'\\r',
        u'\t': u'\\t',
        }

UNICODE_ESCAPE_CHAR = u'u'

STRIP_TAB = [u' ', u'\t', u'\r', u'\n']

CLRF = u'\r\n'

#十进制
DEC_DIGTAL = u'0123456789'
#十六进制
HEX_DIGTAL = u'0123456789abcdef'



##############################################################
'''
工具函数
'''

HEADER = u'\033[95m'
OKBLUE = u'\033[94m'
OKGREEN = u'\033[92m'
WARNING = u'\033[93m'
FAIL = u'\033[91m'
ENDC = u'\033[0m'
BOLD = u"\033[1m"

def disable():
    HEADER = u''
    OKBLUE = u''
    OKGREEN = u''
    WARNING = u''
    FAIL = u''
    ENDC = u''

_debug = False

def infog( msg):
    if _debug:
        print OKGREEN + msg + ENDC

def info( msg):
    if _debug:
        print OKBLUE + msg + ENDC

def warn( msg):
    if _debug:
        print WARNING + msg + ENDC

def err( msg):
    if _debug:
        print FAIL + msg + ENDC

def print_caller(func):
    def func_wrap(*args, **kwargs):
        infog(u'===> %s' % func.func_name)
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


def _is_dec_digit(s, pos):
    return True if s[pos] in DEC_DIGTAL else False

def _is_hex_digit(s, pos):
    return True if s[pos] in HEX_DIGTAL else False

def _is_hex_str(s):
    if len(s) == 4:
        for c in s:
            if c not in HEX_DIGTAL:
                return False
    return True


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
        while True:
            pos += 1
            if esc == False and s[pos] == u'"':
                break
            if esc == True:
                if s[pos] in ESC_CONTROL_CHAR.keys():
                    result.append(ESC_CONTROL_CHAR[s[pos]])
                elif s[pos] == UNICODE_ESCAPE_CHAR:
                    pos += 1
                    hex_s = s[pos:pos+4]
                    pos += 3
                    if not _is_hex_str(hex_s):
                            raise Exception(u'不是正确的十六进制')
                    c = unichr(int(hex_s, 16))
                    result.append(c)
                else:
                    raise Exception(u'不能识别的转义控制符')

                esc = False
            elif s[pos] == u'\\':
                esc  =True
            else:
                result.append(s[pos])
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

        #跳过空白
        pos = _skip_blank(s, pos)

        #如果出现的',', 说明还有键值对
        if s[pos] == u',':
            pos += 1
        else:
            #意味着字典结束，下一个字符必须是'}'
            if s[pos] != u'}':
                raise JsonUnexpectCharException(u'}', s[pos])

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
    while _is_dec_digit(s, pos):
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
    while _is_dec_digit(s, pos):
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

        while _is_dec_digit(s, pos):
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

    if _is_dec_digit(s, pos) or s[pos] in [u'-', u'+']:
        #print '可能是数字'
        num, pos = parse_number(s, pos)
        return num, pos

    raise JsonUnexpectCharException(u'(", [, {, false, true, null, number)', u'(%s)' % s[pos])

##############################################################
'''
打印

'''

def dump_val(buf, v):
    if isinstance(v, (list)):
        dump_list(buf, v)
    elif isinstance(v, (dict)):
        dump_dict(buf, v)
    elif isinstance(v, (bool)):
        dump_bool(buf, v)
    elif isinstance(v, (int, float)):
        dump_num(buf, v)
    elif isinstance(v, (str, unicode)):
        dump_string(buf,v)
    elif type(v) == type(None):
        dump_null(buf, v)
    else:
        print type(v)
        raise JsonInvalidException(u'不支持的类型')

def dump_null(buf, v):
    buf.append('null')

def dump_bool(buf, v):
    buf.append(u'true' if v else u'false')

@print_caller
def dump_string(buf,v):
    s = []
    for c in v:
        if c in RE_ESC_CONTROL_CHAR.keys():
            s.append(RE_ESC_CONTROL_CHAR[c])
        else:
            s.append(u'%c' % c)
    buf.append(u'"%s"' % ''.join(s))

def dump_num(buf, v):
    buf.append('%s' % v)

def dump_list(buf, l):
    cnt = 0
    buf.append(u'[')
    for item in l:
        cnt += 1
        dump_val(buf, item)
        if cnt != len(l):
            buf.append(u',')

    buf.append(u'%s' % (u']'))


def dump_dict(buf, d):
    cnt = 0
    buf.append(u'{')
    for k, v in d.iteritems():
        cnt += 1
        dump_val(buf, k)
        buf.append(u':')
        dump_val(buf, v),
        if cnt != len(d):
            buf.append(u', ')
    buf.append(u'%s' % (u'}'))




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
    elif isinstance(v, (int, float, str, unicode, bool, type(None))):
        return v
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

##############################################################
'''

'''
@print_caller
def update_val(dst, src):

    if isinstance(src, dict):
        return _update_dict(dst, src)
    elif isinstance(src, list):
        return _update_list(dst, src)
    else:
        dst if dst == src else src

def _update_dict(d, rd):
    if rd == None:
        return d

    if d == None: d = {}
    for k, v in rd.iteritems():
        if k in d.keys() and d[k] == v:
            continue
        d[k] = deepcopy(v)
    return d


def _update_list(l, rl):
    return deepcopy(rl)


##############################################################

class object(dict):
    '''
    定义Json中的object对象
    '''
    def __init__(self):
        dict.__init__(self)

class array(list):
    '''
    定义Json中的array对象
    '''
    pass

##############################################################

class JsonParser:
    def __init__(self):
        self.dict = None

    @print_caller
    def load(self, s):
        '''
        读取json格式数据，输入s为一个json字符串，无返回值
        若遇到格式错误的应该抛出异常，json中数字如果超出了python里的浮点数上限的，也可以抛出异常
        所有字符串（键和值）转化为python中的unicode类型字符串，特别注意转义符的转化
        为简便考虑，json的最外层假定只为 object
        '''
        if type(s) != unicode:
            s = s.decode('utf-8')
        self.dict, pos  = parse_object(s, 0)

    @print_caller
    def dump(self):
        '''
        根据类中数据返回json字符串
        '''
        buf = []
        dump_val(buf, self.dict)
        return ''.join(buf)

    @print_caller
    def loadJson(self, f):
        '''
        从文件中读入json格式数据，f为文件路径，格式错误抛出异常
        '''
        try:
            fp = open(f, 'r')
            self.load(fp.read().decode(u'utf-8'))
            #self.load(fp.read())
        finally:
            fp.close()

    @print_caller
    def dumpJson(self, f):
        '''
        将类中的内容以json格式存入文件中，文件若存在则覆盖，文件操作失败抛出异常
        '''
        buf = []
        dump_val(buf, self.dict)

        try:
            fp = open(f, 'w')
            fp.seek(0)
            fp.truncate()
            fp.write(u''.join(buf).encode('utf_8'))
        finally:
            fp.close()

    def loadDict(self, d):
        '''
        读取dict中的数据，存入类中，若遇到不是字符串的key则忽略
        '''
        _d = deepcopy(d)
        if self.dict:
            self.dict.udpate(_d)
        else:
            self.dict = _d

    @print_caller
    def dumpDict(self):
        '''
        返回一个字典
        '''
        return deepcopy(self.dict)

    #高级功能扩展
    def __getitem__(self, key):
        return self.dict.__getitem__(key)

    def __setitem__(self, key, val):
        return self.dict.__setitem__(key, val)

    def __delitem__(self, key):
        return self.dict.__delitem__(key)

    def __getslice__(self, start, end):
        return self.dict.__getslice__(start, end)

    def update(self, d):
        self.dict.update(d)


if __name__ == '__main__':
    try:
        a1 = JsonParser()
        a2 = JsonParser()
        a3 = JsonParser()

        jsonfile = u'test3.json'
        test_json_file = open(jsonfile).read()

        a1.load(test_json_file)
        d1 = a1.dumpDict()


        file_path = u'result.json'
        a2.loadDict(d1)
        a2.dumpJson(file_path)
        a3.loadJson(file_path)
        d3 = a3.dumpDict()

        #print d1
        #print d3
        print d1 == d3

    except JsonUnexpectCharException as e:
        err( u'捕获异常: %s' % unicode(e))
    except JsonNumberInvalidException as e:
        err( u'捕获异常: %s' % unicode(e))
    except JsonEndInvalidException as e:
        err( u'捕获异常: %s' % unicode(e))
    except JsonInvalidException as e:
        err( u'捕获异常: %s' % unicode(e))
    except Exception as e:
        err( u'捕获异常: %s' % unicode(e))
