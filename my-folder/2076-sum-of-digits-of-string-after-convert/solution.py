class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_s = ""
        for i in s:
            num_s += str(ord(i) - ord('a') + 1)
        print(num_s)
        for i in range(k):
            if len(num_s) == 1: return int(num_s)
            new_num_s = 0
            for i in num_s:
                new_num_s += int(i)
            num_s = str(new_num_s)

        return int(num_s)
