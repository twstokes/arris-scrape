"""
Parameters for the modem scraper.
"""
scraper_config = {
    'modem_url': '', # POPULATE MODEM URL HERE
    'max_retries': 5,
    'poll_interval_seconds': 30
}

"""
Parameters for InfluxDBClient. See influxdb.InfluxDBClient for all options.
"""
influx_config = {
    'host': '', # POPULATE INFLUX_DB HOST HERE
    'port': 8086,
    'database': 'modem'
}
