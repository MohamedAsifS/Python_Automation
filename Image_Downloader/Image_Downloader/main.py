import requests,bs4


# get_the_link=input("Enter The Word : ")

def get_the_page(get_the_link):
    actual_link=f"https://www.google.com//images?q={get_the_link}"
    
    get_respose=requests.get(actual_link)
    
    return get_respose.content

beauty=bs4.BeautifulSoup(get_the_page("virat kholi"),'lxml')

img=beauty.find_all('img')

for i in img:
    if i['alt']=='Google':
        pass
    else:
      img_link=requests.get(i['src'])
      if img_link.status_code==200:
        f=open("dhoni1.jpg",'wb')
        f.write(img_link.content)
        f.close()
       
    

# print(get_the_page("cat"))

# to download image

# print(img_link.content)->in image.content  method has bianary of an contents



    
    
    









