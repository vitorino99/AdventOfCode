import re
from utils import ler_arquivo_txt
    
regex = r"mul\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)"
entrada = ler_arquivo_txt('day3/input.txt')
matches = re.findall(regex, entrada)
result = 0 

for x in matches:
    result += int(x[0]) * int(x[1])
print(result)