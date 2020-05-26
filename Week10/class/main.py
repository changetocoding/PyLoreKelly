import stringbuilder as str

stringbuilder = str.StringBuilder()


path = 'C:\\Dev\\Teaching\\Pupils\\PyLoreKelly\\Week10\\class\\foo'
print(path)

split = path.split("\\")

for folder in split:
    stringbuilder.add(folder + "\\");


stringbuilder.remove()
stringbuilder.remove()
stringbuilder.remove()
stringbuilder.remove()
stringbuilder.add('new folder\\')
stringbuilder.add('dog_breeds.txt')

full_path = stringbuilder.to_string()  # "C:\\Dev\\Teaching\\Pupils\\new folder\\"
print(full_path)

with open(full_path, 'r') as reader:
    for line in reader.readlines():
        print(line, end='')




