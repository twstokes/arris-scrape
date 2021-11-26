import sys
import time

from config import scraper_config, influx_config
from scraper.targets.arris_modem import ArrisModem
from scraper.outputters import InfluxDBOutputter
from scraper.downloaders import RequestsDownloader

MAX_RETRIES = scraper_config['max_retries']
MODEM_URL = scraper_config['modem_url']

def run_scraper():
    """
    Starts the scraper.
    """
    print("Modem scraper running.")

    target = ArrisModem()
    outputter = InfluxDBOutputter(influx_config)
    downloader = RequestsDownloader()

    retries = 0
    while retries < MAX_RETRIES:
        try:
            body = downloader.download(MODEM_URL)
            items = target.extract_items_from_html(body)
            outputter.output(items)

            retries = 0
        except KeyboardInterrupt:
            sys.exit()
        except:
            outputter.reset()
            retries += 1
            print("Error:", sys.exc_info())

        time.sleep(scraper_config['poll_interval_seconds'])

    print("Abort! Max retries reached:", MAX_RETRIES)
    sys.exit(1)


if __name__ == "__main__":
    run_scraper()
