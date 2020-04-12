#https://leetcode.com/problems/robot-return-to-origin/submissions/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h_count = 0
        v_count = 0
        for move in moves:
            if move == "U":
                v_count +=1
            elif move == "D":
                v_count -= 1
            elif move == "R":
                h_count += 1
            else:
                h_count -= 1
        if h_count == 0 and v_count == 0:
            return True
        return False
