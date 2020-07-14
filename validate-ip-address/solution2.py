class Solution:
    
    
    def validIPAddress(self, IP: str) -> str:
        def check_v4(ip):
            octates = ip.split('.')
            if len(octates) != 4:
                return False
            
            for octate in octates:
                if not octate or not octate.isdigit():
                    return False
                
                if octate[0] == '0' and len(octate) > 1:
                    return False
                
                if int(octate) > 255:
                    return False
                
            return True
        
        def check_v6(ip):
            allowed_chars = set(('a', 'b', 'c', 'd', 'e', 'f'))
            sections = ip.split(':')
            if len(sections) != 8:
                return False
            
            for section in sections:
                if not section or len(section) > 4:
                    return False
                
                for c in section:
                    if c.isdigit():
                        continue
                    elif c.lower() not in allowed_chars:
                        return False
            return True
        
        if check_v4(IP):
            return "IPv4"
        elif check_v6(IP):
            return "IPv6"
        
        return "Neither"
