import utils.crawler as crawler
import time

begin = time.time()

crawler.crawl(source="https://ndh.vn",keyword="cổ phiếu",from_page=499,exit_when_url_exist=False)

end = time.time()

print("Done. Time taken: "+str(end-begin))