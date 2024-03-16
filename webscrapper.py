import selenium
print(selenium.__version__)
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

"""
* You should have a filepath to the set of channel links. Please, adjust the code based on your environment in the current directory.
* You should adjust iterations parameters. You might want to decrease or increase. 
"""

# You can adjust your preferred browser
# driver = webdriver.Chrome()
driver = webdriver.Firefox()

# Reading links
with open('links/channel_links.txt', 'r') as fo:
    channel_links = fo.read().split('\n')

# The number of iterations to scroll down the page so that more contents will be visible on browser.
iterations = 1

# Wait parameter for each scrolling iteration.
wait = 2

video_data = []
total_duration = 0

for link in channel_links:
    driver.get(link)
    sleep(1)

    channel_title = driver.find_element(By.XPATH, '//yt-formatted-string[contains(@class, "ytd-channel-name")]').text
    
    print('-' * 50)
    print("Moving on {}".format(channel_title))
    print("Scrolling down the page...")

    # Scrolling down 'iterations' times
    for _ in range(iterations):
        height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, arguments[0]);", height)
        sleep(wait)
        print(height)

    print("Executing scripts for titles, links...")
    
    link_elements = driver.find_elements(By.ID, "video-title-link")
    
    for link_element in link_elements:
        link = link_element.get_attribute('href')
        video_data.append(link)

    # Estimating approximate total duration
    print("Executing scripts for duration estimation...")
    duration = list(map(lambda x: x.text, 
                   driver.find_elements(By.CSS_SELECTOR, 'ytd-thumbnail-overlay-time-status-renderer')))

    for str_time in duration:
        if 1 <= len(str_time) <= 5:
            date = datetime.strptime(str_time, '%M:%S')
            total_duration += date.minute * 60 + date.second

        elif str_time:
            date = datetime.strptime(str_time, '%H:%M:%S')
            total_duration += date.minute * 3600 + date.minute * 60 + date.second

    hour = total_duration // 3600
    left_seconds = total_duration % 3600
    minute = left_seconds // 60
    second = left_seconds % 60
    
    print('{} Hours {} Minutes {} Seconds\n'.format(hour, minute, second))

with open('links/links.txt', 'w') as fo:
    for video_link in video_data:
        fo.write(video_link + '\n')