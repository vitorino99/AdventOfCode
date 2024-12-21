import re
from utils import ler_arquivo_txt

entrada = ler_arquivo_txt('day3/input.txt')
padrao = re.compile(r"mul\((\d+\s*,\s*\d+)\)|(do\(\)|don't\(\))")
matches = padrao.findall(entrada)

result = 0
flag = True
for x in matches:
    if "don'" in x[1]:
        flag = False
        continue
    elif 'do' in x[1]:
        flag = True
        continue
    if flag:
        value = eval(x[0])
        result += value[0] * value[1]
print(result)

