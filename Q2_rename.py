import os 
def file_name():
    files_list = os.listdir(r"C:\Users\pb9536\Desktop\Hyd Web Dev\Udacity\Lesson 4\prank1")
    print (files_list)
    path = os.getcwd()
    print path
    os.chdir(r"C:\Users\pb9536\Desktop\Hyd Web Dev\Udacity\Lesson 4\prank1")
    os.rename("sunny.txt","newfile.txt")

file_name()
