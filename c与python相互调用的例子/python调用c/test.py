# -*- coding: utf-8 -*-
import MyCppModule
#导入python的模块（也就是c的模块，注意so文件名是MyCppModule  
r = MyCppModule.MyCppFun1("ls -l")
print r 
print "OK"  
