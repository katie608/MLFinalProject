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

# I have them in a google doc, I just did not want to put them all in one place
# on my github, publically availible online, because that would be irresponsible
# If you happen to be someone reading this that I don't know, and you want them
# for your own research, just email me at katief650@gmail.com with ~2 sentences
# about who you are and what kind of research you are doing
pro_ana_url_list = [

]

pro_recovery_url_list = [
"https://tinybuddha.com/blog/how-i-healed-from-an-eating-disorder-and-stopped-hating-myself-and-my-body/",
"https://www.psychologytoday.com/us/blog/hunger-artist/201808/the-six-seductions-anorexia",
"https://www.reddit.com/r/fuckeatingdisorders/",
"https://www.reddit.com/r/EatingDisorders/",
"https://www.beateatingdisorders.org.uk/your-stories/recovery/progress-not-perfection",
"https://www.nationaleatingdisorders.org/stages-recovery",
"https://www.waldeneatingdisorders.com/blog/7-secrets-to-eating-disorder-recovery/",
"https://www.helpguide.org/articles/eating-disorders/eating-disorder-treatment-and-recovery.htm",
"https://www.verywellmind.com/things-to-stop-if-you-have-an-eating-disorder-1138275",
"https://www.self.com/story/eating-disorder-definition-recovery",
"https://www.eatingdisorderhope.com/recovery/self-help-tools-skills-tips",
"https://www.eat-26.com/eat-26/",
"https://www.nedc.com.au/eating-disorders/treatment-and-recovery/treatment/treatment-options/",
"https://www.beateatingdisorders.org.uk/your-stories/recovery/i-love-myself-more-than-i-ever-did",
"https://www.beateatingdisorders.org.uk/your-stories/recovery/travelling-overseas-eating-disorder",
"https://www.transfolxfightingeds.org/about",
"https://emilyprogram.com/blog/how-do-i-develop-a-positive-body-image/",
"https://emilyprogram.com/blog/eating-disorders-in-older-adults/",
"https://www.healthyplace.com/blogs/survivinged/2019/10/eating-disorder-stigma-eating-disorders-are-for-the-vain",
"https://www.healthyplace.com/blogs/survivinged/2019/10/the-risk-of-eating-disorders-in-college-students"
]


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
            # print("INFO: {url!r} found in local file cache, reading".format(url=self.url))
            self.read_cache()

        # If not found, download (and write to local file cache)
        else:
            # print("INFO: {url!r} not found in local file cache, downloading".format(url=self.url))
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
    for url in list:
        get_extracted_text(list[i])
        i+=1
        # Wait 2 seconds to avoid stressing data source and rate-limiting
        time.sleep(2)




# Run this code when called from the command line
if __name__ == "__main__":
    import doctest

    # Uncomment this when you want to download all text from url list
    get_all_texts(pro_ana_url_list )


    # Run all doctests in this file
    doctest.testmod()
