"""
Target module.
"""
class Target():
    """
    Subclass this for scraping targets.
    """
    def extract_items_from_html(self, html_string):
        """
        Generates Item subclasses by parsing HTML.

        Args:
            html_string (string): HTML
        """
