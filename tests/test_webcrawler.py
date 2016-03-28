import mock
import tempfile
import unittest

import os
import requests
import webcrawler

class TestWebcrawler(unittest.TestCase):

    url = 'https://www.google.ie/search?q=keithrooney93@gmail.com'

    simple_html_with_anchor = '<html><a href="some/link"></a></html>'

    def setUp(self):
        self.mock_action = mock.MagicMock()
        self.mock_response = mock.MagicMock()
        self.crawler = webcrawler.WebCrawler(self.mock_action)
        self.assertEqual(self.mock_action, self.crawler.action)

    @mock.patch('requests.get')
    def test_crawl(self, mock_request):
        mock_request.return_value = self.mock_response
        self.mock_response.text = self.simple_html_with_anchor

        self.crawler.crawl(self.url)

        mock_request.assert_called_once_with('https://www.google.ie/search?q=keithrooney93@gmail.com')
        self.mock_action.execute.assert_called_once_with(response=self.mock_response)

    @mock.patch('requests.get')
    def test_webcrawler_crawl_with_depth_equal_zero(self, mock_request):
        self.crawler.crawl(self.url, depth=0)
        mock_request.assert_not_called()

    @mock.patch('requests.get')
    def test_webcrawler_crawl_raises_request_exception(self, mock_request):
        mock_request.side_effect = requests.RequestException('Failed to make request.')
        self.crawler.crawl(self.url)
        mock_request.assert_called_once_with('https://www.google.ie/search?q=keithrooney93@gmail.com')


class TestScreenshot(unittest.TestCase):

    def setUp(self):
        self.directory = tempfile.mkdtemp()
        self.action = webcrawler.Screenshot(self.directory)
        self.assertEqual(self.directory, self.action.home)
        self.mock_response = mock.MagicMock()

    def test_execute(self):
        self.mock_response.text = 'This is some test'
        self.mock_response.encoding = 'utf-8'
        self.action.execute(response=self.mock_response)
        screenshots = os.listdir(self.directory)
        self.assertEqual(1, len(screenshots))
        with open('{0}\\{1}'.format(self.directory, screenshots[0]), 'r') as screenshot:
            self.assertEquals('This is some test', screenshot.read())

    def test_execute_raises_exception(self):
        self.action.execute(response=self.mock_response)
        screenshots = os.listdir(self.directory)
        self.assertEqual(0, len(screenshots))

if __name__ == '__main__':
    unittest.main()