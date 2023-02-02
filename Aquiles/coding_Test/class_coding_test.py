# Aquiles Code Testing Module
from writer import printer



 #Simply version

key_words = 'class def self self. def _'

file_name = input("")

file1 = open(file_name, 'r')

Lines = file1.readlines()
  
count = 0

for line in Lines:
    count += 1
    p = printer()
    code_line = line.strip()

    if key_words.find(code_line) == -1:
        p.success("Line{}: {}".format(count, line.strip()))
    if code_line == "":
        p.warning("Line{}: {} Blank Space".format(count, line.strip()))


        
      
    