import webcrawler


if __name__ == '__main__':
    google_url = 'https://www.google.ie/search?q=keithrooney93@gmail.com'
    crawler = webcrawler.WebCrawler(webcrawler.Screenshot('../resources'))
    crawler.crawl(google_url, depth=3)
