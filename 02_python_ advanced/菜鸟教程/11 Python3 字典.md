# Python3  
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

```

d = {key1 : value1, key2 : value2 }

```
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
一个简单的字典实例：
```

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

```
也可如此创建字典：
```

dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }

```
---
## 访问字典里的值
把相应的键放入到方括号中，如下实例:
```
## 实例
#!/usr/bin/python3
 
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
```
以上实例输出结果：
```

dict['Name']:  Runoob
dict['Age']:  7
```
如果用字典里没有的键访问数据，会输出错误如下：
```
## 实例
#!/usr/bin/python3
 
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("dict['Alice']: ", dict['Alice'])
```
以上实例输出结果：
```

Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print ("dict['Alice']: ", dict['Alice'])
KeyError: 'Alice'

```
---
## 修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
```
## 实例
#!/usr/bin/python3
 
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
 
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```
```

dict['Age']:  8
dict['School']:  菜鸟教程

```
---
## 删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：
```
## 实例
#!/usr/bin/python3
 
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```
但这会引发一个异常，因为用执行 del 操作后字典不再存在：
```

Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print ("dict['Age']: ", dict['Age'])
TypeError: 'type' object is not subscriptable

```
注：del() 方法后面也会讨论。
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：



1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：


```
## 实例
#!/usr/bin/python3
 
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
 
print ("dict['Name']: ", dict['Name'])
```
以上实例输出结果：
```

dict['Name']:  小菜鸟

```
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
```
## 实例
#!/usr/bin/python3
 
dict = {['Name']: 'Runoob', 'Age': 7}
 
print ("dict['Name']: ", dict['Name'])
```
以上实例输出结果：
```

Traceback (most recent call last):
  File "test.py", line 3, in <module>
    dict = {['Name']: 'Runoob', 'Age': 7}
TypeError: unhashable type: 'list'

```
---
## 字典内置函数&方法
Python字典包含了以下内置函数：
序号|函数及描述|实例
:-:|:-:|:-:
1|代码块|代码块
2|代码块|代码块
3|代码块|代码块
Python字典包含了以下内置方法：
序号|函数及描述
:-:|:-:
1|代码块
2|代码块
3|代码块
4|代码块
5|代码块
6|代码块
7|代码块
8|代码块
9|代码块
10|代码块
11|代码块
12|代码块
---
