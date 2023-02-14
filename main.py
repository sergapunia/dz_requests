import json
import requests
import pprint
def super_intelligence(powerstats,name=[]):
    #Hulk, Captain America, Thanos - intelligence
    respone= requests.get(url='https://akabab.github.io/superhero-api/api/all.json')
    all=respone.json()
    print(f'*{powerstats}* :')
    for g in name:
        for i in all:
            if i['name']==g:
                print(f"{i['name']} - {i['powerstats'][powerstats]}")
super_intelligence('intelligence',['Hulk','Captain America','Thanos'])

#token=
def headler():
    return {
        'Content-Type':'application/json',
        'Authorization':'OAuth {}'.format()#token)
    }
url='https://cloud-api.yandex.net:443/'
param='v1/disk'
#'v1/disk/resources' #'v1/disk/public/resources' #'v1/disk/trash/resources'
def files():
    url='https://cloud-api.yandex.net/v1/disk/resources/files'
    headers=headler()
    response = requests.get(url,headers=headers)
    return response.json()

def upload_file(file,path=''):
   name=file.split('/')[-1]
   url='https://cloud-api.yandex.net/v1/disk/resources/upload'
   headers=headler()
   if path!='':
       params={'path':path+'/'+name,'overwrite':'true'}
   else:
       params = {'path': name, 'overwrite': 'true'}
   response=requests.get(url,headers=headers,params=params)
   resp=response.json()
   result=resp.get('href')
   response=requests.put(result,data=open(file,'rb'))
   response.raise_for_status()
   if response.status_code==201:
       print('выполнено')
upload_file('/home/sergapunia/Рабочий стол/test.txt')