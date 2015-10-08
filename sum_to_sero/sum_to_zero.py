#N elements of an array summing to number X

def elem_sum_zero(ip,value,value_list,count,max_count,index,size,number):
    if index < size:
        elem_sum_zero(ip,value,value_list,count,max_count,index+1,size,number)
        value =  value + ip[index]
        temp_list =  [x for x in value_list]
        temp_list.append(ip[index])
        count += 1
        if count == max_count:
            if value == number:
                print temp_list
            else:
                return 
        elem_sum_zero(ip,value,temp_list,count,max_count,index+1,size,number)
    else:
        return

a = [1,4,-5,2,4,-6,-10]
value = 0
value_list = []
count = 0
max_count = 4
index = 0
size =  len(a)
number = 0
elem_sum_zero(a,value,value_list,count,max_count,index,size,number)
    