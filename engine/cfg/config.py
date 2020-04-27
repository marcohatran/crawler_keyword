CHROME_PATH = "http://127.0.0.1:4444/wd/hub"

config = {
    "https://ndh.vn": {
        "elastic_index": "posts",
        "pagination_url": "https://ndh.vn/search.html?q={:s}&page={:d}.html",
        "xpath": {
            "post_links": "//div[@class='list-news']//article[@class='item-news']//h3[@class='title-news']//a",
            "title": "//h1[@class='title-detail']",
            "content": "//article[@class='fck_detail']",
            "date": "//span[@class='date-post']",
            "author": "",
        }
    }
}