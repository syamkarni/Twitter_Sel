from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import uuid
from datetime import datetime
import time

# Load environment variables
load_dotenv()
TWITTER_USERNAME = os.getenv("username")
TWITTER_PASSWORD = os.getenv("password")

# MongoDB Configuration
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["twitter_scraper"]
collection = db["trending_topics"]

# Path to ChromeDriver 
CHROMEDRIVER_PATH = "/Users/syamkarniuppalapati/Downloads/chromedriver-mac-arm64/chromedriver"


chrome_options = Options()

# PROXY = "user:pass@host:port"
# chrome_options.add_argument(f'--proxy-server=http://{PROXY}')

driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)


driver.get("https://twitter.com/login")
driver.implicitly_wait(10)

username_field = driver.find_element(By.NAME, "text")
username_field.send_keys(TWITTER_USERNAME)
username_field.send_keys(Keys.RETURN)
time.sleep(2)

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(TWITTER_PASSWORD)
password_field.send_keys(Keys.RETURN)
time.sleep(5)

print("python3 main.py")
print("Logged into Twitter. Navigating to Explore page...")

time.sleep(5)


try:
    trending_container = driver.find_element(By.XPATH, "//div[@aria-label='Timeline: Trending now']")
except Exception as e:
    print("Failed to find the 'Timeline: Trending now' container:", e)
    driver.quit()
    exit()


trend_blocks = trending_container.find_elements(By.XPATH, ".//div[@data-testid='trend']")
trend_blocks = trend_blocks[:4]

trending_topics = []


for i, block in enumerate(trend_blocks, start=1):

    block_html = block.get_attribute("outerHTML")
    

    div_ltr_elements = block.find_elements(By.XPATH, './/div[@dir="ltr"]')
    
    if len(div_ltr_elements) < 2:
        # If we can't find at least 2, fallback to the last one or skip
        continue
    

    main_topic = div_ltr_elements[1].text.strip()
    trending_topics.append(main_topic)


document = {
    "unique_id": str(uuid.uuid4()),
    "trend1": trending_topics[0] if len(trending_topics) > 0 else "N/A",
    "trend2": trending_topics[1] if len(trending_topics) > 1 else "N/A",
    "trend3": trending_topics[2] if len(trending_topics) > 2 else "N/A",
    "trend4": trending_topics[3] if len(trending_topics) > 3 else "N/A",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}
collection.insert_one(document)

print("Saved Trending Topics to MongoDB:")
print(document)


time.sleep(3)
driver.quit()
