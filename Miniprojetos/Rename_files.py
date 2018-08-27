import os
def rename_files ():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Felipe\Desktop\UDACITY\Projetos\Projeto04_smoviesite\rename_file")
    print file_list
    saved_path = os.getcwd()
    print "Current Working Directory is" + saved_path
    os.chdir(r"C:\Users\Felipe\Desktop\UDACITY\Projetos\Projeto04_smoviesite\rename_file")
    #(2) for each file, rename filename
    for filename in file_list:
        os.rename(filename,filename.translate(None, "0,1,2,3,4,5,6,7,8,9"))
    os.chdir (saved_path)
rename_files()
