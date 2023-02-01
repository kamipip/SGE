# Aquiles Code Testing Module
from writer import printer
from langdetect import detect 

  
# Using readlines()
file1 = open('coding_test.py', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print()
    p = printer()
    p.success("Line{},: {}".format(count, line.strip()))
    code_line = line.strip()
    if code_line == "":
        print("Blank Space...")
    else:
        print(detect(code_line))