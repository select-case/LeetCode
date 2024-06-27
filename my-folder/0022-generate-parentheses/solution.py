class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def gen(left,right, s):
            if len(s) == 2*n:
                result.append(s)
            if left < n:
                gen(left + 1, right, s + '(')
            if right < left:
                gen(left, right + 1, s + ')')
        gen(0,0,'')
        
        return result
