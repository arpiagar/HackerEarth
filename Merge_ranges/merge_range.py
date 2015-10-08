class Range:
    def __init__(self, begin, end):
        self.start = begin
        self.end = end


def get_merged_ranges(range_list, new_range):
    offset= None
    max_offset = None
    for i  in xrange(0,len(range_list)):
        temp_offset =  range_list[i].end - new_range.start
        if temp_offset >= 0:
            if offset == None:
                offset = temp_offset
                offset_idx = i
                min_start_range = range_list[i].start
            else:
                if range_list[i].start < min_start_range:
                    offset = temp_offset
                    offset_idx = i
                    min_start_range = range_list[i]
        max_temp_offset =   new_range.end -range_list[i].start 
        if max_temp_offset >= 0:
            if max_offset == None:
                max_offset = max_temp_offset
                max_offset_idx = i
                max_end_range = range_list[i].end
            else:
                if range_list[i].end > max_end_range:
                    max_offset = max_temp_offset
                    max_offset_idx = i
                    max_end_range = range_list[i].end
    return offset_idx,max_offset_idx
    
range_list  = [Range(1,5), Range(9,13), Range(17,22)]
new_range = Range(4,10)
def get_new_list(range_list, new_range):
    start_idx, end_idx = get_merged_ranges(range_list, new_range)
    final_list = range_list[0:start_idx] + [Range(range_list[start_idx].start,range_list[end_idx].end)] + range_list[end_idx+1:len(range_list)]
    for elem in final_list:
        print elem.start, elem.end
get_new_list(range_list, new_range)


        
                    
        
        
            