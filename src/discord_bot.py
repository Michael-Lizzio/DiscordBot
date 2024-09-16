import json
import time
from bs4 import BeautifulSoup
from main_webscraper import MainWebScraper

PROFILE = "Profile 999"
class DiscordBot(MainWebScraper):
    def __init__(self):
        super().__init__(website_url="https://discord.com/channels/@me", speed_limiter=1.5, log_value=2,
                         headless=False, debug_name="Discord Bot", profile=PROFILE, undetectable=False)
        self.main()

    def main(self):
        pass
        # Floats through a list of channels using a dict as a key
        # In a json stores a list of all chat_is's that it has seen
        # adds new chats to the seen list and the test and what not to a "new message list"

if __name__ == '__main__':
    proxy_details = {
        'hostname': 'dc.smartproxy.com',
        'port': '10002',
        'username': '',
        'password': '',
        'ip': ''
    }
    scraper = DiscordBot()

