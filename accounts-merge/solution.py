#https://leetcode.com/problems/accounts-merge/submissions/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_map = {}
        for account in accounts:
            name, email_list =  account[0], account[1:]
            if name not in account_map:
                account_map[name] = [account[1:]]
            else:
                account_map[name].append(email_list)
        out = []
        for k,v in account_map.items():
            ml = self.merge_lists(v)
            for m in ml:
                out.append([k]+sorted(m))
        return out

    def merge_lists(self, nested_list):
        temp = []
        for i in range(len(nested_list)-1):
            sublist = nested_list[i]
            for j in range(i+1, len(nested_list)):
                secondsublist = nested_list[j]
                for email in sublist:
                    if email in secondsublist:
                        temp.append(j)
                        temp.append(i)
        prep_list = []
        outlist = []
        for i in range(len(nested_list)):
            if i in temp:
                prep_list= prep_list+nested_list[i]
            else:
                outlist.append(list(set(nested_list[i])))
        if prep_list:

            outlist.append(list(set(prep_list)))
        return outlist


