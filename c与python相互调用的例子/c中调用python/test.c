/*
 * =====================================================================================
 *
 *       Filename:  test.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  06/25/2012 10:37:23 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Dr. Fritz Mehner (mn), mehner@fh-swf.de
 *        Company:  FH Südwestfalen, Iserlohn
 *
 * =====================================================================================
 */
#include <stdio.h>
#include <stdlib.h>
#include "/usr/include/python2.6/Python.h"
	void printDict(PyObject* obj) {  
		if (!PyDict_Check(obj))  
			return;  
		PyObject *k, *keys;  
		keys = PyDict_Keys(obj);  
		int i = 0;
		for (i = 0; i < PyList_GET_SIZE(keys); i++) {  
			k = PyList_GET_ITEM(keys, i);  
			char* c_name = PyString_AsString(k);  
			printf("%s\n", c_name);  
		}  
	}  

int main(int argc, char* argv[])
{
	PyObject *pModel, *pDict, *pFunc, *pArgs, *pRetVal;

	// 初始化Python 
	//在使用Python系统前，必须使用Py_Initialize对其 
	//进行初始化。它会载入Python的内建模块并添加系统路 
	//径到模块搜索路径中。这个函数没有返回值，检查系统 
	//是否初始化成功需要使用Py_IsInitialized。 
	Py_Initialize();

	// 检查初始化是否成功 
	if (!Py_IsInitialized())
	{
		return -1;
	}

	// 添加当前路径 
	//把输入的字符串作为Python代码直接运行，返回0 
	//表示成功，-1表示有错。大多时候错误都是因为字符串 
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");
	// 载入名为pytest的脚本 
	pModel = PyImport_ImportModule("pytest");

	if (!pModel)
	{
		printf("can't find pytest.py\n");
		return -1;
	}
	//得到模块字典
	pDict = PyModule_GetDict(pModel);
	if (!pDict)
	{
		return -1;
	}
	printDict(pDict);
	// 找出函数名为add的函数 
	pFunc = PyDict_GetItemString(pDict, "add");
	if (!pFunc || !PyCallable_Check(pFunc))
	{
		printf("can't find function [add]");
		getchar();
		return -1;
	}
	//创建参数
	pArgs = PyTuple_New(2);
	//  PyObject* Py_BuildValue(char *format, ...) 
	//  把C++的变量转换成一个Python对象。当需要从 
	//  C++传递变量到Python时，就会使用这个函数。此函数 
	//  有点类似C的printf，但格式不同。常用的格式有 
	//  s 表示字符串， 
	//  i 表示整型变量， 
	//  f 表示浮点数， 
	//  O 表示一个Python对象。 
	PyTuple_SetItem(pArgs, 0, Py_BuildValue("l", 3));
	PyTuple_SetItem(pArgs, 1, Py_BuildValue("l", 4));
	// 调用Python函数
	pRetVal = PyObject_CallObject(pFunc, pArgs);
	Py_DECREF(pArgs);
	Py_DECREF(pModel);
	Py_DECREF(pRetVal);
	Py_DECREF(pDict);
	Py_DECREF(pFunc);

	//以上为普通函数的使用。
	//下面显示类的使用
	/*******************************************************
	 * ****************************************************
	 * ****************************************************/
	// 载入名为pytest的脚本 
	pModel = PyImport_ImportModule("pytest");

	if (!pModel)
	{
		printf("can't find pytest.py\n");
		return -1;
	}
	//得到模块字典
	pDict = PyModule_GetDict(pModel);
	if (!pDict)
	{
		return -1;
	}
	printDict(pDict);

	PyObject* pClassPerson = PyDict_GetItemString(pDict, "Person");
	if (!pClassPerson)
	{
		printf("can't find Person class.\n");
		return -1;
	}

	//构造Person实例
	PyObject* pInstancePerson = PyInstance_New(pClassPerson, NULL, NULL);
	if (!pInstancePerson)
	{
		printf("can't create Person instance.\n");
		return -1;
	}

	PyObject_CallMethod(pInstancePerson, "s", "Huang");

	Py_DECREF(pModel);
	Py_DECREF(pDict);
	Py_DECREF(pClassPerson);
	Py_DECREF(pInstancePerson);


	Py_Finalize();
	return 0;

}
