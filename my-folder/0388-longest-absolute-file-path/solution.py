class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depth = 0
        longest = 0
        map_ = {0:0}
        
        levels = input.split("\n")
        
        for level in levels:
            name = level.lstrip('\t')
            depth = len(level) - len(name)
            
            if "." in name:
                longest = max(longest, map_[depth] + len(name))
            else:
                map_[depth+1] = map_[depth] + len(name) + 1
        return longest
