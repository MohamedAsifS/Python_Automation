import os
import shutil

def folder_path(path):
    log=[]
    for folder,subfolder,files in os.walk(path):
         for sub in subfolder:
            print(sub)
            if files and sub not in log:
                for file_name in files:
                    spliter=file_name.split('.')
                    print(log)
                    if spliter[1] not in log:
                        os.mkdir(path+"\\"+spliter[1])
                        shutil.move(folder+"\\"+files[0],path+"\\"+spliter[1])
                        log.append(spliter[1].upper)
                    else:
                        shutil.move(folder+"\\"+files[0],path+"\\"+spliter[1])
    # for folder,subfolder,files in os.walk(path):
    #     if subfolder[0] not in log:
    #         os.rmdir(path+"\\"+subfolder[0])
    
            
                
                
folder_path("C:\\Users\\JOVE\\OneDrive\\Documents\\WORKSPACE\\python\\PROJECTS\\File_Sorter\\test")

       
