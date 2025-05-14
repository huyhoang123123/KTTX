from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trang web
driver.get("http://quotes.toscrape.com/")

# Lấy danh sách các trích dẫn trên trang
quotes = driver.find_elements(By.CLASS_NAME, "quote")

# Duyệt qua từng trích dẫn và in ra nội dung cùng tác giả
for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    print(f'"{text}" - {author}')

# Đóng trình duyệt
driver.quit()
