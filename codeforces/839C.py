
# Number of Cities
number_of_cities = int(input())

road_connections = []
list_of_roads = []

# Input Paths
for roads in range(number_of_cities-1):
	list_of_roads.append(roads+1)
	road_connections.append(list(map(int, input().split(" "))))

list_of_roads.append(number_of_cities)

# Unvisited Neighbours
city_neighbour_dict =  {k: [] for k in list_of_roads}
for path in road_connections:
	city_neighbour_dict[path[0]].append(path[1])
	city_neighbour_dict[path[1]].append(path[0])

final_expected_sum = 0

# Horse reaching the city
def visit_a_city(current_city, previous_city, distance_travelled_to_reach_previous_city, previous_city_probability):
	global city_neighbour_dict
	global final_expected_sum
	if current_city>1:
		city_neighbour_dict[current_city].remove(previous_city)
		distance_travelled_to_reach_this_city = distance_travelled_to_reach_previous_city+1
		current_city_probability = previous_city_probability*(1/len(city_neighbour_dict[previous_city]))
		city_value = distance_travelled_to_reach_this_city*current_city_probability
	else:
		city_value = 0
		current_city_probability = 1
		distance_travelled_to_reach_this_city = 0

	future_cities = city_neighbour_dict[current_city]
	if future_cities == []:
		final_expected_sum = final_expected_sum + city_value

	for future_city in future_cities:
		visit_a_city(future_city, current_city, distance_travelled_to_reach_this_city, current_city_probability)

visit_a_city(1,1,0,1)

print(final_expected_sum)