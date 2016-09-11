from __builtin__ import str
from dask.array.creation import arange

class lib:
    def get_str_first_value(self, Param):
        List  = str(Param).split()
        #print List
        for i in range(len(List)):
            #print List(i)
            try:
                number = float(str(List[i]))
                return number
            except ValueError:
                None
                  
            try:
                number = int(str(List[i]))
                return number
            except ValueError:
                None