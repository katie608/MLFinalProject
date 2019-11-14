"""
Downloads data from internet into text files
"""


import math
import os
import requests
import sys
import time
import pdb
import urllib.request
from bs4 import BeautifulSoup


pro_ana_url_list = [
"https://proanagoddess.wordpress.com/ana-lifestyle-religion-2/",
"https://proanagoddess.wordpress.com/hello-beautiful-%e2%9d%a4%ef%b8%8f/",
"https://proanagoddess.wordpress.com/tips-tricks-2/",
"https://proanagoddess.wordpress.com/diets/",
"https://proanagoddess.wordpress.com/workouts/",
"https://proanagoddess.wordpress.com/thinspiration/",
"http://tilt214.tripod.com/index.html",
"http://tilt214.tripod.com/id7.html",
"http://tilt214.tripod.com/id8.html",
"http://tilt214.tripod.com/id31.html",
"http://tilt214.tripod.com/id30.html",
"https://theproanatips.com/",
"https://theproanatips.com/about-me/",
"https://theproanatips.com/blog/",
"https://theproanatips.com/disclaimer/"
]

pro_recovery_url_list = [
"https://tinybuddha.com/blog/how-i-healed-from-an-eating-disorder-and-stopped-hating-myself-and-my-body/",
"https://www.psychologytoday.com/us/blog/hunger-artist/201808/the-six-seductions-anorexia"
]

url_list = pro_ana_url_list

"""DOWNLOADING AND FORMATTING"""

class Text:
    """
    Text class holds text-based information downloaded from the web
    It uses local file caching to avoid downloading a given file multiple times,
    even across multiple runs of the programself.
    """
    def __init__(self, url, file_cache=os.path.join(sys.path[0], "cache")):
        """
        Given 'url' of a text file, create a new instance with the
        text attribute set by either downloading the URL or retrieving
        it from local text cache.
        Optional 'file_cache' argument specifies where text cache should be
        stored (default: same directory as the script in a "cache" folder)
        """
        self.url = url
        self.local_fn = os.path.join(file_cache, strip_scheme(url))

        # First see if file is already in local file cache
        if self.is_cached():
            print("INFO: {url!r} found in local file cache, reading".format(url=self.url))
            self.read_cache()

        # If not found, download (and write to local file cache)
        else:
            print("INFO: {url!r} not found in local file cache, downloading".format(url=self.url))
            self.download()
            self.write_cache()

    def __repr__(self):
        return "Text({url!r})".format(url=self.url)

    def is_cached(self):
        """Return True if file is already in local file cache"""
        return os.path.exists(self.local_fn)

    def download(self):
        """Download URL and save to .text attribute"""
        self.text = requests.get(self.url).text     # TODO: Exception handling
        # Wait 2 seconds to avoid stressing data source and rate-limiting
        # You don't need to do this here (only has to happen between requests),
        # but you should have it somewhere in your code
        time.sleep(2)

    def write_cache(self):
        """Save current .text attribute to text cache"""
        # Create directory if it doesn't exist
        directory = os.path.dirname(self.local_fn)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Write text to local file cache
        with open(self.local_fn, 'w') as fp:
            fp.write(self.text)

    def read_cache(self):
        """Read from text cache (file must exist) and save to .text attribute"""
        with open(self.local_fn, 'r') as fp:
            self.text = fp.read()

def get_extracted_text(url):
    """Takes in url, then downloads the html from the url and strips the html
    and creates a file with the extracted text
    Not a fruitful function so no doctests possible
    """
    # Set file title to the shortened title from the html
    file_title = requests.get(url).text
    # file_title = file_title.replace("American Rhetoric","")
    file_title = file_title.replace(": ","")
    print(file_title)

    soup = BeautifulSoup(file_title, 'html.parser') # gets file from the url and sets it to html
    fout = open(os.path.join("cache", soup.title.text), "w") # makes or opens a file with title of html

    # This can be modified to only return text with certain fonts or styles
    # text = html.get_text()
    #pdb.set_trace()
    # text = html.find_all(face="Droid Sans")
    # Writes the text from the html to a file as plain text
    # for line in text:
    #     fout.write(line.text)
    # # for line in text2:
    # #     fout.write(line.text)
    # fout.close()


    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    fout.write(text)
    fout.close()








def get_all_texts(list):
    """Takes in a list of URLs and rus get_extracted_text for each of them
    Not a fruitful function so no doctests possible
    """
    i = 0
    for url in url_list:
        get_extracted_text(url_list[i])
        i+=1
        time.sleep(2)


"""ANALYSIS"""
def get_lines(filename):
    """
    Read all lines from `filename` and return a list of strings,
    one per line, with whitespace stripped from the ends.
    >>> lines_list = get_lines("doctestText.txt")
    doctestText.txt
    >>> print(lines_list[0:2])
    ['Tomorrow, and tomorrow, and tomorrow,', 'Creeps in this petty pace from day to day,']
    """
    print(filename)
    lines = []
    with open(filename) as fp:
        for line in fp:
            processed_line = line.strip()
            lines.append(processed_line)
    return lines




# Run this code when called from the command line
if __name__ == "__main__":
    import doctest

    # Uncomment this when you want to download all text from url list
    get_all_texts(url_list)


    # Run all doctests in this file
    doctest.testmod()