class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m = None
        for i in range(1,len(coordinates)):
            if coordinates[i][0] != coordinates[i-1][0]:
                m = (coordinates[i][1] - coordinates[i-1][1])/(coordinates[i][0] - coordinates[i-1][0])
                c = coordinates[0][1] - m*coordinates[0][0]
                break
        if m == None: return True

        for i in coordinates:
            if i[1] - m*i[0] - c == 0:
                pass
            else: return False
        return True