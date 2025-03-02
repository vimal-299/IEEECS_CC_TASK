class intervalmerger:
    def __init__(self):
        self.intervals = []
    def addIntervals(self,start,end):
        self.intervals.append([start,end])
        self.intervals.sort()
        length = len(self.intervals)
        for i in range(length-1):
            dis = len(self.intervals)
            if dis>1:
                if self.intervals[0][1]<self.intervals[1][0] :
                    continue
                else :
                    merged =[]
                    merged.append(min(self.intervals[0][0],self.intervals[1][0]))
                    merged.append(max(self.intervals[0][1],self.intervals[1][1]))
                    self.intervals.pop(0)
                    self.intervals.pop(0)
                    self.intervals.insert(0,merged)
    def getIntervals(self):
        print(self.intervals)
