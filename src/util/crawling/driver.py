from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.core import settings


class WebDriver(webdriver.Chrome):
    def __init__(self, OPTION):
        if OPTION == 'PRODUCTION':
            path = settings.DRIVER_PATH
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1280x1696')
            chrome_options.add_argument('--user-data-dir=/tmp/user-data')
            chrome_options.add_argument('--hide-scrollbars')
            chrome_options.add_argument('--enable-logging')
            chrome_options.add_argument('--log-level=0')
            chrome_options.add_argument('--v=99')
            chrome_options.add_argument('--single-process')
            chrome_options.add_argument('--data-path=/tmp/data-path')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--homedir=/tmp')
            chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')        
            
            chrome_options.binary_location = settings.BINARY_DRIVER_PATH
        
        elif OPTION == 'DEVELOP':
            path = settings.LOCAL_DRIVER_PATH
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
        
        webdriver.Chrome.__init__(
            self,
            executable_path = path,
            options = chrome_options
        )