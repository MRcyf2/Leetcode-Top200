#214
#manacher

#只需要求出以s[0]为开头的最长回文子串即可。
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def manacher(s):
            ss="#"+'#'.join(s)+"#"
            n=len(ss)
            A,B=[],[1]*n
            mid,r=0,0
            for i in range(n):
                a=min(A[2*mid-i],r-i) if r>i else 0
                while i-a>=0 and i+a<n-1 and ss[i-a-1]==ss[i+a+1]:
                    a+=1
                    B[i+a]=max(B[i+a],a*2+1)
                A.append(a)
                if i+a>r:
                    mid,r=i,i+a
                
            return B 
        
        if s=="":
            return ""
        B=[(b+1)//2 for b in manacher(s)[1::2]]
        for i in range(len(B)-1,-1,-1):
            if B[i]==i+1:
                return s[i+1:][::-1]+s