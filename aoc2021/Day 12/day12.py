

file = open('day12_test.in', 'r')

adjacent_nodes_input = [line for line in file.readlines()]

adjacent_nodes_list = []

for adj_nodes in adjacent_nodes_input:
	adjacent_nodes_list.append(adj_nodes.strip().split("-"))

#print(adjacent_nodes_list)

unique_nodes_set = set([])

for adj_nodes in adjacent_nodes_list:
	unique_nodes_set.add(adj_nodes[0])
	unique_nodes_set.add(adj_nodes[1])

#print(unique_nodes_set)

# Initialize Adjacency Node Dictionary

adj_dict = {k: [] for k in unique_nodes_set}

for adj_nodes in adjacent_nodes_list:
	adj_dict[adj_nodes[0]].append(adj_nodes[1])
	adj_dict[adj_nodes[1]].append(adj_nodes[0])

#print(adj_dict)

max_visit_dict = {k: None for k in unique_nodes_set}

for key in max_visit_dict:
	#print(key)
	if key.islower() == True:
		max_visit_dict[key] = 1

	else:
		max_visit_dict[key] = 10000

# print(max_visit_dict)

number_of_paths = 0

final_paths = []


def explore(current_node, adj_dict, visit_dict, number_of_paths, current_path, final_paths):
	print("exploring", current_node)
	current_path_temp = current_path

	current_path_temp.append(current_node)
	print(current_path_temp)
	temp_visit_dict = visit_dict
	temp_visit_dict[current_node] = temp_visit_dict[current_node] - 1
	if current_node == 'end':
		number_of_paths = number_of_paths + 1
		final_paths.append(current_path_temp)

	else:
		adjacent_nodes = adj_dict[current_node]
		print("Adjacent Nodes:",adjacent_nodes)
		for adj_node in adjacent_nodes:
			if temp_visit_dict[adj_node] > 0:
				number_of_paths, final_paths = explore(adj_node, adj_dict, temp_visit_dict, number_of_paths, current_path_temp, final_paths)

	return number_of_paths, final_paths

number_of_paths, final_paths = explore('start', adj_dict, max_visit_dict, number_of_paths, [], final_paths)

#print(number_of_paths, final_paths)