from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

x = 0
for x in range(3):
    list[x] = input ()

print ("I'm going to write these to the file.")

for x in range(3):
    target.write(linex)
    target.write("\n")


print ("And finally, we close it.")
target.close()