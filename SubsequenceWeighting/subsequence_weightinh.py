test_num = int(raw_input())



def recurse(val_list,wt_list,length,curr_idx,consider_idx,curr_val):
        if consider_idx < length:
            if val_list[curr_idx] < val_list[consider_idx]:
                k1 = recurse(val_list,wt_list,length,curr_idx,consider_idx+1,curr_val)
                curr_val +=  wt_list[consider_idx]
                k2 = recurse(val_list,wt_list,length,consider_idx,consider_idx+1,curr_val)
                return max(k1,k2)
            else:
                return recurse(val_list,wt_list,length,curr_idx,consider_idx+1,curr_val)
        else:
            return curr_val
        

    
for i in xrange(0,test_num):
        length =  int(raw_input())
        value_list = raw_input().split(" ")
        weight_list = raw_input().split(" ")
        value_list = [int(x) for x in value_list]
        weight_list = [int(x) for x in weight_list]
        q = []
        for i in xrange(0,length):
            q.append(recurse(value_list,weight_list,length,i,i+1,weight_list[i])) 
        print max(q)