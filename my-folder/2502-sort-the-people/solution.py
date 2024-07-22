class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = []
        for i in range(len(names)):
            lst.append((heights[i],names[i]))
        lst.sort()
        for i in range(len(names)):
            names[i] = lst[i][1]
        names.reverse()
        return names
