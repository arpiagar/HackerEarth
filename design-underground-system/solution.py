i#https://leetcode.com/problems/design-underground-system/


class UndergroundSystem:

    def __init__(self):
        self.user_map = {}
        self.station_map = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user_map[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.user_map[id]
        endStation, endTime = stationName, t
        if (startStation,endStation) in self.station_map:
            avg, count = self.station_map[(startStation,endStation)]
            new_avg =  ((avg*count) + endTime-startTime)/(count+1)
            self.station_map[(startStation,endStation)] = (new_avg, count+1)
        else:
            self.station_map[(startStation,endStation)] = (endTime-startTime, 1)
        self.user_map.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_map[(startStation,endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
