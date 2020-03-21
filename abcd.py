import re

sen1 = '''hi this is saurabh verma, i am the great'''
sen2 = 'start a sentence and the bring it to end'
pattern = re.compile(r'verma')
matches = pattern.finditer(sen1)
print('saurabh')
print(sen1)
print(sen2)
