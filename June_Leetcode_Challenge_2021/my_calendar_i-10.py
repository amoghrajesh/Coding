class MyCalendar:

    def __init__(self):
        self.events = []
        

    def book(self, start: int, end: int) -> bool:
        for i in self.events:
            s, e = i
            if max(s, start) < min(e, end):
                return False
        self.events.append([start, end])
        return True
            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
