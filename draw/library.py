class lib:
    
    # get first int number in a string
    # eg "adbcd 123 456" return 123
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
    
    def get_exec_time(self, Param):
        ret_list = Param.split()
        tmp_data = 0
        #print Param.split()
        for i in range(len(ret_list)):
            #print ret_list[i]
            if str(ret_list[i]).find("real") >= 0:
                    tmp_data = ret_list[i-1]
                    
        return int(float(tmp_data[2:-1]) * 1000)
