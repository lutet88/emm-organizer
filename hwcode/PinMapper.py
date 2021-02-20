"""
# PinMapper.py
# github.com/lutet88
# 
# simple library that creates pin definitions three ways:
# 2D grid, ID, and actual value
"""

class PinMapper:
    def __init__(self, d2dsize):
        self.idCount = 0
        self.pinmaps = {}
        self.d2d = [[None for y in range(d2dsize[1])] for x in range(d2dsize[0])]

    def add_to_map(self, id, child):
        self.pinmaps[id] = child

    def setd2d(self, x, y, child):
        self.d2d[x][y] = child

    def nextid(self):
        self.idCount += 1
        return self.idCount - 1

    def getMapById(self, id):
        return self.pinmaps[id]

    def getMapBy2D(self, x, y):
        return self.d2d[x][y]

    def createPinMap(self, actual_value, x, y):
        PinMap(actual_value, x, y, self)

    def getMapByValue(self, value):
        for m in pinmaps:
            if pinmaps[m].value == value:
                return pinmaps[m]

    def getMapBy2DIndex(self, idx):
        return self.d2d[idx // 4][idx % 4]
    
class PinMap:
    def __init__(self, actual_value, x, y, mapper):
        self.value = actual_value
        self.d2d = (x, y)
        self.id = mapper.nextid()
        mapper.add_to_map(self.id, self)
        mapper.setd2d(x, y, self)

    def getd2d(self):
        return self.d2d

    def getid(self):
        return self.id

    
