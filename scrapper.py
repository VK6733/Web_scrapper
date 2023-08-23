from urllib import request
import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd


tags=st.selectbox("choose the topic for the search",["love","humor","life","books","friendship"])
url=f"https://quotes.toscrape.com/tag/{tags}/"

generate=st.button("generate csv")

st.write("we are scrappping data from",url)


res=requests.get(url)

st.write(res)

content=BeautifulSoup(res.content,"html.parser")

quotes=content.find_all("div",class_="quote")

file=[]

for quote in quotes:
    text=quote.find("span",class_="text").text
    author=quote.find("small",class_="author").text
    link=quote.find("a")
    st.success(text)
    st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>by author ::{author}</a>",unsafe_allow_html=True)
   
    file.append([text,author,link['href']])

if generate:
    try:
        df=pd.DataFrame(file)
        df.to_csv("quote.csv",index=False,header=['quote','author','link'],encoding='cp1252')
    except:
        st.write("Loading...")