#-*-coding:utf-8-*-
#!/usr/bin/python


##############################################################
'''
打印

'''

def print_val(buf, v, indent = 0):
    if isinstance(v, (list)):
        print_list(buf, v, indent)
    elif isinstance(v, (dict)):
        print_dict(buf, v, indent)
    elif isinstance(v, (bool)):
        print_bool(buf, v, indent)
    elif isinstance(v, (int, float)):
        print_num(buf, v, indent)
    elif isinstance(v, (str, unicode)):
        print_str(buf, v, indent)
    elif type(v) == type(None):
        print_null(buf, v, indent)
    else:
        print type(v)
        raise JsonInvalidException(u'不支持的类型')

def print_null(buf, v, indent=0):
    buf.append('%s%s' % (u' ' * indent, u'null'))

def print_bool(buf, v, indent=0):
    buf.append('%s%s' % (u' ' * indent, u'true' if v else u'false'))

def print_str(buf,v, indent=0):
    buf.append(u'%s"%s"' % (u' ' * indent, v))

def print_num(buf, v, indent=0):
    buf.append(u'%s%s' % (u' ' * indent, v))

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


