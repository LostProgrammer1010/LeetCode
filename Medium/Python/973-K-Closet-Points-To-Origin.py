def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        closet_points = []

        if k == len(points):
            return points

        largest = 0
        distance = sorted([(points[i][0]**2 + points[i][1]**2, points[i]) for i in range(len(points))])

        for i in range(k):
            closet_points.append(distance[i][1])

        return closet_points
