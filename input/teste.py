# -*- coding: UTF-8 -*-
import os.path
import os
from os import listdir
import re



rg2 = '(entrada|Entrada)([0-9])+(\.txt$)'
rg3 = '(entrada|Entrada)([0-9])+([.]txt$)'
rg4 = '(entrada|Entrada)\d+\.txt$'

i = 0
for file in os.listdir('input/'):
    if re.match(rg4, file):
        print(file)
        i += 1
print(i)