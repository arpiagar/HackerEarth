i#https://leetcode.com/problems/partition-labels/submissions/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        out = []
        self.findEnd(0, S, out)
        print(out)
        return [len(x) for x in out]

    def findEnd(self, start, inputstring, out):
        if start >= len(inputstring):
            return
        character = inputstring[start]
        found_map = {}
        last_idx = inputstring.rfind(character)
        start_idx = start
        while last_idx < len(inputstring) and last_idx != start_idx:
                new_last_idx = last_idx
                for i in range(start_idx, last_idx+1):
                    if inputstring[i]  not in found_map:
                        found_map[inputstring[i]] = 1
                        new_last_idx = max(new_last_idx, inputstring.rfind(inputstring[i]))
                start_idx = last_idx
                last_idx = new_last_idx
        out.append(inputstring[start:last_idx+1])
        if last_idx < len(inputstring):
            return self.findEnd(last_idx+1, inputstring, out)
        return


