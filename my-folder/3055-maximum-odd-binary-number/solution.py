class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count0 = s.count('0')
        count1 = len(s) - count0
        return '1' * (count1 - 1) + '0' * count0 + '1'
    
