from linux import linux

class app:
    
    def get_app_list(self, Param):
        local_linux = linux()
        app_list = local_linux.cmd("adb shell monkey --port 1080 -v -v")
        print app_list
        #
    def lunch_app(self, appname):
        local_linux = linux()
        local_cmd = "adb shell am start %s" % (appname);
        #print local_cmd
        local_linux.cmd(local_cmd)


# if __name__ == '__main__':
#     local_app = app()
#     file_fd = open("tmp").readlines()
#     print file_fd
#     for i in range(len(file_fd)):
#         line_list = str(file_fd[i]).split()
#         #print line_list
#         appname =  str(line_list[1]) + "/" + str(line_list[0])
#         write_fd = open("./app.list", "a+")
#         write_fd.write(appname + "\n")
#         
#         #local_app.lunch_app(appname)