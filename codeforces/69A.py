# https://codeforces.com/problemset/problem/69/A
# Baba
number_of_vectors = input()
# print("Total Vectors:", int(number_of_vectors))

x_sum = 0
y_sum = 0
z_sum = 0

for vector_index in range(int(number_of_vectors)):
    # print(vector_index)
    vector_input = input()
    vector_input_array = list(map(int, vector_input.split(" ")))
    x_sum = x_sum + vector_input_array[0]
    y_sum = y_sum + vector_input_array[1]
    z_sum = z_sum + vector_input_array[2]
    
if x_sum == 0 and y_sum == 0 and z_sum == 0:
    print("YES")
    
else:
    print("NO")
    