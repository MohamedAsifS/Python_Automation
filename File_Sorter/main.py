import os
import shutil
import send2trash



LOG=[]
subfolder_checker=[]
def folder_path(path):
    path=rf"{path}"
    if not os.path.exists(path):
        raise FileNotFoundError(f"The folder {path} does not exist.")
    
    
    
    for folder,subfolder,files in os.walk(path):
           for sub in subfolder:
               subfolder_checker.append(sub.lower())
           break
   
    
       
   
    
    
    for folder,subfolder,files in os.walk(path):
      main_Path=path
      
      
      
      if files:
          for i in files:  
               count=0
               if i.split('.')[-1].lower() in subfolder_checker:
                    temp=i.split('.')[-1].lower()
                    LOG.append(temp)
                  
                    # if folder+"\\"+i == main_Path+"\\"+i.split('.')[-1].lower()+"\\"+i:
                    #       count+=1
                    #       os.rename(folder+"\\"+i,"a"+i)
                    #       shutil.move(folder+"\\"+("a"+i),main_Path+"\\"+i.split('.')[-1].lower()+"\\")
                      
                  
                  
                    if folder+"\\" !=main_Path+"\\"+i.split('.')[-1].lower()+"\\":
                         shutil.move(folder+"\\"+i,main_Path+"\\"+i.split('.')[-1].lower()+"\\") 
                     
                    
                    
               else:
                  os.mkdir(main_Path+"\\"+i.split('.')[-1].lower())
                  shutil.move(folder+"\\"+i,main_Path+"\\"+i.split('.')[-1].lower()+"\\")
                  temp=i.split('.')[-1].lower()
                  subfolder_checker.append(temp)
                  LOG.append(temp)
                  
                  
   

def delete_folder(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The folder {path} does not exist.")
    box=set(LOG)
    deleter=[]
    
    for i in subfolder_checker:
        if i not in box:
            deleter.append(i)
    
    
            
    
    
    for folder,subfolder,files in  os.walk(path):
                
            for i in subfolder:
                if i in deleter:
                    send2trash.send2trash(folder+"\\"+i)
                    print(f"Deleted folder {folder}\\{i}")
                    subfolder_checker.remove(i)
                         
            
        
    
    
   
    
                  
            
           
                
            
               
    
            
                
                
folder_path("C:\Users\JOVE\Music\test")
delete_folder("C:\\Users\\JOVE\\Music\\test")




       
