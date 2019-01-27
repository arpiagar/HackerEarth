
birth_dates = [[1970,1980], [1946, 1951],[1982,1983],[2002,2005],[2006,2007]]
birth_dates = [[1970,1990], [1946, 1951],[1982,1983],[2002,2005],[2006,2007], [1946,1990], [1946,1951]]


def custom_sort(birth_dates):
	dates_map = {}
	for dates in birth_dates:
		if dates_map.has_key(dates[0]):
			dates_map[dates[0]].append(dates[1])
		else:
			dates_map[dates[0]] = [dates[1]]
	sorted_birth_years = dates_map.keys()
	sorted_birth_years.sort()
	sorted_dates_array = []
	for b_dates in sorted_birth_years:
		for d_dates in dates_map[b_dates]:
			sorted_dates_array.append([b_dates,d_dates])
	return sorted_dates_array

def find_max_population(birth_dates):
	birth_dates.sort(key = lambda x: x[0])
	print custom_sort(birth_dates)
	max_range = None
	max_count = 0
	for i in xrange(0, len(birth_dates) ):
		birth_year,death_year = birth_dates[i][0],birth_dates[i][1]
		count = 1
		for j in xrange(0, len(birth_dates)):
                        if i==j:
                            continue
                        dates = birth_dates[j]
			b_year,d_year = dates[0], dates[1]
                        if birth_year <= b_year and b_year <= death_year:
                                count += 1
                        if d_year > birth_year and d_year < death_year:
                            count -= 1

		if max_count < count:
		    max_range = birth_dates[i]
		    max_count = count

	return max_count,max_range

def find_max_population_method_2(birth_dates):
    delta_map = {}
    max_count = 0
    for dates in birth_dates:
        birth,death = dates[0],dates[1]
        if delta_map.has_key(birth):
            delta_map[birth] += 1
        else:
            delta_map[birth] = 1
        if delta_map.has_key(death):
            delta_map[death] -= 1
        else :
            delta_map[death] = -1
    delta_map_keys = delta_map.keys()
    delta_map_keys.sort()
    count = 0
    print delta_map,delta_map_keys
    for dates in delta_map_keys:
        count += delta_map[dates]
        if count > max_count:
            max_count = count
    return max_count

print find_max_population(birth_dates)
print find_max_population_method_2(birth_dates)
def assertEqual(s,expected, actual):
	if expected != actual:
		print s
	else:
		print "Test passed"

max_count, max_range = find_max_population(birth_dates)
assertEqual("The max count does not match ",3, max_count)
assertEqual("The birth year does not match ",1946, max_range[0])
assertEqual("The death year does not match ",1951, max_range[1])


