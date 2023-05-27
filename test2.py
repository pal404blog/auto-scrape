
outF = open("myOutFile.txt", "w")
for line in textList:
  # write line to output file
  outF.write(line)
  outF.write("\n")
outF.close()
