def division_without_div_operator(number,divisor):
    if divisor == 0:
        return "infinity","infinity"
    if number == 0:
        return 0,0
    count = 0
    remaining_num =  number
    while remaining_num >= divisor:
        count += 1
        remaining_num -= divisor
    return count,remaining_num

        
print division_without_div_operator(0,32)
print division_without_div_operator(1,0)
print division_without_div_operator(12,6)
print division_without_div_operator(12,24)
print division_without_div_operator(12,5)