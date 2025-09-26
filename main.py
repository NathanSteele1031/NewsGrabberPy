import requests, json, time

NEWS_PATH = "Data/news.json"
GOT_NEWS_PATH = "Data/got_news.txt"

def news_request(API_KEY, q):
    url = f"https://newsdata.io/api/1/latest?apikey={API_KEY}&q={q}"
    response = requests.get(url)
    json_output = response.json()
    articles = json_output["results"]
    return articles

def get_english_articles(articles):
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
        with open(GOT_NEWS_PATH, "r") as f:
            time_content = f.read()
        if time_content.split(" ")[2] == time.ctime().split(" ")[2]:
            return True
        return False
    except FileNotFoundError:
        with open(GOT_NEWS_PATH, "w") as f:
            pass
        return False

def write_time():
    with open(GOT_NEWS_PATH, "w") as f:
        f.write(time.ctime())

def show_article_titles(titles):
    number = 1
    for title in titles:
        print(f"{number}. {title}")
        number += 1

API_KEY = input("Type the API key: ")

def main():
    if not has_gathered_news():
        articles = news_request(API_KEY, "everything")
        write_time()
        json.dump(articles, open(NEWS_PATH, "w"))
        print("Requested Data")
    else:
        with open(NEWS_PATH, "r") as f:
            articles = json.load(f)
        print("Loaded Data")
    
    english_articles = get_english_articles(articles)
    article_titles = titles_of_articles(english_articles)
    show_article_titles(article_titles)

    running = True
    while running:
        selected_article = int(input("Select an article: "))
        print(articles[selected_article - 1]["link"])

if __name__ == "__main__":
    main()