class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        path_list = [x for x in path_list if x != ""]
        stack = []
        for elem in path_list:
            if elem == ".":
                continue
            elif elem == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(elem)
        
        return "/"+"/".join(stack)
