
import requests
from bs4 import BeautifulSoup

def fetch_books_from_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    books = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        book_items = soup.find_all("div", class_="tp-product-content-2")
        for item in book_items:
            try:
                title = item.find("h3", class_="tp-product-title-2").text.strip()
                price = item.find("div", class_="tp-product-price-wrapper-2").text.strip()
                link = item.find("a")["href"].strip()
                full_link = f"https://www.se-ed.com{link}"
                books.append({
                    "title": title,
                    "price": price,
                    "link": full_link
                })
            except AttributeError:
                continue
    return books

def fetch_all_books(base_url):
    books = []
    page = 1
    while True:
        url = f"{base_url}?page={page}"
        print(f"Fetching: {url}")
        page_books = fetch_books_from_page(url)
        if not page_books:
            break
        books.extend(page_books)
        page += 1
    return books

if __name__ == "__main__":
    base_url = "https://www.se-ed.com/Search"
    all_books = fetch_all_books(base_url)
    print(f"Fetched {len(all_books)} books.")
