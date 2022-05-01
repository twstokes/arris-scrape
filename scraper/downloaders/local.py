from .downloader import Downloader

class LocalDownloader(Downloader):
    """
    Downloader subclass that loads local HTML files.

    Raises:
        Exception: Content couldn't be loaded successfully.

    Returns:
        string: HTML string of content.
    """
    @staticmethod
    def download(url):
        file = open(url, 'r')

        return file.read()