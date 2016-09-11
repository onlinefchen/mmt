import matplotlib.pyplot as plt
import numpy as np
from array import array
from dask.array.creation import arange
from linux_cmd import linux

class data:
    data_number = []
    data_name = ""
    
class view:
    array_orig = []
    array_new = []
    
    
    def init_array(self, param_file, param_array):
        file = open(param_file, "a+")
        file_fd = file.readlines()
        file.close()
        #print file_fd[0]
        for i in range(len(str(file_fd[0]).split())):
            #print str(file_fd[0]).split()[i]
            local_data = data()
            local_data.data_number = []
            if (i % 2 - 1):
                #print i
                try:
                    local_data.data_name = str(file_fd[0]).split()[i]
                except Exception , e:
                    local_data.data_name = ""
                #print local_data.data_name
                param_array.append(local_data)
        
        for i in range(len(file_fd)):
            line_list = file_fd[i].split()
            print len(line_list)
            for i in range(len(param_array)):
                #print i * 2 + 1
                #print line_list[i * 2 + 1]
                try:
                    local_number = int(line_list[i * 2 + 1])
                except Exception , e:
                    local_number = 0
                param_array[i].data_number.append(local_number)
        
        for i in range(len(param_array)):
            print param_array[i].data_number
            
    def draw_single_figure(self, Param):
        local_view = view()
        local_view.init_array(Param, view.array_orig)
        plt.figure(figsize = (12,20) , dpi = 100)
        for i in range(len(view.array_orig)):
            plt.subplot(len(view.array_orig), 2, i + 1).autoscale_view(True,True,True)
            x = np.arange(len(view.array_orig[i].data_number))
            y = view.array_orig[i].data_number
            plt.plot(x, y, label = view.array_orig[i].data_name)
        plt.show()
#     plt.savefig("test.png", dpi = 100)
        
    def draw_compare_figure(self, Param1, Param2):
        local_view = view()
        local_linux = linux()
        local_view.init_array(Param1, view.array_orig)
        local_view.init_array(Param2, view.array_new)
        width = 2
        length = len(view.array_orig)
        fig = plt.figure(figsize =(width * 7, length * 4) , dpi = 300)
        for i in range(len(view.array_orig)):
            plt.subplot(len(view.array_orig), 2, i + 1)
            x = np.arange(len(view.array_orig[i].data_number))
            y1 = view.array_orig[i].data_number
            y2 = view.array_new[i].data_number
            plt.plot(x, y1, label = Param1, color = "b")
            plt.plot(x, y2, label = Param2, color = "r")
            plt.title(view.array_new[i].data_name)
            #plt.legend()
            plt.subplots_adjust(hspace=1,top=2)
            plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), borderaxespad=0.)

        
        #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0, rect=[0, 0, 0.5, 1])
        plt.tight_layout(pad=0.4, w_pad=1, h_pad=2)
        plt.savefig("result.png", dpi = 70)
        local_linux.cmd("google-chrome ~/workspace/mmtest/result.png")
        #plt.show()
        
#         for i in range(len(list_line)):
#             tmp_data = new data()
#             tmp_data.data_name = list_line[i]
#             tmp_data.data_number = ""
            
        
# if __name__ == '__main__':
#     local_view = view()
# #     local_view.draw_single_figure("orig")
#     local_view.draw_compare_figure("orig", "new")
#draw_figure(array_x1, array_y2, 2, y_label, "graph2", 1)
#draw_figure(array_x1, array_y2, 3, y_label, "graph3", 2)
