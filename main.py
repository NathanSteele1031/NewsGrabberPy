import requests, json, time

def news_request(API_KEY, q):
    url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&q={q}"
    response = requests.get(url)
    json_output = response.json()
    articles = json_output["results"]
    return articles

def english_articles(articles):
    english_articles = []
    for article in articles:
        if article["language"] == "english":
            english_articles.append(article)
    return english_articles

def titles_of_articles(articles):
    titles = []
    for article in articles:
        titles.append(article["title"])
    return titles

def has_gathered_news():
    try:
        with open("got_news.txt", "r") as f:
            time = f.read()
        if time.split(" ")[2] == time.ctime().split(" ")[2]:
            return True
        return False
    except FileNotFoundError:
        with open("got_news.txt", "w") as f:
            pass
        return False
    except:
        return False

API_KEY = input("Type the API key: ")
# articles = news_request(API_KEY, "covid")
# articles = english_articles(articles)
# article_titles = titles_of_articles(articles)
def main():
    pass

if __name__ == "__main__":
    main()