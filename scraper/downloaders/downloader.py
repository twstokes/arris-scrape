"""
Downloader module.
"""
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
