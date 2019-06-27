# Python3 
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
创建字符串很简单，只要为变量分配一个值即可。例如：
```
var1 = 'Hello World!'
var2 = "Runoob"
```
---
## Python 访问字符串中的值
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python 访问子字符串，可以使用方括号来截取字符串，如下实例：
```
## 实例(Python 3.0+)
#!/usr/bin/python3
 
var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
```
以上实例执行结果：
```
var1[0]:  H
var2[1:5]:  unoo
```
---
## Python 字符串更新
你可以截取字符串的一部分并与其他字段拼接，如下实例：
```
## 实例(Python 3.0+)
#!/usr/bin/python3
 
var1 = 'Hello World!'
 
print ("已更新字符串 : ", var1[:6] + 'Runoob!')
```
以上实例执行结果
```
已更新字符串 :  Hello Runoob!
```
---
## Python转义字符
在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：
转义字符|描述
:-:|:-:
\(在行尾时)|续行符
\\|反斜杠符号
\'|单引号
\"|双引号
\a|响铃
\b|退格(Backspace)
\000|空
\n|换行
\v|纵向制表符
\t|横向制表符
\r|回车
\f|换页
\oyy|八进制数，yy代表的字符，例如：\o12代表换行
\xyy|十六进制数，yy代表的字符，例如：\x0a代表换行
\other|其它的字符以普通格式输出
---
## Python字符串运算符
下表实例变量a值为字符串 "Hello"，b变量值为 "Python"：
操作符|描述|实例
:-:|:-:|:-:
+|字符串连接| a + b 输出结果： HelloPython
*|重复输出字符串| a*2 输出结果：HelloHello
[]|通过索引获取字符串中字符|代码块
[ : ]|代码块|代码块
in|成员运算符 - 如果字符串中包含给定的字符返回 True |代码块
not in |成员运算符 - 如果字符串中不包含给定的字符返回 True |代码块
r/R|代码块|代码块
%|格式字符串|请看下一节内容。
```
## 实例(Python 3.0+)
#!/usr/bin/python3
 
a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')
```
以上实例输出结果为：
```
a + b 输出结果： HelloPython
a * 2 输出结果： HelloHello
a[1] 输出结果： e
a[1:4] 输出结果： ell
H 在变量 a 中
M 不在变量 a 中
\n
\n```
---
## Python字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
```
## 实例(Python 3.0+)
#!/usr/bin/python3
 
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
```
以上实例输出结果：
```
我叫 小明 今年 10 岁!
```
python字符串格式化符号:
