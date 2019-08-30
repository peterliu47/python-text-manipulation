import sys

args = sys.argv

input = (args[1])
output = (args[2])

outfile = open(output, 'w')

with open(input) as f:
    outfile.write(" ".join(line.strip() for line in f))
    
outfile.close()

print("Done.")
    
    