# dictionary
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
> d = {key1 : value1, key2 : value2 }

键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
一个简单的字典实例：
> dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

也可如此创建字典：
> dict1 = { 'abc': 456 }    
> dict2 = { 'abc': 123, 98.6: 37 }
# 访问字典里的值
使用索引访问字典里的值
> #!/usr/bin/python3    
> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}    
> print ("dict['Name']: ", dict['Name'])    
> print ("dict['Age']: ", dict['Age'])
# 修改字典里的值
向字典添加新内容的方法是增加新的键/值对，或通过已有键找到对应的值进行修改：
> #!/usr/bin/python3    
> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}  
> dict['Age'] = 8               # 更新 Age   
> dict['School'] = "菜鸟教程"  # 添加信息  
> print ("dict['Age']: ", dict['Age'])  
> print ("dict['School']: ", dict['School'])
# 删除字典里的值
> #!/usr/bin/python3    
> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}    
> del dict['Name'] # 删除键 'Name'    
> dict.clear()     # 清空字典    
> del dict         # 删除字典
# 字典键的特性
* 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住    
* 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

# 字典内置函数
## 计算字典元素个数
> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}    
> len(dict)    
> 结果：3
## 输出字典，以可打印的字符串表示
> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}    
> str(dict)    
> "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"
## in操作符
如果键在字典dict里返回true，否则返回false
Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true
> #!/usr/bin/python3    
dict = {'Name': 'Runoob', 'Age': 7}    
 if  'Age' in dict:    
    print("键 Age 存在")    
else :    
    print("键 Age 不存在")    
if  'Sex' in dict:    
    print("键 Sex 存在")    
else :    
    print("键 Sex 不存在")    
## not in 操作符
> if  'Age' not in dict:    
    print("键 Age 不存在")    
else :    
    print("键 Age 存在")    

# 字典内置方法
## 删除字典内所有元素
Python 字典 clear() 函数用于删除字典内所有元素。
### 语法
dict.clear()
### 参数
NA
### 返回值
该函数没有任何返回值。
### 实例
> #!/usr/bin/python3    
dict = {'Name': 'Zara', 'Age': 7}    
print ("字典长度 : %d" %  len(dict))    
dict.clear()    
print ("字典删除后长度 : %d" %  len(dict))    
#### 结果
> 字典长度 : 2    
字典删除后长度 : 0
## 从字典获取值的列表
Python 字典 values() 方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。
### 语法
dict.values()
### 参数
NA
### 返回值
返回迭代器。
### 实例
> #!/usr/bin/python3    
dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}    
print ("字典所有值为 : ",  list(dict.values()))
#### 结果
> ['female', 7, 'Zara']
## 字典浅复制
Python 字典 copy() 函数返回一个字典的浅复制。
### 语法
dict.copy()
### 参数
NA
### 返回值
返回一个字典的浅复制。
### 实例
> #!/usr/bin/python3    
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}    
dict2 = dict1.copy()    
print ("新复制的字典为 : ",dict2)
#### 结果
> {'Age': 7, 'Name': 'Runoob', 'Class': 'First'}
### 直接赋值和 copy 的区别
> #!/usr/bin/python    
> \# -*- coding: UTF-8 -*    -
dict1 =  {'user':'runoob','num':[1,2,3]}    
dict2 = dict1          # 浅拷贝: 引用对象    
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用    
> \# 修改 data 数据    
dict1['user']='root    '
dict1['num'].remove(1)    
> \# 输出结果    
print(dict1)    
print(dict2)    
print(dict3)    
#### 结果
实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。
> {'user': 'root', 'num': [2, 3]}    
{'user': 'root', 'num': [2, 3]}    
{'user': 'runoob', 'num': [2, 3]}
## 从字典获取索引的列表
Python3 字典 keys() 方法返回一个可迭代对象，可以使用 list() 来转换为列表。
### 语法
dict.keys()
### 参数
NA
### 返回值
返回一个迭代器。
### 实例
> dict = {'Name': 'Runoob', 'Age': 7}    
> dict.keys()    
dict_keys(['Name', 'Age'])    
> list(dict.keys())             # 转换为列表    
['Name', 'Age']
## 从字典中删除指定的元素
Python 字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
### 语法
> pop(key[,default])
### 参数
* key 要删除的元素
* default 如果key不存在，返回default值

### 返回值
返回被删除的元素的值
### 实例
> site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}    
> pop_obj=site.pop('name')    
> print(pop_obj)    
