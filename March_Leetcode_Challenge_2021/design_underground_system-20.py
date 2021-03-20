class UndergroundSystem:

    def __init__(self):
        self.travelDetails = dict()
        self.avgDetails = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.travelDetails:
            self.travelDetails[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        p = self.travelDetails.get(id)
        self.travelDetails.pop(id)
        key = (p[0], stationName)
        if key in self.avgDetails:
            self.avgDetails[key] = (self.avgDetails[key][0] + t - p[1], self.avgDetails[key][1] + 1)
        else:
            self.avgDetails[key] = (t - p[1], 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        s, n = self.avgDetails[key]
        return s / (n * 1.0)
