i_index_of_1 = -1
j_index_of_1 = -1
for i in range(5):
    row = input()
    row_array = list(map(int, row.split(" ")))
    for j in range(5):
        if row_array[j] == 1:
            i_index_of_1 = i
            j_index_of_1 = j
            break
    
    if i_index_of_1>-1:
        break
        

print(abs(i_index_of_1 - 2)+abs(j_index_of_1 - 2))