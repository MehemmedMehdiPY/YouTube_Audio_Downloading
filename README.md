# YouTube_Audio_Downloading
The repository aims to present the code for web-scrapping YouTube pages. The task is to download audio data from YouTube.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install yt-dlp.

```bash
pip install selenium
```

## Usage
You are supposed to run webscrapper.py script to scrape pages on YouTube. The expected input is channels.txt file (exemplary file uploaded in links folder) containing links to YouTube channels whose authors share contents in Azerbaijani language. The task should follow the below procedure:
* Researching YouTube channels from Azerbaijan and collecting their links in .txt file. Make sure you provide the right folder path to videos section, for example, https://www.youtube.com/@channel_name/**videos**. And ensure if links are arranged line by line in .txt file.

* Go to script and adjust your **iterations** parameter. In our case, initial parameter was **iterations=1**. The parameter value indicates how many times to scroll down the YouTube channel page. The more the number of iterations the more likely to load the more videos in the browser. It is better if you increase it in order to collect more video links.

* After you are done with that, share your links with us. Later, we will provide you separate .txt files as chunks with 100 links.
 
* When you have access to those chunks, go to the [colab](https://colab.research.google.com/drive/11dQCvhGE9Iu6yDYP4CFvDwZFu9WzEdpi?usp=sharing) and follow instructions there.