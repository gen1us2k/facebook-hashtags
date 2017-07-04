# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup


def get_post_by_hashtag(hashtag):
    url = "https://www.facebook.com/hashtag/%s" % hashtag
    r = requests.get(url, headers={'User-agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"})
    hashtags = []
    for code in BeautifulSoup(r.content, 'html.parser').findAll('code'):
        for div in BeautifulSoup(str(code.contents).replace('<!--', '').replace('-->', ''), 'html.parser').findAll('div', {'class': 'userContentWrapper'}):
            userprofile = ""
            user_content = ""
            profile_link = ""
            original_post = ""
            data = BeautifulSoup(str(div), 'html.parser')
            for span in data.findAll('span', {'class': 'fwb'}):
                # print span
                # print
                # print
                for link in span.findAll('a'):
                    if not link:
                        continue
                    if link.get('href', ""):
                        profile_link = link.get('href', "")
                        userprofile = link.getText()

            for span in data.findAll('span', {'class': 'fsm'}):
                for link in span.findAll('a'):
                    if not link:
                        continue
                    if link.get('href', ""):
                        original_post = link.get('href', "")


            for div in data.findAll('div', {'class': 'userContent'}):
                user_content = div.getText()

            hashtags.append({
                'profile_link': profile_link,
                'userprofile': userprofile,
                'content': user_content,
                'original_post': original_post
                })
    return hashtags



if __name__ == '__main__':
    print get_post_by_hashtag('делайдобро')
