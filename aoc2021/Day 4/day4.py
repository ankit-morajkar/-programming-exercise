# Part 1
import numpy as np
np.__version__

file = open('Day 4/day4.in', 'r')

input_array = [line for line in file.readlines()]

draw_str = input_array[0].strip().split(",")

draw = list(map(int, draw_str))

print(len(draw))
# 100 draws

input_array.pop(0)
input_array.pop(0)

input_array_2 = list(map(int, input_array[0].strip().split(" ")))

# 100 Boards

boards = np.zeros((100, 5, 5))
drawn_boards = np.zeros((100, 5,5))

for board_number in range(100):
  for i in range(5):
    boards[board_number, i] = list(map(int,list(filter(None,input_array[board_number*6+i].strip().split(" ")))))


def check_five(drawn_boards, board_number):
  for row in range(5):
    if (int(drawn_boards[board_number,row,0])+int(drawn_boards[board_number,row,1])+int(drawn_boards[board_number,row,2])+int(drawn_boards[board_number,row,3])+int(drawn_boards[board_number,row,4])) == 5:
      return True
    
  for col in range(5):
    if (int(drawn_boards[board_number,0,col])+int(drawn_boards[board_number,1,col])+int(drawn_boards[board_number,2,col])+int(drawn_boards[board_number,3,col])+int(drawn_boards[board_number,4,col])) == 5:
      return True
    
  return False

drawn_number_final = -1
final_board_number = -1
    
for draw_number in draw:
  for board_number in range(100):
    for row in range(5):
      for col in range(5):
        if boards[board_number, row, col] == draw_number:
          drawn_boards[board_number, row, col] = 1
          
    if check_five(drawn_boards, board_number) == True:
      print('final drawn number', draw_number)
      drawn_number_final = draw_number
      print('final board number', board_number)
      final_board_number = board_number
      break
  
  if drawn_number_final != -1:
    break
    
sum_unpicked_numbers = 0
for row in range(5):
  for col in range(5):
    if drawn_boards[final_board_number, row, col] == 0:
      sum_unpicked_numbers = sum_unpicked_numbers + boards[final_board_number, row, col]
      print(boards[final_board_number, row, col])
      
print(sum_unpicked_numbers)
print(sum_unpicked_numbers*drawn_number_final)
# Correct Answer!!!

#----------------------------------------------------------------------------------------------------------------------------------
import numpy as np
np.__version__

# Part 1
file = open('Day 4/day4.in', 'r')

input_array = [line for line in file.readlines()]

draw_str = input_array[0].strip().split(",")

draw = list(map(int, draw_str))

print(len(draw))
# 100 draws

input_array.pop(0)
input_array.pop(0)

input_array_2 = list(map(int, input_array[0].strip().split(" ")))



# 100 Boards

boards = np.zeros((100, 5, 5))
drawn_boards = np.zeros((100, 5,5))
solved_board_numbers = np.zeros((100))
total_solved_boards = 0

for board_number in range(100):
  for i in range(5):
    boards[board_number, i] = list(map(int,list(filter(None,input_array[board_number*6+i].strip().split(" ")))))


def check_five(drawn_boards, board_number):
  for row in range(5):
    if (int(drawn_boards[board_number,row,0])+int(drawn_boards[board_number,row,1])+int(drawn_boards[board_number,row,2])+int(drawn_boards[board_number,row,3])+int(drawn_boards[board_number,row,4])) == 5:
      solved_board_numbers[board_number] = 1
      return True
    
  for col in range(5):
    if (int(drawn_boards[board_number,0,col])+int(drawn_boards[board_number,1,col])+int(drawn_boards[board_number,2,col])+int(drawn_boards[board_number,3,col])+int(drawn_boards[board_number,4,col])) == 5:
      solved_board_numbers[board_number] = 1
      return True
    
  return False
    
drawn_number_final = -1
final_board_number = -1
    
for draw_number in draw:
  for board_number in range(100):
    total_solved_boards = 0
    for row in range(5):
      for col in range(5):
        if boards[board_number, row, col] == draw_number:
          drawn_boards[board_number, row, col] = 1
          
    if check_five(drawn_boards, board_number) == True:
      print('final drawn number', draw_number)
      drawn_number_final = draw_number
      print('final board number', board_number)
      final_board_number = board_number
      for solve_index in solved_board_numbers:
        if solve_index == 1:
          total_solved_boards = total_solved_boards + 1
          
      if total_solved_boards == 100:
        break
  if total_solved_boards == 100:
    break    
  
  
    
sum_unpicked_numbers = 0
for row in range(5):
  for col in range(5):
    if drawn_boards[final_board_number, row, col] == 0:
      sum_unpicked_numbers = sum_unpicked_numbers + boards[final_board_number, row, col]
      print(boards[final_board_number, row, col])
      
print(sum_unpicked_numbers)
print(sum_unpicked_numbers*drawn_number_final)
