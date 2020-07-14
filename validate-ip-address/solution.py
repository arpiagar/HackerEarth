

class Solution:
    def validIPAddress(self, IP: str) -> str:
        NEITHER = "Neither"
        IPV4 = "IPv4"
        IPV6 = "IPv6"
        if len(IP.split('::')) > 1 or len(IP.split('..')) > 1:
            return NEITHER
        if len(IP.split('.')) == 4 :
            if self.validateIPV4(IP):
                return IPV4
        elif len(IP.split(':')) == 8:
            if self.validateIPV6(IP):
                return IPV6
        return NEITHER
    
    def validateIPV4(self, ip):
        ip_subnet = ip.split('.')
        valid_set = set([])
        for i in range(0,10):
            valid_set.add(str(i))
        for elem in ip_subnet:
            for subelem in elem:
                if subelem not in valid_set:
                    return False
            
        try:
            valid  = all([int(x)<= 255 and int(x) >= 0 for x in ip_subnet])
        except:
            return False
        if not valid:
            return False
        first_letter_zero = [x for x in ip_subnet if x[0]=="0"]
        for elem in first_letter_zero:
            if len(elem) > 1:
                return False
        return True
    
    
    def validateIPV6(self,ip):
        ip_subnet = ip.split(':')
        invalid = any([len(x)>4 for x in ip_subnet])
        if invalid:
            return False
        valid_set = set([])
        for i in range(0,10):
            valid_set.add(str(i))
        for i in range(0,6):
            valid_set.add(chr(ord('A')+i))
            valid_set.add(chr(ord('a')+i))
        for elem in ip_subnet:
            for sub_elem in elem:
                if sub_elem not in valid_set:
                    return False
        return True

