import os
def puzzle():
    
    # 1. get file names in the folder
    
    file_list=os.listdir(r"H:\spring term 2016\python programming(oops)- Udacity\prank\prank")
    saved_path=os.getcwd()
    print saved_path
    os.chdir("H:\spring term 2016\python programming(oops)- Udacity\prank\prank")

    # 2. for each filename, rename that filename
    
    for file_name in file_list:
        print "file name: ",file_name
        print "new name: ", file_name.translate(None,"0123456789")
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    return
puzzle()
    
