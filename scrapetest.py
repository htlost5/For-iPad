import requests
from bs4 import BeautifulSoup
import re

def get_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'xml')  # 'html.parser'から'xml'に変更

def get_title():
    soup = get_page_content('https://ja.wikipedia.org/wiki/')
    page_title = soup.find("title")
    return page_title.text.strip()

def get_ticket_info():
    soup = get_page_content('https://www.anime-japan.jp/tickets/')
    ticket_info_div = soup.find('div', class_='ticket-info')
    if ticket_info_div:
        return ticket_info_div.text.strip()
    else:
        return "チケット情報が見つかりませんでした。"

def get_anime_list():
    soup = get_page_content('https://www.anime-japan.jp')
    # 出展アニメリストを含む要素を特定し、リストを作成
    anime_list = [item.text for item in soup.find_all('title')]
    return anime_list

def get_news():
    soup = get_page_content('https://www.anime-japan.jp/news/')
    # ニュース項目を含む要素を特定し、リストを作成
    news_items = [item.text for item in soup.find_all('div', class_='news-item')]
    return news_items

def main():
    title = get_title()
    ticket_info = get_ticket_info()
    anime_list = get_anime_list()
    news = get_news()

    print(title)
    print("\nチケット情報:")
    print(ticket_info)
    print("\n出展アニメ一覧:")
    for anime in anime_list:
        print(anime)
    print("\nニュース:")
    for item in news:
        print(item)

if __name__ == "__main__":
    main()