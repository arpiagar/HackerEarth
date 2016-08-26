def consume_string(f_map, base_list, i, out_list):
  if i < 10:
    new_list = [x for x in out_list]
    k = consume_string(f_map, base_list, i+1, out_list)
    if  k!= None:
      return k
    base_map = base_list[i]
    flag = True
    for elem in base_map.keys():
      if f_map.has_key(elem) and f_map[elem] >= base_map[elem]:
        f_map[elem] -= base_map[elem]
      else:
        flag =  False
        break
    if flag:
      new_list.append(str(i))
      if f_map_empty(f_map):
        return "".join(new_list)
    #import pdb;pdb.set_trace()
    if flag:
      l1 =  consume_string(f_map, base_list, i, new_list)
      if l1 != None:
        return l1
    m_list = [x for x in new_list]
    l2 =  consume_string(f_map, base_list, i+1, m_list)
    
    if l2 != None:
        return l2

def f_map_empty(f_map):
  for elem in f_map.keys():
    if f_map[elem] !=0:
      return False
  return True
def combination(input_string):
  base_list = [{"Z" : 1,"E" :1,"R" :0,"O" : 1},{"O" : 1,"N":1,"E" :1},{"T":1,"W":1,"O":1},{"T":1,"H":1,"R":1,"E":2},{"F":1,"O":1,"U":1,"R":1},{"F":1,"I":1,"V":1,"E":1},{"S":1,"I":1,"X":1},{"S":1,"E":2,"V":1,"N":1},{"E":1,"I":1,"G":1,"H":1,"T":1},{"N":2,"I":1,"E":1}]
  f_map = frequency_map(input_string)
  for i in xrange(0,10):
    out_list = []
    return consume_string(f_map,base_list,i, out_list)
    

def frequency_map(input_string):
  map1 = {}
  for elem in input_string:
    elem =  elem.upper()
    if map1.has_key(elem):
      map1[elem] += 1
    else:
      map1[elem] = 1
  return map1 


count-i =0(3,3)
3
7-3
# 0123456789
# abc def
# ONE
# TWO
# THREE
# FOUR
# FIVE
# SIX
# SEVEN
# EIGHT
# NINE

filepath  = raw_input('enter filepath').strip()
f = open(filepath)
flag = False
counter = 0
for lines in f:
  print lines
  if not flag:
    flag = True
    n = int(lines)
  else:
    #import pdb;pdb.set_trace()
    value = combination(lines.strip())
    if value != None:
      print "Case %d: %s"%(counter,value)
  counter += 1