import os

def make_folder(folder_name):
    os.system("mkdir \"..\Data\solutions\\"+folder_name+"\"")

def file_read():
    with open("..\\Data\\student_data.csv") as file:
        data=file.read()
        data=data.splitlines()

        final_list=[]

        for i in data:
            final_list.append(i.split(","))
        
        return final_list

def get_code(project_name,data):
    url="git clone https://github.com/"
    os.chdir("..\\Data\\solutions\\"+project_name)

    for i in data:
        os.mkdir(i[2])
        os.chdir(i[2])
        print("started"+i[2])
        os.system(url+i[2]+"/"+project_name)
        os.chdir("..")
    
    os.chdir("..\\..\\..\\code")

