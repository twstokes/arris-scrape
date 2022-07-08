import sys
import time

from config import scraper_config, influx_config
from scraper.outputters.influxdb import InfluxDBOutputter
from scraper.outputters.printer import PrinterOutputter
from scraper.downloaders.requests import RequestsDownloader

MAX_RETRIES = scraper_config['max_retries']
MODEM_URL = scraper_config['modem_url']
MODEM_MODEL = scraper_config['modem_model']
OUTPUTTER = scraper_config['outputter']

def run_scraper():
    """
    Starts the scraper.
    """
    print("Modem scraper running.")

    target = get_target(MODEM_MODEL)
    outputter = get_outputter(OUTPUTTER)
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

def get_target(model):
    if model == "SB6183":
        from scraper.targets.arris_modem_SB6183 import ArrisModemSB6183
        return ArrisModemSB6183()
    if model == "TM1602AP2":
        from scraper.targets.arris_modem_TM1602AP2 import ArrisModemTM1602AP2
        return ArrisModemTM1602AP2()
    if model == "CM802A":
        from scraper.targets.arris_modem_CM820A import ArrisModemCM820A
        return ArrisModemCM820A()
    if model == "SB6190":
        from scraper.targets.arris_modem_SB6190 import ArrisModemSB6190
        return ArrisModemSB6190()

def get_outputter(output):
    if output == 'influxdb':
        return InfluxDBOutputter(influx_config)
    else:
        return PrinterOutputter()

if __name__ == "__main__":
    run_scraper()
