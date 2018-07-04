import random
import string

url=''
for i in range(11):
    url=url+(random.choice((string.digits + string.letters)))
    
print(url)
