# Part 1
file = open('Day 1/1.in', 'r')

input_array = [line for line in file.readlines()]

input_array_2 = list(map(str.strip, input_array))

file.close()

count = 0

for i in range(0,len(input_array_2)-1):
  if int(input_array_2[i+1]) > int(input_array_2[i]):
    count = count + 1
    print(input_array_2[i+1], input_array_2[i], count)
    
    
print(count)

# Part 2
count = 0
for i in range(0,len(input_array_2)-3):
  if (int(input_array_2[i+1])+int(input_array_2[i+2])+int(input_array_2[i+3])) > (int(input_array_2[i]) + int(input_array_2[i+1]) + int(input_array_2[i+2])):
    count = count + 1
    
  print(int(input_array_2[i+3]))

print(count)