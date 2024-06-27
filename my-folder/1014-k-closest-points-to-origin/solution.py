class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in points:
            distance = (i[0]**2 + i[1]**2)**0.5
            i.append(distance)
        # print(points)
        points.sort(key = lambda point: point[2])
        for i in range(len(points)):
            points[i] = points[i][:-1]
        print(points)
        return points[:k]

