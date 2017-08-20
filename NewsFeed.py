# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:30:35 2017

@author: vignesht
"""

#IMPORT THE PACKAGES
import requests
import pandas as pd
import json
pd.set_option('display.max_colwidth', 200)


#Api connecting with pocet for news feed
auth_params = {'consumer_key':'68152-f3fce122267d8d0f3ae4051a','redirect_uri':'https://twitter.com/packtsandhyo'}
tkn = request.post('https://getpocket.com/v3/oauth/request',data = auth_params)
tkn.content

#consumer key user  authentication
usr_params = {'consumer_key':'68152-f3fce122267d8d0f3ae4051a','code':'14fbe71-51bd-960f-5ad1-2183e3'}
usr = requests.post('https://getpocket.com/v3/oauth/request',data = usr_params)
usr.content

#Access token
no_params = {'consumer_key':'68152-f3fce122267d8d0f3ae4051a','access_token':'871e6e46-d047-2fd3-79a8-01a1a4','tag':'n'}
no_result = request.postr('https://getpocket.com/v3/get',data = no_params)
no_result.text

#Laod json data and append in list
no_jf = json.loads(no_result.text)
no_jd = no_jf['list']
no_urls=[]
for i in no_jd.values():
    no_urls.append(i.get('resloved_url'))
no_urls


#Convert list into dataframe which has two colums one is website and whether we are intrested to read or not
#NO data
no_uf = pd.DataFrame(no_urls,columns=['urls'])
no_uf = no_uf.assign(wanted = lambda x:'n')
no_uf

#Access token
yes_params = {'consumer_key':'68152-f3fce122267d8d0f3ae4051a','access_token':'871e6e46-d047-2fd3-79a8-01a1a4','tag':'y'}
yes_result = request.postr('https://getpocket.com/v3/get',data = no_params)
yes_result.text

#Laod json data and append in list
yes_jf = json.loads(yes_result.text)
yes_jd = no_jf['list']
yes_urls=[]
for i in yes_jd.values():
    yes_urls.append(i.get('resloved_url'))
yes_urls


#Convert list into dataframe which has two colums one is website and whether we are intrested to read or not
#NO data
yes_uf = pd.DataFrame(yes_urls,columns=['urls'])
yes_uf = no_uf.assign(wanted = lambda x:'n')
yes_uf

#yes data frame
yes_uf = pd.DataFrame(no_urls,columns=['urls'])
yes_uf = no_uf.assign(wanted = lambda x:'n')
yes_uf

#Concat both yes and no data for preperation of model
df = pd.concat([yes_uf,no_uf])
df.dropna(inplace=1)
df

#Using the embed.ly API to download story bodies
import urllib
def get_html(x):
    qurl = urllib.parse.quote(x)
    rhtml=requests.get('https://api.embedly.com/1/extract?url=' + qurl +'&key=some_api_key')
    ctnt=json.loads(rhtml.text).get('content')
    return ctnt
    df.loc[:,'html'] = df['urls'].map(get_html)
    df.dropna(inplace=1)
    df


#Improt beautiful soup package
from bs4 import BeautifulSoup
def get_text(x):
    soup = BeautifulSoup(x,'lxml')
    text = soup.get_text()
    return text
    zf.loc[:,'text'] = zf['html'].map(get_text)
    zf


#Natural Langauage processing 
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(ngram_range = (1,3),stop_words = 'english',min_df=3)
tv = vect.fit_transform(df['text'])

#Apply svm on the data
from sklearn.svm import LinearSVC
clf = LinearSVC
model = clf.fit(tv,df['wanted'])

#Integration with feeds,google sheets and email
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\Vignesh\Downloads\My Project-1cdc0bbf95f6.json',scope)
gc = gspread.authorize(credentials)


ws = gc.open("NewStories")
sh = ws.shhet1
zd = list(zip(sh.col_values(2),sh.col_values(3),sh.col_values(4)))
zf = pd.DataFrame(zd,columns=['title','urls','html'])
zf.replace('',pd.np.nan,inplace=True)
zf


#Transforming data
zf.loc[:,'text'] = zf['html'].map(get_text) 
zf.reset_index(drop = True,inplace=True)
test_matrix = vect.transform(zf['text'])
test_matrix

#store the result in data frame
results = pd.DataFrame(model.predict(test_matrix),columns=['wanted'])


#Merge the data
rez = pd.merge(results,zf,left_index = True,right_index = True)
rez


#change to yes and no 
change_to_no = [130,145,148,163,178,199,219,222,223,226,235,279,348,357,427,440,542,544,546]
change_to_yes = [0,9,29,35,42,71,110,190,319,335,344,371,385,399,408,409,422,472,520,534]

for i in rez.iloc[chenge_to_yes].index:
    rez.iloc[i]['wanted'] = 'y'
for i in rez.iloc[chenge_to_no].index:
    rez.iloc[i]['wamted'] = 'n'
rez

comdined = pd.concat([df[['wanted','text']],rez[['wanted','text']]])
combined


#FIt the data in model
tvcomb = vect.fit_transform(combined['text'], combined['wanted'])
model = clf.fit(tvcomb,combined['wanted'])

#import the pickel
import pickle
pickle.dump(model,open(r'C:\Users\vignesht\news_model_pickle.p','wb'))
pickle.dump (vect,open(r'C:\Users\vignesht\news_model_pickle.p','wb'))


#create a function to fetch news and show in mail as impotant news
def ftech_news():
    try:
        vect = pickle.load(model,open(r'C:\Users\vignesht\news_model_pickle.p','wb'))
        model = pickle.load (vect,open(r'C:\Users\vignesht\news_model_pickle.p','wb'))
 
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\vignesht\downlaods\myproject)
        gc  = gspread.authorize(credentials)
        
        ws=gc.open("NewStories")
        sh = ws.sheet1
        zd = list(zip(sh.col_values(2),sh.col_values(3),sh.col_values(4)))
        zf = pd.DataFrame(zd,columns = ['title''urls','html'])
        zf.replace('',pd.np.nam,inplace = True)
        zf.dropna(inplace = True)
        
        def get_text(x):
            soup = BeautifulSoup(x,'lxml')
            text = soup.get_text()
            return text
    zf.loc[:,'text'] = zf['html'].map(get_text)
    
    tv = vect.fit_transform(df['text'])
    res = model.predictor(tv)
    
    rf = pd.DataFrame(res,columns = ['wanted'])
    rez = pd.merge(rf,zf,left_index=True,right_index=True)
    
    news_str = ''
    for t,u in zip(rez[rez['wanted']=='y']['title'],rez[rez['wanted']=='y']['urls']):
        news_str = news_str +t + '\n' +u + '\n'
        
    payload = {"value1" : news_str}
    r = requests.post('https://maker.ifttt.com/trigger/news_event/with/key/cZjkYp5rzvtZubasgskdhi',data = payload)
    
    #clean up worksheet
    lenv = len(sh.col_values(1))
    cell_list = sh.range('A1:F' + str(lenv))
    for cell in cell_list:
        cell.value = ""
    sh.update_cells(cell_list)
    
    print(r.text)
    
  except:
      print('Failed')

schedule.every(60).minutes.do(fetch_news)

while 1: