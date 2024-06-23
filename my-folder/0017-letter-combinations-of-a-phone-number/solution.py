class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        ret, sol = [],[]

        letters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        def recursive(i=0):
            if len(sol) == len(digits):
                ret.append(''.join(sol[:]))
                return

            for num in letters[int(digits[i])]:
                sol.append(num)
                recursive(i+1)
                sol.pop()
        
        recursive(0)
        return ret

