def possible_combination(input_list):
    if len(input_list) > 0:
        out_list = [z for z in input_list[0]]
    else:
        return []
    for i in xrange(1, len(input_list)):
        new_list = []
        for elem in out_list:            
            for new_elem in input_list[i]:
                new_list.append(elem+new_elem)
        out_list = new_list
    return out_list

print possible_combination(["abc","def","ghi"])
print possible_combination([])


# ##########################Question##########
# Permutate a list of string 
# this question is supposed permutate the characters instead of who string, 

# as input example {"red", "fox", "super" }, the expected output is 

# rfs 
# rfu 
# rfp 
# rfe 
# rfr 
# ros 
# rou 
# rop 
# roe 
# ror 
# rxs 
# rxu 
# rxp 
# rxe 
# rxr 
# efs 
# efu 
# efp 
# efe 
# efr 
# eos 
# eou 
# eop 
# eoe 
# eor 
# exs 
# exu 