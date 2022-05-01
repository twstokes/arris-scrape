from .downloader import Downloader
import requests

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
        result = requests.get(url,timeout=10)
        
        if result.status_code != 200:
            raise Exception("Received non-200 response.")

        return result.content
