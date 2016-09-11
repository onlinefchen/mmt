import os
class linux:
    
    def cmd(self, Param):
        list = os.popen(Param).readlines()
        for line in list:
            line.strip("\n")
            line.strip("\r")
        
        #print len(list)
        return list