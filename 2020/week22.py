import re

string = r'D:\qb\workspace\3797\src\platform\blah\...'
#string = r'D:\qb\workspace\a3s7d97a\src\platform\blah\...'
#pattern = r'D:\\qb\\workspace\\[0-9]+\\src\\'
pattern = r'D:\\qb\\workspace\\\w*\\src\\'
result = re.sub(pattern, '', string)

print(result)