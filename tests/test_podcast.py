import os

import feedparser
import requests
from bs4 import BeautifulSoup

def query_changer(podcast_name):
    """
    This function takes a string parameter `podcastName`, replaces any spaces in it with plus signs,
    and returns a URL that can be used to search for the podcast on a podcast platform.

    Args:
    - podcastName (str): The name of the podcast to search for

    Returns:
    - url (str): The URL for the search results page for the podcast on a podcast platform
    """

    podcast_name = podcast_name.replace(" ", "+")
    url = "https://podcastaddict.com/?q=" + podcast_name
    return url


def scrape_query(url):
    """
    This function takes a URL parameter `url` that represents the search results page for a podcast
    on a podcast platform. It then scrapes the page to find the link to the podcast's main page.

    Args:
    - url (str): The URL for the search results page for the podcast on a podcast platform

    Returns:
    - link (str): The URL for the podcast's main page on the podcast platform
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    div = soup.find("div", {"id": "centertext"})
    a = div.find('a', {"class": "clickeableItemRow"})
    link = a.get('href')
    return link


def scrape_pod_page(url):
    """
    This function takes a URL parameter `url` that represents the main page for a podcast
    on a podcast platform. It then scrapes the page to find the link to the podcast's RSS feed.

    Args:
    - url (str): The URL for the podcast's main page on the podcast platform

    Returns:
    - link (str): The URL for the podcast's RSS feed
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    div = soup.find("div", {"class": "podcastHeader"})
    a = div.find('a')
    link = a.get('href')
    return link


def name_checker(string):
    """
    This function takes a string parameter `string` and replaces any characters that are not
    allowed in file names with underscores.

    Args:
    - string (str): The string to check and modify

    Returns:
    - string (str): The modified string with illegal characters replaced with underscores
    """

    string = string.replace(" ", "_")
    string = string.replace(":", "")
    string = string.replace("|", "")
    string = string.replace("__", "_")
    string = string.replace("___", "_")
    return string


def rss_scraper(rss, num_of_eps):
    """
    This function takes an RSS feed URL parameter `rss` and an integer parameter `numOfEps`
    that represents the number of episodes to scrape. It then scrapes the RSS feed to download
    the audio files for the specified number of episodes.

    Args:
    - rss (str): The URL for the podcast's RSS feed
    - numOfEps (int): The number of episodes to download

    Returns:
    - None
    """

    feed = feedparser.parse(rss)
    title = feed.feed.title
    if not os.path.exists(title):
        os.makedirs(title)
    c_dir = os.getcwd()
    rel_dir = "/" + title
    n_dir = c_dir + rel_dir
    os.chdir(n_dir)
    for i in range(num_of_eps):
        entry = feed.entries[i]
        link = entry.enclosures[0]
        link = link['href']
        name = entry.title
        name = str(i + 1) + "_" + name + ".mp3"
        name = name_checker(name)
        audio = requests.get(link)
        with open(name, 'wb') as f:
            f.write(audio.content)
        print(name)
        i += 1



os.chdir('/home/claude/Desktop/career/Projects/MediaCollector/data/audio')

#podcastName = input("Enter name of podcast :")
numberOfEpisodes = int(input("Enter number of episodes needed :"))
#url = queryChanger(podcastName)
#url = scrapeQuery(url)
#RSS_Link = scrapePodPage(url)
rss_scraper("https://feed.podbean.com/aitalk/feed.xml", numberOfEpisodes)

