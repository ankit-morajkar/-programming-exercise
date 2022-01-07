file = open('day12.in', 'r')
# Part 2
adjacent_nodes_input = [line for line in file.readlines()]

adjacent_nodes_list = []

for adj_nodes in adjacent_nodes_input:
	adjacent_nodes_list.append(adj_nodes.strip().split("-"))

unique_nodes_set = set([])

for adj_nodes in adjacent_nodes_list:
	unique_nodes_set.add(adj_nodes[0])
	unique_nodes_set.add(adj_nodes[1])

# Initialize Adjacency Node Dictionary

adj_dict = {k: [] for k in unique_nodes_set}

for adj_nodes in adjacent_nodes_list:
	adj_dict[adj_nodes[0]].append(adj_nodes[1])
	adj_dict[adj_nodes[1]].append(adj_nodes[0])

max_visit_dict = {k: None for k in unique_nodes_set}

small_caves = []

for key in max_visit_dict:
	if key in ['start', 'end']:
		max_visit_dict[key] = 1
	elif key.islower() == True:
		max_visit_dict[key] = 2
		small_caves.append(key)
	else:
		max_visit_dict[key] = 10000

number_of_paths = 0

def explore(current_node, visit_dict, current_path):
	global adj_dict
	global number_of_paths
	global final_paths
	global small_caves

	if current_node.islower() and current_node in current_path:
		currently_visiting_small_cave_2nd_time = True

	else:
		currently_visiting_small_cave_2nd_time = False

	current_path = current_path + [current_node]
	visit_dict_local = visit_dict.copy()

	visit_dict_local[current_node] = visit_dict_local[current_node] - 1
	if current_node == 'end':
		number_of_paths = number_of_paths + 1

	else:
		adjacent_nodes = adj_dict[current_node]
		if currently_visiting_small_cave_2nd_time:
			for small_cave in small_caves:
				visit_dict_local[small_cave] = visit_dict_local[small_cave] - 1

		for adj_node in adjacent_nodes:
			if visit_dict_local[adj_node]>0:
				explore(adj_node, visit_dict_local, current_path)

explore('start', max_visit_dict, [])

print(number_of_paths)