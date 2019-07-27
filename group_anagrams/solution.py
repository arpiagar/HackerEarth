class Solution(object):
    def groupAnagrams(self, strs):
        elem_map = {}
        for elem in strs:
            temp = "".join(sorted(elem))
            if elem_map.has_key(temp):
                elem_map[temp].append(elem)
            else:
                elem_map[temp] = [elem]
        out_list = []
        for elem in elem_map.keys():
            out_list.append(elem_map[elem])
        return out_list
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

