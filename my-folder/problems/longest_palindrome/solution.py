class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_index = {}
        for i in s:
            if i not in dict_index:
                dict_index[i] = 1
            else: dict_index[i] += 1
        count = 0
        for i in dict_index:
            if dict_index[i]%2 == 0:
                count += dict_index[i]
                dict_index[i] = 0
            else:
                count += dict_index[i]
                count -= 1
                dict_index[i] = 1
        for i in dict_index:
            if dict_index[i] == 1:
                count += 1
                dict_index[i] -= 1
                break
        return count