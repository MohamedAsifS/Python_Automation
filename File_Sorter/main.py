import os
import shutil

def folder_path(path):
    log=[]
    subfolder_checker=[]
    for folder,subfolder,files in os.walk(path):
      main_Path=path
      if subfolder:
        for i in subfolder:
            subfolder_checker.append(i.lower())
      if files:
          for i in files:
              if i.split('.')[1].lower() in subfolder_checker:
                  shutil.move(folder+"\\"+i,folder+"\\"+i.split('.')[1].lower()) 
                  log.append(i.split('.')[1].lower())
              else:
                  os.mkdir(main_Path+"\\"+i.split('.')[1].lower())
                  shutil.move(folder+"\\"+i,main_Path+"\\"+i.split('.')[1].lower()+i)
                  log.append(i.split('.')[1].lower())
                  subfolder_checker.append(i.split('.')[1].lower())
                  
            
           
                
            
               
    
            
                
                
folder_path("C:\\Users\\JOVE\\Music\\test")




       
