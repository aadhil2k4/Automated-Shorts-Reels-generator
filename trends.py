import requests
import pandas as pd
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError
import time

def get_trends_data(kw_list, retries=3, sleep_duration=60):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

    for attempt in range(retries):
        try:
            iot = pytrends.interest_over_time()
            return iot
        except requests.exceptions.RequestException as e:
            print(f"RequestException: {e}. Retrying in {sleep_duration} seconds...")
            time.sleep(sleep_duration)
        except TooManyRequestsError as e:
            print(f"TooManyRequestsError: {e}. Retrying in {sleep_duration} seconds...")
            time.sleep(sleep_duration)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    return None

kw_list = ["Blockchain"]
trends_data = get_trends_data(kw_list)

if trends_data is not None:
    print(trends_data.head())
else:
    print("Failed to retrieve trends data after multiple attempts.")
