file = open("034_multiLine_file.txt", "w")
text = '''Line 1 
Line 2
Line 3
Line 4
Line 5'''
file.write(text)
file.close()

file = open("034_multiLine_file.txt", "r")
lines = file.readline()
while lines != "":
    print(lines)
    lines = file.readline()

file.close()