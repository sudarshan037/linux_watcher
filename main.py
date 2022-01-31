from src.ChromeHistory import ChromeHistory
from pprint import pprint

if __name__ == "__main__":
    chrome_history = ChromeHistory()
    results = chrome_history.execute()
    pprint(results)