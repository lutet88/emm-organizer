"""
# database.py
# github.com/lutet88
#
# json handler.
#
"""

import json
import os.path
import random

testing_names = ["apple", "banana", "carrot", "dog", "elephant", "fish", "giraffe", "hedgehog", "igloo", "japan", "korea", "liechtenstein", "mongolia", "noose", "oval", "pig", "query", "raster", "stupid", "turtle", "universe", "violin", "wallaby", "yak", "zebra"]

class Database:
    def __init__(self, filename, testing=False):
        self.filename = filename
        if os.path.isfile(filename):
            # file exists
            f = open(filename)
            data = "".join(f.readlines())
            f.close()
            self.data = json.loads(data)
        else:
            f = open(filename, "w+")
            f.write("")
            f.close()
            self.data = self.__createDatabase(testing)
            self.__dumpJSON()
            
        
    def __createDatabase(self, testing=False):
        data = [{} for x in range(20)]
        for x in range(20):
            if testing:
                data[x]["name"] = testing_names[x]
                data[x]["quantity"] = random.randint(0, 10)
                data[x]["maximum"] = data[x]["quantity"] + random.randint(0, 10)
                data[x]["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            else:
                data[x]["name"] = ""
                data[x]["quantity"] = 0
                data[x]["maximum"] = 10
                data[x]["color"] = (166, 166, 166)
        return data

    
    def __dumpJSON(self):
        f = open(self.filename, "w+")
        f.writelines(json.dumps(self.data))
        f.close()
    
    
    def setName(self, id, name):
        self.data[id]["name"] = name
        self.__dumpJSON()
        
    def setMaximum(self, id, mx):
        self.data[id]["maximum"] = mx
        self.__dumpJSON()
    
    def setQuantity(self, id, qty):
        self.data[id]["quantity"] = qty
        self.__dumpJSON()
    
    def changeQuantity(self, id, change):
        self.data[id]["quantity"] += change
        self.__dumpJSON()
    
    def setColor(self, id, r, g, b):
        self.data[id]["color"] = (r, g, b)
        self.__dumpJSON()
        
    def setAttribute(self, id, name, value):
        self.data[id][name] = value
        self.__dumpJSON()
        
    def getQuantity(self, id):
        return self.data[id]["quantity"]
    
    def getMaximum(self, id):
        return self.data[id]["maximum"]
    
    def getName(self, id):
        return self.data[id]["name"]
    
    def getColor(self, id):
        return self.data[id]["color"]
        
    def __del__(self):
        self.__dumpJSON()

