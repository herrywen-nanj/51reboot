### str方法
```
.count          返回str在string 里面出现的次数,可以通过beg和end指定查找范围
.startswith     检查字符串是否是以指定子字符串开头,是则返回True否则返回False.可以通过beg和end指定查找范围
.endswith       检查字符串是否是以指定子字符串结尾,是则返回True否则返回False.可以通过beg和end指定查找范围
.find           检测指定字符是否包含在字符串中，存在返回索引值，不存在返回-1
.format         字符串格式化输出
.index          与.find类似,只不过如果指定字符不在字符串中会报一个异常.
.isdigit        判断字符串是否只包含数字,如果是返回True否则返回False
.islower        判断字符串是否全为小写,如果是返回True否则返回False 
.isupper        判断字符串是否全为大写,如果是返回True否则返回False  
.join           以指定字符串作为分隔符，合并为新的字符串  
.ljust          返回一个原字符串左对齐  
.lower          转换字符串中所有大写字符为小写
.lstrip         截掉字符串左边的空格或指定字符
.replace        字符串替换  
.rjust          返回一个原字符串右对齐  
.split          指定分隔符对字符串进行分割
.strip          去除左右两端空格  
.upper          转换字符串中的小写字母为大写
```

### list方法
```
.append         在列表末尾添加新的对象
.count          统计某个元素在列表中出现的次数
.extend         在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
.index          从列表中找出某个值第一个匹配项的索引位置
.insert         将对象插入列表指定位置
.pop            移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
.remove         移除列表中某个值的第一个匹配项
.reverse        反向列表中元素
.sort           对原列表进行排序
```
