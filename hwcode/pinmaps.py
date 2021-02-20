# this is literally just our pinmaps.
# literally just use it as a pinmap something like
# 
# import pinmaps
# mapper = pinmaps.get_pinmapper()

from hwcode.PinMapper import PinMapper

def get_pinmapper():
    pm = PinMapper((5, 4))
    pm.createPinMap(0, 1, 3)
    pm.createPinMap(1, 2, 3)
    pm.createPinMap(2, 2, 1)
    pm.createPinMap(3, 2, 2)
    pm.createPinMap(4, 1, 2)
    pm.createPinMap(5, 0, 0)
    pm.createPinMap(6, 1, 1)
    pm.createPinMap(7, 1, 0)
    pm.createPinMap(8, 2, 0)
    pm.createPinMap(9, 3, 0)
    pm.createPinMap(10, 4, 0)
    pm.createPinMap(11, 4, 1)
    pm.createPinMap(12, 4, 2)
    pm.createPinMap(13, 0, 2)
    pm.createPinMap(14, 0, 1)
    pm.createPinMap(15, 0, 3)
    pm.createPinMap(16, 3, 1)
    pm.createPinMap(17, 4, 3)
    pm.createPinMap(18, 3, 2)
    pm.createPinMap(19, 3, 3)
    return pm
    
    
    
    
    
