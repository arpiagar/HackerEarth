https://leetcode.com/problems/simplify-path/submissions/




class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/")
        if path and path[-1] == "/":
            path = path[0:len(path)-1]
        path_list = path.split("/")[1:]
        s = []
        for elem in path_list:
            if elem == "." or elem == "":
                continue
            elif elem == "..":
                if len(s):
                    s = s[0:len(s)-1]
            else:
                s.append(elem)
        if not len(s):
            return "/"
        else:
            output = "/"+"/".join(s)
            return output

