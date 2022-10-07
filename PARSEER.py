inport requests
from bs4 import BeautifulSoup




def get_data():
    headers = {
        "user-agent:  Mozilla/5.0(x11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.8.4472.106 Safari/537.36"
    }


    url = "https://www.labirint.ru/genres/2308/?page=1&display=table"

    response = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(response,"lxnl")

    pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)
    print(pages_count)


for page in range(1,pages_count + 1):
        url = "https://www.labirint.ru/genres/2308/?page=1&display=table&page={page}"

        response = requests.get(url=url, headers=headers)
        soup =BeautifulSoup(response.text, "lxnl")

        books_iteams = soup.find("tbody", class_= "products-table__body").find_all("tr")

        for bi in books_iteams:
            books_data = bi.find_all("td")

            try:
                book_title = books_data[0].find("a").text.strip()
            except:
                book_title = "Нет названия книги"

            print(book_title)





def main():
    get_data()

if __name__ == "__main__":
    main