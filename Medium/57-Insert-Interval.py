def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        no_overlaps = []
        start = -1
        end = -1

        if not intervals:
            return [new_interval]

        for i in intervals:
            if i[1] < new_interval[0]:
                            no_overlaps.append(i)
                        elif i[0] > new_interval[1]:
                            if [start, end] not in no_overlaps and start != -1 and end != -1:
                                no_overlaps.append([start, end])
                            no_overlaps.append(i)
                        else:
                            if start == -1:
                                if i[0] <= new_interval[0]:
                                    start = i[0]
                                elif i[0] > new_interval[0]:
                                    start = new_interval[0]
                            if end == -1:
                                if i[1] >= new_interval[1]:
                                    end = i[1]
                                elif i[1] < new_interval[1]:
                                    end = new_interval[1]
                                if end < i[1]:
                                    end = i[1]

        if [start, end] not in no_overlaps and start != -1 and end != -1:
                                no_overlaps.append([start, end])

        if start == -1 and end == -1:
            if new_interval[0] < intervals[0][0]:
                no_overlaps.insert(0,new_interval)
            else:
                no_overlaps.append(new_interval)
        return sorted(no_overlaps)
