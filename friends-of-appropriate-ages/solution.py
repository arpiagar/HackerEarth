#https://leetcode.com/problems/friends-of-appropriate-ages/submissions/
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0 # 5 4 3 2 1
        age_count = {}
        for age in ages:
            if age in age_count:
                age_count[age] += 1
            else:
                age_count[age] = 1
        age_key_list = age_count.keys()
        for age_a in age_key_list :
            for age_b in age_key_list:
                if self.sendsFriendRequest(age_a,age_b):
                    count += age_count[age_a] * age_count[age_b]
                    if age_a == age_b:
                        count -= age_count[age_a]
        return count

    #>A:120   ageb>=67

    def sendsFriendRequest(self, age_a:int,age_b:int) -> bool:
        #age_a = age[a_index]
        #age_b = age[b_index]
        if age_b > age_a:
            return False
        if age_b > 100 and age_a < 100:
            return False
        if float(age_b) <= float(age_a/2) + 7:
            return False
        return True
