#https://leetcode.com/problems/palindromic-substrings/solution/

def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        m_map = set([])
        m_map.add((0,0))
        count = 1

        for i in range(0, len(s)):
            m_map.add((i,i))
            if i+1 <len(s) and s[i] == s[i+1]:
                offset = 1
                m_map.add((i,i+1))
                while(i-offset >=0 and i+offset+1 < len(s) and s[i-offset] == s[i+offset+1]):
                    m_map.add((i-offset,i+offset+1))
                    offset += 1
            if i-1 >= 0 and i+1 < len(s) and s[i+1] == s[i-1]:
                m_map.add((i-1,i+1))
                offset = 1
                while(i-offset-1 >=0 and i+offset+1 < len(s) and s[i-offset-1] == s[i+offset+1]):
                    m_map.add((i-offset-1,i+offset+1))
                    offset += 1

        return len(list(m_map))
