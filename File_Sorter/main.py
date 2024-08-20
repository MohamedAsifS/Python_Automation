import os
import shutil


LOG=[]
def folder_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The folder {path} does not exist.")
    
    subfolder_checker=[]
    
    for folder,subfolder,files in os.walk(path):
           for sub in subfolder:
               subfolder_checker.append(sub.lower())
           break
    LOG=subfolder_checker.copy()
    print(LOG)
       
   
    
    
    for folder,subfolder,files in os.walk(path):
      main_Path=path
      
      
      if files:
          for i in files:
               count=0
               if i.split('.')[1].lower() in subfolder_checker:
                  temp=i.split('.')[1].lower()
                  
                  
                  if folder+"\\" !=main_Path+"\\"+i.split('.')[1].lower()+"\\":
                     shutil.move(folder+"\\"+i,main_Path+"\\"+i.split('.')[1].lower()+"\\") 
                     
                    
                    
               else:
                  os.mkdir(main_Path+"\\"+i.split('.')[1].lower())
                  shutil.move(folder+"\\"+i,main_Path+"\\"+i.split('.')[1].lower()+"\\")
                  temp=i.split('.')[1].lower()
                  subfolder_checker.append(temp)
                  
                  LOG.append(temp)
    print(LOG,subfolder_checker)

# def delete_folder(path):
#     if not os.path.exists(path):
#         raise FileNotFoundError(f"The folder {path} does not exist.")
#     log=[]
#     for files,sub_folder,folder in  os.walk(path):
                
#                     for i in sub_folder:
                         
            
        
    
    
   
    
                  
            
           
                
            
               
    
            
                
                
folder_path("C:\\Users\\JOVE\\Music\\test")
# delete_empty("C:\\Users\\JOVE\\Music\\test")




       
