class UndergroundSystem:

    def __init__(self):
        self.travel_times = {}
        self.check_ins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins.pop(id)
        travel = (start_station, stationName)
        travel_time = t - check_in_time

        if travel in self.travel_times: self.travel_times[travel].append(travel_time)
        else: self.travel_times[travel] = [travel_time]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation,endStation)
        avg = 0 
        for i in self.travel_times[travel]: avg += i
        avg /= len(self.travel_times[travel])
        return avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)