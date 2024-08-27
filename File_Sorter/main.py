import os
import shutil
import send2trash

LOG = []

subfolder_checker = []


def folder_path(path):
    """handle a folder path
    *if extention folder is already there  it will move to those files to particular folder
    *if files has duplicate it will rename and move to those corresponding folder
    * if not it will create a new folder with extention name and it will move files to those folders
    

    Args:
        path (path): _description_

    Raises:
        FileNotFoundError: _description_
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"The folder {path} does not exist.")
    
    # To get the aprent directory folders name
    for folder, subfolder, files in os.walk(path):
        for sub in subfolder:
            subfolder_checker.append(sub.lower())
        break

    for folder, subfolder, files in os.walk(path):
        main_Path = path

        if files:

            for i in files:

                if i.split('.')[-1].lower() in subfolder_checker:

                    count = 0
                    temp = i.split('.')[-1].lower()
                    LOG.append(temp)

                    
                    # if duplicate folder this condtion will handle duplicate
                    if (os.path.exists(main_Path + "\\" + i.split(".")[-1].lower() + "\\" + i)):
                        re = str(count) + i
                        count += 1

                        
                        if folder + "\\" != main_Path + "\\" + i.split('.')[-1].lower() + "\\":
                            os.rename(folder + "\\" + i, folder + "\\" + re)
                            shutil.move(folder + "\\" + re, main_Path +
                                        "\\" + i.split('.')[-1].lower() + "\\")
                    #if not this will
                    elif folder + "\\" != main_Path + "\\" + i.split('.')[-1].lower() + "\\":
                        shutil.move(folder + "\\" + i, main_Path +
                                    "\\" + i.split('.')[-1].lower() + "\\")
                        
                #it there is not extention it will create a new folder and move the directory
                else:
                    os.mkdir(main_Path + "\\" + i.split('.')[-1].lower())
                    shutil.move(folder + "\\" + i, main_Path +
                                "\\" + i.split('.')[-1].lower() + "\\")
                    temp = i.split('.')[-1].lower()
                    subfolder_checker.append(temp)
                    LOG.append(temp)


def delete_folder(path):
    """it will delete the folder which is empty by checking intersection of log and subfolder_checker

    Args:
        path (path): _description_

    Raises:
        FileNotFoundError: _description_
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The folder {path} does not exist.")
    #log has officail files
    box = set(LOG)
    deleter = []
    
    #comparing folders
    for i in subfolder_checker:
        if i not in box:
            deleter.append(i)
    #deleteing those folder
    for folder, subfolder, files in os.walk(path):
        #this will send to the recycle bin
        for i in subfolder:
            if i in deleter:
                send2trash.send2trash(folder + "\\" + i)
                print(f"Deleted folder {folder}\\{i}")
                subfolder_checker.remove(i)


folder_path("C:\\Users\\JOVE\\Music\\test")
delete_folder("C:\\Users\\JOVE\\Music\\test")
