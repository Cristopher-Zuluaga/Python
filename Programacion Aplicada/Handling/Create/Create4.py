f = open("myfile.txt", "w")
f.write("Hi everyone")
f.close()

f = open("myfile.txt", "r")
print(f.read)