import sys

args = sys.argv

input = (args[1])
output = (args[2])

# Get file contents
infile = open(input)
contents = infile.readlines()
infile.close()

new_contents = []

outfile = open(output, 'w')

# Get rid of empty lines
for line in contents:
    # Strip whitespace. Should leave nothing if empty line was just "\n".
    # In that case, write what we have so far and insert a blank line after.
    if not line.strip():
        outfile.write(" ".join(new_contents))
        outfile.write("\n\n")
        new_contents = []
    # We got something, save it
    else:
        new_contents.append(line.strip())
        
outfile.close()

print("Done.")