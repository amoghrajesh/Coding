
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.N = len(rects)
        self.areas = [0]*self.N
        for i in range(self.N):
            x1, y1, x2, y2 = self.rects[i]
            self.areas[i] = (y2+1-y1)*(x2+1-x1)
        

    def pick(self) -> List[int]:
        if not self.rects:
            return []
        i = random.choices(range(self.N), weights = self.areas)[0]
        rect = self.rects[i]
        return self.get_point(*rect)

    def get_point(self, x1, y1, x2, y2):
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x,y]