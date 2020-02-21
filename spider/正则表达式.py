import re

content="Hello 1234567 World_This is a Regex Demo"
#pattern=re.compile("Hello.*Demo",re.S)
# re.compile 将正则字符串编译成正则表达式对象
result=re.search("Hello.*(W.*_.*?s)\s.*Demo",content)
print(result.group(1))


"""
# 最常规的匹配
content='Hello 123 4567 World_This is a Regex Demo'
print(len(content))#41
result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)#<_sre.SRE_Match object; span=(0, 41), match='Hello 123 4567 World_This is a Regex Demo'>
print(result.group())#Hello 123 4567 World_This is a Regex Demo
print(result.span())#(0,41)

# 泛匹配
content='Hello 123 4567 World_This is a Regex Demo'
result=re.match("^Hello.*Demo$",content)
print(result)
print(result.group())
print(result.span())
"""

