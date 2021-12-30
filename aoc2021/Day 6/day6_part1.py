
file = open('day6.in', 'r')

input_array = list(map(int, [line for line in file.readlines()][0].split(",")))

#fish_list = input_array

fish_list = [1]

for days in range(256):
    temp_list = []
    for fish in fish_list:
        if fish > 0:
            temp_list.append(fish-1)
            
        if fish == 0:
            temp_list.append(6)
            temp_list.append(8)
            
    fish_list = temp_list
    print('day:', days, '; number of fishes:', len(fish_list))        
    
    


