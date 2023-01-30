---
title: 文件操作
date: 2022-12-6
lastmod: '2022-12-064T16:44:38+08:00'
summary: 文件的各种操作
weight: 80
toc: true
type: book
---

## 文件路径

一个路径是一个文件或文件夹

函数|用法
-:|:-
**os模块**|
os.getcwd()|查看当前路径
os.chdir()|设定工作目录
**os.path模块**|
abspath(path)|	返回给定路径的绝对路径
basename(path)|	返回指定路径的最后一个组成部分
commonpath(paths)|	返回给定的多个路径的最长公共路径
commonprefix(paths)|	返回给定的多个路径的最长公共前缀
dirname(p)|	返回给定路径的文件夹部分
exists(path)|判断文件是否存在
isabs(path)|判断path是否为绝对路径
isdir(path)|判断path是否为文件夹
isfile(path)|判断path是否为文件
join(path, \*paths)|连接两个或多个path
realpath(path)|返回给定路径的绝对路径
relpath(path)|返回给定路径的相对路径，不能跨越磁盘驱动器或分区
samefile(f1, f2)|测试f1和f2这两个路径是否引用的同一个文件
split(path)|以路径中的最后一个斜线为分隔符把路径分隔成两部分，以元组形式返回
splitext(path)|从路径中分隔文件的扩展名
splitdrive(path)|从路径中分隔驱动器的名称

## 打开路径下的所有文件

如果该路径是文件，则路径下没有文件，返回空|如果是文件夹，则返回文件夹下的所有**目录**（就是文件或文件夹的名称）。路径加上该名称就是新的路径。

函数|用途
-:|:-
**os模块**|
listdir(path)|	返回path目录下的文件和目录列表
scandir(path='.')|	返回包含指定文件夹中所有DirEntry对象的迭代对象，遍历文件夹时比listdir()更加高效

## 打开特定的文件

1. path是一个字符串，可以用字符串的endswith函数判断指定类型
2. 可以用splitext函数获取路径的扩展名，从而删选类型

## 为文件改名或移动

[remove，rename，replace](#os)

## 文件的复制

[shutil模块](#shutil)


```python
##如果需要遍历指定目录下所有子目录和文件，可以使用递归的方法。

from os import listdir
from os.path import join, isfile, isdir

def listDirDepthFirst(directory):
    '''深度优先遍历文件夹'''
    #遍历文件夹，如果是文件就直接输出
    #如果是文件夹，就输出显示，然后递归遍历该文件夹
    for subPath in listdir(directory):
        path = join(directory, subPath)
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listDirDepthFirst(path)
```

```python
##下面的代码使用了广度优先遍历方法。

from os import listdir
from os.path import join, isfile, isdir

def listDirWidthFirst(directory):
    '''广度优先遍历文件夹'''
    #使用列表模拟双端队列，效率稍微受影响，不过关系不大
    dirs = [directory]
    #如果还有没遍历过的文件夹，继续循环
    while dirs:
        #遍历还没遍历过的第一项
        current = dirs.pop(0)
        #遍历该文件夹，如果是文件就直接输出显示
        #如果是文件夹，输出显示后，标记为待遍历项
        for subPath in listdir(current):
            path = join(current, subPath)
            if isfile(path):
                print(path)
            elif isdir(path):
                print(path)
                dirs.append(path)

```

## 模块 

### os

方法|	功能说明
-:|:-
chdir(path)	|把path设为当前工作目录
curdir	|当前文件夹
environ	|包含系统环境变量和值的字典
extsep	|当前操作系统所使用的文件扩展名分隔符
get_exec_path()	|返回可执行文件的搜索路径
getcwd()	|返回当前工作目录
listdir(path)	|返回path目录下的文件和目录列表
remove(path)	|删除指定的文件，要求用户拥有删除文件的权限，并且文件没有只读或其他特殊属性
rename(src, dst)|	重命名文件或目录，可以实现文件的移动，若目标文件已存在则抛出异常，不能跨越磁盘或分区
replace(old, new)|	重命名文件或目录，若目标文件已存在则直接覆盖，不能跨越磁盘或分区
scandir(path='.')|	返回包含指定文件夹中所有DirEntry对象的迭代对象，遍历文件夹时比listdir()更加高效
sep	当前操作系统所使用的路径分隔符
startfile(filepath \[, operation\])	|使用关联的应用程序打开指定文件或启动指定应用程序
system()	|启动外部程序

### os.path

方法|	功能说明
-:|:-
abspath(path)|	返回给定路径的绝对路径
basename(path)|	返回指定路径的最后一个组成部分
commonpath(paths)|	返回给定的多个路径的最长公共路径
commonprefix(paths)|	返回给定的多个路径的最长公共前缀
dirname(p)|	返回给定路径的文件夹部分
exists(path)|	判断文件是否存在
getatime(filename)	|返回文件的最后访问时间
getctime(filename)	|返回文件的创建时间
getmtime(filename)	|返回文件的最后修改时间
getsize(filename)	|返回文件的大小
isabs(path)	|判断path是否为绝对路径
isdir(path)	|判断path是否为文件夹
isfile(path)	|判断path是否为文件
join(path, \*paths)	|连接两个或多个path
realpath(path)	|返回给定路径的绝对路径
relpath(path)	|返回给定路径的相对路径，不能跨越磁盘驱动器或分区
samefile(f1, f2)	|测试f1和f2这两个路径是否引用的同一个文件
split(path)	|以路径中的最后一个斜线为分隔符把路径分隔成两部分，以元组形式返回
splitext(path)|	从路径中分隔文件的扩展名
splitdrive(path)|	从路径中分隔驱动器的名称

### shutil

方法	|功能说明
-:|:-
copy(src, dst)	|复制文件，新文件具有同样的文件属性，如果目标文件已存在则抛出异常
copy2(src, dst)|	复制文件，新文件具有原文件完全一样的属性，包括创建时间、修改时间和最后访问时间等等，如果目标文件已存在则抛出异常
copyfile(src, dst)	|复制文件，不复制文件属性，如果目标文件已存在则直接覆盖
copyfileobj(fsrc, fdst)	|在两个文件对象之间复制数据，例如copyfileobj(open('123.txt'), open('456.txt', 'a'))
copymode(src, dst)	|把src的模式位（mode bit）复制到dst上，之后二者具有相同的模式
copystat(src, dst)	|把src的模式位、访问时间等所有状态都复制到dst上
copytree(src, dst)	|递归复制文件夹
disk_usage(path)	|查看磁盘使用情况
move(src, dst)	|移动文件或递归移动文件夹，也可以给文件和文件夹重命名
rmtree(path)	|递归删除文件夹
make_archive(base_name, format, root_dir=None, base_dir=None)	|创建tar或zip格式的压缩文件
unpack_archive(filename, extract_dir=None, format=None)	|解压缩压缩文件

## 对文件对象的操作

按文件中数据的组织形式把文件分为文本文件和二进制文件两类。

文本文件：文本文件存储的是常规字符串，由若干文本行组成，通常每行以换行符'\n'结尾。常规字符串是指记事本或其他文本编辑器能正常显示、编辑并且人类能够直接阅读和理解的字符串，如英文字母、汉字、数字字符串。文本文件可以使用字处理软件如gedit、记事本进行编辑。

二进制文件：二进制文件把对象内容以字节串(bytes)进行存储，无法用记事本或其他普通字处理软件直接进行编辑，通常也无法被人类直接阅读和理解，需要使用专门的软件进行解码后读取、显示、修改或执行。常见的如图形图像文件、音视频文件、可执行文件、资源文件、各种数据库文件、各类office文档等都属于二进制文件。

无论是文本文件还是二进制文件，其操作流程基本都是一致的，首先打开文件并创建文件对象，然后通过该文件对象对文件内容进行读取、写入、删除、修改等操作，最后关闭并保存文件内容。

### 内置函数open

open(file, mode='r', buffering=-1, encoding=None, errors=None,newline=None, closefd=True, opener=None)

file参数指定了被打开的文件名称。（可以认为是文件的路径）

mode参数指定了打开文件后的处理方式。

buffering参数指定了读写文件的缓存模式。0表示不缓存，1表示缓存，如大于1则表示缓冲区的大小。默认值是缓存模式。

encoding参数指定对文本进行编码和解码的方式，只适用于文本模式，可以使用Python支持的任何格式，如GBK、utf8、CP936等等。

mode的可选项：

模式|	说明
-|:-
r|	读模式（默认模式，可省略），如果文件不存在则抛出异常
w	|写模式，如果文件已存在，先清空原有内容
x	|写模式，创建新文件，如果文件已存在则抛出异常
a	|追加模式，不覆盖文件中原有内容
b	|二进制模式（可与其他模式组合使用）
t	|文本模式（默认模式，可省略）
\+	|读、写模式（可与其他模式组合使用）

注意b和\+可以和其他模式组合，比如 `mode='rb'`

### with语句

在实际开发中，读写文件应优先考虑使用上下文管理语句with，关键字with可以自动管理资源，不论因为什么原因（哪怕是代码引发了异常）跳出with块，总能保证文件被正确关闭，并且可以在代码块执行完毕后自动还原进入该代码块时的上下文，常用于文件操作、数据库连接、网络连接、多线程与多进程同步时的锁对象管理等场合。

注意：**with语句后有“：”号，下一行要缩进。**

    with open(filename, mode, encoding) as fp:
        #这里写通过文件对象fp读写文件内容的语句

上下文管理语句with还支持下面的用法：

    with open('test.txt', 'r') as src, open('test_new.txt', 'w') as dst:
        dst.write(src.read())

### 读入二进制文件

数据库文件、图像文件、可执行文件、动态链接库文件、音频文件、视频文件、Office文档等均属于二进制文件。

对于二进制文件，不能使用记事本或其他文本编辑软件直接进行正常读写，也不能通过Python的文件对象直接读取和理解二进制文件的内容。必须正确理解二进制文件结构和序列化规则，然后设计正确的反序列化规则，才能准确地理解二进制文件内容。

所谓序列化，简单地说就是把内存中的数据在不丢失其类型信息的情况下转成二进制形式的过程，对象序列化后的数据经过正确的反序列化过程应该能够准确无误地恢复为原来的对象。

Python中常用的序列化模块有struct、pickle、shelve、marshal。

### 文件的方法和属性

方法|	功能说明
-|:-
close()|	把缓冲区的内容写入文件，同时关闭文件，并释放文件对象
flush()|	把缓冲区的内容写入文件，但不关闭文件
read(\[size\])	|从文本文件中读取size个字符（Python 3.x）的内容作为结果返回，或从二进制文件中读取指定数量的字节并返回，如果省略size则表示读取所有内容
readline()|	从文本文件中读取一行内容作为结果返回
readlines()|	把文本文件中的每行文本作为一个字符串存入列表中，返回该列表
seek(offset\[, whence\])|	把文件指针移动到新的字节位置，offset表示相对于whence的位置。whence为0表示从文件头开始计算，1表示从当前位置开始计算，2表示从文件尾开始计算，默认为0
tell()		|返回文件指针的当前位置
write(s)	|把s的内容写入文件
writelines(s)|	把字符串列表写入文本文件，不添加换行符

一个文件对象被创立后，文本中的每一行可以被看做是他的元素，进行遍历。

### 步骤

1. 先创建文件对象

这个对象被指定了是只读，就会读取文件的内容。被指定了写，之后就可以把内容写入。

encoding决定了文件对象的编码方式，代码被读入或被写入内容的编码方式。如果是读入，必须和原编码方式一致。txt文件的默认编码是cp936，而文件对象也默认是cp936。当读入一个文件后，就不再是编码形式。这时可以换一种编码写入另一个文件。如果是写入，可以是设置编码方式。

`with open() as f`

2. 然后利用文件对象的方法，将内容写入，或者读取文件。

3. 如果是二进制文件，就要先序列化，读入后在反序列化。

4. 最后一定要关闭文件，否则内容不一定被保存。
