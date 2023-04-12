import os
import pandas as pd
import numpy as np
import re
import warnings 

def get_data(basedir = '/home/dewan/codespace/news-search/data'):
    dflist = []
    files = os.listdir(basedir)
    for fname in files:
        warnings.filterwarnings("ignore")
        if fname[-4:]=='xlsx':
            df = pd.read_excel(f'{basedir}/{fname}')
        if fname[-4:]=='csv':
            df = pd.read_csv(f'{basedir}/{fname}')
        dflist.append(df)
    result = pd.concat(dflist)
    result.drop(columns=['datetime', 'Media'], inplace=True)
    return result

#Removes Punctuations
def remove_punctuations(data):
    punct_tag=re.compile(r'[^\w\s]')
    data=punct_tag.sub(r'',data)
    return data

#Removes HTML syntaxes
def remove_html(data):
    html_tag=re.compile(r'<.*?>')
    data=html_tag.sub(r'',data)
    return data

#Removes URL data
def remove_url(data):
    url_clean= re.compile(r"https://\S+|www\.\S+")
    data=url_clean.sub(r'',data)
    return data

#Removes Emojis
def remove_emoji(data):
    emoji_clean= re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    data=emoji_clean.sub(r'',data)
    url_clean= re.compile(r"https://\S+|www\.\S+")
    data=url_clean.sub(r'',data)
    return data


def clean_feature(dataframe, featurename):
    for i in range(len(dataframe)):
        dataframe.iloc[i][featurename] = remove_punctuations(str(dataframe.iloc[i][featurename]))
        dataframe.iloc[i][featurename] = remove_html(str(dataframe.iloc[i][featurename]))
        dataframe.iloc[i][featurename] = remove_url(str(dataframe.iloc[i][featurename]))
        dataframe.iloc[i][featurename] = remove_emoji(str(dataframe.iloc[i][featurename]))

    return dataframe.reset_index(drop=True)

def calculate_TFIDF(dataframe, query, featurename='Title'):
    count_docs = 0
    for i in range(len(dataframe[featurename])):
        dt = str(dataframe.iloc[i][featurename]).lower()
        query = query.lower()
        bow = dt.split(" ")
        tfscore = dt.count(query)/len(bow)
        dataframe.at[i, 'score'] = tfscore
        if query in bow:
            count_docs+=1
    IDF = np.log(len(dataframe[featurename])/count_docs)
    dataframe['score'] = dataframe['score']*IDF
    return dataframe

def search_by_query(dataframe, keyword):
    res = calculate_TFIDF(dataframe=dataframe, query=keyword).sort_values(by=['score'], ascending=False)
    for i in range(len(res[:10])):
        print("=============================================================================================================================================================================================")
        print(res.iloc[i]['Title'])
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(res.iloc[i]['Article'])