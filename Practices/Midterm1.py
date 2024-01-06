# First we shall read the file content
f = open("students.txt", 'r')
content = f.readlines()       # A list of strings (each line)
f.close()

if content[-1] == "\n":           # Gaurantee one more mistaked blank line in the end of the file
   content.pop()

content_copy = []              # Make a copy for rewriting

for i in range(len(content)):                # Make each string a list and reverse in order to sort out the highest
   content[i] = content[i].split(',')
   content[i][-1] = int(content[i][-1])
   content_copy.append(content[i][:])
   content[i].reverse()


'''
Sort from highest to lowest, content[0] shall be the student information with the highest score, but we need to care about whether there are more students with the same score.
'''

content.sort(reverse=True)    

# Printing out the student with the highest marks

content[0].reverse()
print(f"The student with the highest marks are: \n{content[0]}")

i=1
while content[i][0] == content[i-1][-1] and i < len(content):     # If next one has the same score
   content[i].reverse()
   print(content[i])
   i += 1

# Calculating the average mark

sum = 0                                # Initialize the sum

for i in range(len(content_copy)):
   sum += content_copy[i][-1]                    # v[-1] is an integer already
   content_copy[i][-1] += 5
   content_copy[i][-1]=str(content_copy[i][-1])

print(f"The average mark for all students is: {sum / len(content_copy)}")

# Rewrite the file

f = open("students.txt", 'w')
for v in content_copy:
   f.write(','.join(v) + '\n')
f.close()
