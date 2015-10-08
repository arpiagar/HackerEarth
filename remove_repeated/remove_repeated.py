def remove_repeated(input_string):
    output_array = []
    repeat_hash = {}
    for elem in input_string:
        if not repeat_hash.has_key(elem):
            repeat_hash[elem] =  True
            output_array.append(elem)
    return "".join(output_array)

print remove_repeated("aaasjbfkhbgejhvsassadfsva")
print remove_repeated("aaabbbcccaaann")