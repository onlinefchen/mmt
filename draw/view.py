import matplotlib.pyplot as plt
import numpy as np
from pc import windows
import datetime
class data:
    data_number = []
    data_name = ""
    
class view:
    array_orig = []
    array_new = []
    array_three = []
    
    
    def init_array(self, param_file, param_array):
        file = open(param_file, "a+")
        print param_file
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
        
    def draw_compare_figure(self, Param1, Param2, Param3, imagename = None):
        local_view = view()
        local_windows = windows()
        local_view.init_array(Param1, view.array_orig)
        local_view.init_array(Param2, view.array_new)
        if (len(Param3)):
            local_view.init_array(Param3, view.array_three)
        width = 2
        length = len(view.array_orig)
        fig = plt.figure(figsize =(width * 7, length * 4) , dpi = 300)
        for i in range(len(view.array_orig)):
            plt.subplot(len(view.array_orig), 2, i + 1)
            x = np.arange(len(view.array_orig[i].data_number))
            y1 = view.array_orig[i].data_number
            y2 = view.array_new[i].data_number
            if (len(Param3)):
                y3 = view.array_three[i].data_number
            line_param1 = plt.plot(x, y1, label = Param1, color = "b")
            line_param2 = plt.plot(x, y2, label = Param2, color = "r")
            if (len(Param3)):
                line_param3 = plt.plot(x, y3, label = Param3, color = "g")
            plt.title(view.array_new[i].data_name,loc='left')
            #plt.legend()
            plt.subplots_adjust(hspace=1,top=2)
            plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), borderaxespad=0.)

        
        #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0, rect=[0, 0, 0.5, 1])
        plt.tight_layout(pad=0.4, w_pad=1, h_pad=2)
        fig.legend((line_param1, line_param2), ('Line 3', 'Line 4'), 'upper right')
        if imagename is None:
            now = datetime.datetime.now().strftime('%H-%M-%S')
            plt.savefig("result.png", dpi = 70)
        else:
            plt.savefig(imagename, dpi = 70)
        plt.show()

            
        
# if __name__ == '__main__':
#     local_view = view()
#     local_view.draw_single_figure("orig")
#     local_view.draw_compare_figure("new.txt", "orig.txt" , "")
#draw_figure(array_x1, array_y2, 2, y_label, "graph2", 1)
#draw_figure(array_x1, array_y2, 3, y_label, "graph3", 2)
