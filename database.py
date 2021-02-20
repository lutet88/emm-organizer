"""
# database.py
# github.com/lutet88
#
# json handler.
#
"""

import json
import os.path

class Database:
    def __init__(self, filename):
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
            self.data = self.__createDatabase()
            self.__dumpJSON()
        
        
    def __createDatabase(self):
        data = [{} for x in range(20)]
        for x in range(20):
            data[x]["name"] = ""
            data[x]["quantity"] = 0
            data[x]["color"] = (0, 15, 0)
        return data

    
    def __dumpJSON(self):
        f = open(self.filename, "w+")
        f.writelines(json.dumps(self.data))
        f.close()
    
    
    def setName(self, id, name):
        self.data[id]["name"] = name
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
        
    def __del__(self):
        self.__dumpJSON()

