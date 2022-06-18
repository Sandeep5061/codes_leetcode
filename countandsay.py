<<<<<<< HEAD
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        if n==2:
            return "11"
        val = "11"
        for i in range(3 , n+1):
            val = self.counter(val)
        return val
        
        
    def counter(self , val):
        res = ""
        val = val + '&'
        temp = 1
        for i in range(1 , len(val)):
            if val[i]!=val[i-1]:
                res = res + str(temp)
                res = res + val[i-1]
                temp = 1
            else:
                temp = temp + 1
        return res
=======

class Solution:
    def countAndSay(self, n: int) -> str:
        
        f = "1"
        
        if n == 1:
            
            return f
        
        else:
            
            f = "11"
            
            for _ in range(2, n):
                                    
                z = ""
                
                a = 0
                
                b = 1
                
                while b <= len(f) - 1:
                    
                    if f[a] == f[b]:
                        
                        b = b + 1
                        
                    else:
                                            
                        z = z + str(b - a) + str(f[a])
                        
                        a = b
                        
                        b = b + 1
                        
                    if b == len(f) :

                        z = z + str(b - a) + str(f[a])
                
                f = z
                        
        return f
                    
>>>>>>> 329b61c5e63c0ba2c5347f0fb05361dcdfafe986
