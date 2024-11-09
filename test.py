import re

pattern = r'\W+'

text = 'Hallo Ditta!'

x = re.findall(pattern,text)

print(x)