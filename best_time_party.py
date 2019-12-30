from collections import defaultdict



class Point:

    def __init__(self,hour:int,start:bool,weight=0):
        self.hour = hour
        self.start = start
        self.weight = 0
    
        
    def __lt__(self,other):
        if isinstance(other,Point):
            return self.hour < other.hour
    

    def __repr__(self):
        return f"Point({self.hour},{self.start})"


def best_time_to_party(schedule,start_time,end_time):

    points = []
    for start,end in schedule:
        points.append(Point(start,True))
        points.append(Point(end,False))

    points.sort() 
    max_count = float("-inf")
    max_hour = None
    count = 0

    for point in points:
        if point.hour >= end_time:
            break
        if point.start:
            count += 1 # point.weight
            if point.hour >= start_time:
                if count > max_count:
                    max_count = count
                    max_hour = point.hour
        else:
            count -= 1 #point.weight

    return max_count    
#    return max_hour,max_count

def best_time_to_party_alternate(schedule):
    counts = defaultdict(int)
    for interval in schedule:
        if interval in counts:
            continue
        start_time = interval[0]
        for other_interval in schedule:
            if other_interval == interval:
                continue
            if other_interval[0] <= start_time < other_interval[1]:
                counts[interval] += 1
    
    return max(counts.keys(),key=lambda x:counts[x])[0]
if __name__ == "__main__":

    sched = [(6,8),(6,12),(6,7),(7,8),(7,10),(8,9),(8,10),(9,12),(9,10),(10,11),(10,12),(11,12)]

    print(best_time_to_party_alternate(sched))




