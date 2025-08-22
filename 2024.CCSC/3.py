class Town:
    def __init__(self, numPaths):
        self.paths = [False for _ in range(numPaths)]
    def add(self, path):
        self.paths[path - 1] = True


def dfs(seen, towns, currTown):
    if seen[currTown - 1]:
        return False
    elif towns[currTown - 1].paths == []:
        return True
    else:
        for path in towns[currTown - 1].paths:
            seen[path - 1] = True
            return dfs(seen, towns, path)

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        towns = [Town(m) for _ in range (n)]
        for _ in range(m):
            ni, mi = map(int, input().split())
            towns[ni - 1].add(mi)
            
        cycle = False
        for town in range(n):
            cycle = dfs([False for i in range(m)], towns, town)
            if cycle:
                print('YES')
                exit()
    print('NO')

