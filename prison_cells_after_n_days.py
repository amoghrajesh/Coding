def prisonAfterNDays(cells, N):
    def change(cells, n):
        ans = [0]*8
        while n>0:
            n-=1
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    ans[i] = 1
                else:
                    ans[i] = 0
        cells = ans
        return cells
    cells = change(cells,1)
    N = (N - 1) % 14
    cells = change(cells, N)
    print(cells)

cells = [0,1,0,1,1,0,0,1]
N = 7
prisonAfterNDays(cells, N)
