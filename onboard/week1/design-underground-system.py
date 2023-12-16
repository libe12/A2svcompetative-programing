class UndergroundSystem:

    def __init__(self):
        
        self.tupple=defaultdict(tuple)
        self.lists=defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.tupple[id]=(t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime,startstation=self.tupple[id]
        total=t-starttime
        self.lists[(startstation,stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.lists[(startStation,endStation)])/len(self.lists[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)