#!/usr/bin/env python3
# -- coding: utf-8 --

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import tkinter

root = tkinter.Tk()
T = tkinter.Text(root, height=2, width=30)
T.pack()

# request headers while establishing connection with the url
request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0)
    Gecko/20100101 Firefox/40.0""",
    "Accept": """text/html,application/xhtml+xml,
    application/xml;q=0.9,*/*;q=0.8""",
    "Referer": "http://thewebsite.com",
    "Connection": "keep-alive"
}


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


# Get html source of url
def get_html(url):
    return urlopen(
        Request(url, headers=request_headers)
    ).read().decode('utf-8', 'ignore')


def get_tweet(username):
    soup = get_soup(get_html(f'https://twitter.com/{username}'))
    tweets = soup.findAll('div', attrs={"class": "tweet"})
    for tweet in tweets:
        if (not tweet.find('span', attrs={'js-pinned-text'})):
            return(tweet.find('p', attrs={"class": "js-tweet-text"}).text,
                   tweet.find('span', attrs={'class': '_timestamp'})
                   ['data-time'])


def get_tweets(unames):
    while True:
        for uname in unames:
            # T.insert(tkinter.END, get_tweet(uname))
            print(get_tweet(uname))
            # tkinter.mainloop()
        time.sleep(60)


# get_tweets(['MisraNityanand', 'TrueIndology'])
print(get_tweet('MisraNityanand'))
