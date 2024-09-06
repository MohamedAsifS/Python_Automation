import requests,bs4,os


# get_the_link=input("Enter The Word : ")

def get_the_Search(Asif):
    cse_id="605b2f7696f594e3b"
    api_key="AIzaSyDlOgaAGZX2bN1jUP99dpNceTbIh_wV_lY" 
    
    url = f"https://www.googleapis.com/customsearch/v1?q={Asif} animal&num=10&start=1&imgSize=huge&searchType=image&key={api_key}&cx={cse_id}" 
    
    response=requests.get(url) 
    get_json=response.json()
    get_link=get_json['items'][3]['link']
    
    print(get_link)
     
    
def get_path_save_file(path,file_name):
    os.mkdir(path+"\\"+file_name)

get_the_Search("cat")





# beauty=bs4.BeautifulSoup(get_the_page("virat kholi"),'lxml')

# img=beauty.find_all('img')

# for i in img:
#     if i['alt']=='Google':
#         pass
#     else:
#       img_link=requests.get(i['src'])
#       if img_link.status_code==200:
#         f=open("dhoni1.jpg",'wb')
#         f.write(img_link.content)
#         f.close()


    
    
    
    

# print(get_the_page("cat"))
# get_path_save_file("C:\\Users\\JOVE\\OneDrive\\Documents\\WORKSPACE\\python\\PROJECTS\\Image_Downloader\\Image_Downloader","cat")
# to download image

# print(img_link.content)->in image.content  method has bianary of an contents



    
    
    









