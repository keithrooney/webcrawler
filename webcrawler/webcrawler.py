import os
import bs4
import time
import requests


class Action(object):

    def __init__(self):
        pass

    def execute(self, **kwargs):
        pass


class Screenshot(Action):

    def __init__(self, home):
        """
        This class requires a directory to store the screenshots.

        :param home the location where we save our screenshots
        """
        super(Screenshot, self).__init__()
        self.home = home

    def execute(self, **kwargs):
        """
        We create a file, with the current time appended to file name,
        then write the content of our response.text to the file.

        :param kwargs name/value pairs, which should contain a response.
        """
        response = kwargs['response']
        filename = '{0}/screenshot_{1}.html'.format(self.home, time.time())
        try:
            with open(filename, 'w+') as f:
                f.write(response.text.encode(response.encoding))
        except Exception:
            os.remove(filename)


class WebCrawler(object):

    """
    A simple WebCrawler, which carries out an action, after a request.
    """

    def __init__(self, action):
        """
        Initialize the WebCrawler with an action, this action
        is carried out in the crawl method below.

        :param action An initialized class extending the Action class.
        """
        self.action = action

    def crawl(self, url, depth=1):
        """
        When this method is called, it will carry out the action
        initialized in the constructor, after which it will make
        a request to the specified url, parse it, then recursively
        call crawl with the new url and a depth of depth - 1.

        :param url the url we wish to make a request to and crawl.
        :param depth how deep we want to follow a link.
        """
        if depth == 0:
            return
        else:
            try:
                response = requests.get(url)
            except requests.RequestException:
                return
            self.action.execute(response=response)
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            for anchor in soup.find_all('a'):
                if anchor.has_attr('href'):
                    new_depth = depth - 1
                    self.crawl(anchor.get('href'), depth=new_depth)
