file_name = raw_input("Enter file name: ")
in_file = open(file_name, "r")
lines = []
for line in in_file:
    lines.append(line)
in_file.close()
out_file = open(file_name, "w")
i = len(lines) - 1
while i >= 0:
    out_file.write(lines[i])
    i -= 1
out_file.close()
