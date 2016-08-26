amount = int(raw_input('enter the amount'))

denominations = [1,2,3]

def get_possible_combinations(amount, denominations,curr_list, output_list):
	for elem in denominations:
		if amount-elem > 0:
			new_list = [x for x in curr_list]
			new_list.append(elem)
			output_list = get_possible_combinations(amount-elem,denominations, new_list, output_list)
		elif amount-elem ==0:
			curr_list.append(elem)
			output_list.append(curr_list)
	return output_list

print get_possible_combinations(amount, denominations,[], [])

