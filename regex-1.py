import re

str='the price of oil is 65$ for 3boshke'
print(re.findall(r'the price of oil is (\d+)\$ for (\d+)boshke',str))

#################################

str2='salam fafa. salam mehdi. salam sara. salam soosan.'
result=re.search(r'salam',str2)

#################################

str3='salam fafa. salam mehdi. salam sara. salam soosan.'
result2=re.sub(r'salam','Hi',str3)
print(result2)
print(str3)