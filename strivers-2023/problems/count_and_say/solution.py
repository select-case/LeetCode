class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'
        for i in range(n-1):
            string = ''.join(f'{sum(1 for _ in gr)}{key}' for key, gr in groupby(string))
        return string