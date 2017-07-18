"""
Downloader module.
"""
import requests


class Downloader():
    """
    Subclass this for downloading content from URLs.
    """
    def download(self, url):
        """
        Given a URL, return the HTML content body as a string, otherwise raise.

        Args:
            url (string): URL to download HTML from.
        """

class RequestsDownloader(Downloader):
    """
    Downloader subclass that uses Requests to download content.

    Raises:
        Exception: Content couldn't be downloaded successfully.

    Returns:
        string: HTML string of content.
    """
    @staticmethod
    def download(url):
        result = requests.get(url)

        if result.status_code != 200:
            raise Exception("Received non-200 response.")

        return result.content
