import sys

args = sys.argv

input = (args[1])
output = (args[2])

outfile = open(output, 'w')

with open(input) as f:
    for line in f:
        if line.strip():
            outfile.write(line)
    
outfile.close()

print("Done.")