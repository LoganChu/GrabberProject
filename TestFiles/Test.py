#opening file to write
with open("test.csv", "w") as file:
    line = ""
    n = [0]*9
    line += str(n)[1:-1]+", "
    line+=(str(n)[1:-1]+", ")
    file.write(line[0:-2])










