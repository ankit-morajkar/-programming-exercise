class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        N = max(len(s), len(t))
        sstack = []
        tstack = []
        
        for i in range(N):
            try:
                si = s[i]
            except:
                si = ''
            try:
                ti = t[i]
            except:
                ti = ''
                
            if si == "#":
                if len(sstack)>0:
                    sstack.pop()
            if ti == "#":
                if len(tstack)>0:
                    tstack.pop()
            if si != '' and si != '#':
                sstack.append(si)
            if ti != '' and ti != '#':
                tstack.append(ti)
                    
            print(si, ti, sstack, tstack)
                    
        if sstack == tstack:
            return True
        else:
            return False
            
        