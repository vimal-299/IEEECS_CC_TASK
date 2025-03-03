class intervalmerger:
    def __init__(self):
        self.intervals = []  # Creates a list to store intervals

    def addIntervals(self,start,end):
        self.intervals.append([start,end])  # Adds the given interval to the list 
        self.intervals.sort()  # Sorts the intevals in ascending order based on their start values
        length = len(self.intervals)
        for i in range(length-1):
            dis = len(self.intervals)
            if dis>1:
                if self.intervals[0][1]<self.intervals[1][0] :
                    continue
                else :
                    # Creates a merged interval with min start value and max end value
                    merged =[]
                    merged.append(min(self.intervals[0][0],self.intervals[1][0]))
                    merged.append(max(self.intervals[0][1],self.intervals[1][1]))

                    # Replaces the intervals with the merged interval
                    self.intervals.pop(0)
                    self.intervals.pop(0)
                    self.intervals.insert(0,merged)

    def getIntervals(self):
        print(self.intervals) # Prints the intervals
