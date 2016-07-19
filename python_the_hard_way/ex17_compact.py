from sys import argv

script, from_file, to_file = argv

with open(from_file) as in_file, open(to_file,"w") as out_file:
    out_file.write(in_file.read())
