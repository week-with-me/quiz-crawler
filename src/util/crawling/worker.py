import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.core import settings
from src.util.regex import get_movie_cd
from src.util.crawling.driver import WebDriver


def get_movie_information(OPTION='DEVELOP'):
    try: 
        driver = WebDriver(OPTION=OPTION)
        driver.get(url=settings.URL)

        wrapper = driver.find_element(By.XPATH, '//*[@id="tab-5"]')
        driver.execute_script("document.getElementById('tab-5').style.display = 'block';")
        parent_window = driver.current_window_handle

        movies = []

        for i in range(0, 500):
            movie_info = wrapper.find_element(By.ID, f'tr_tot{i}')
            
            movie_element = movie_info.find_element(By.CSS_SELECTOR, 'td > a')
            
            movie_cd = movie_element.get_attribute('onclick')
            movie_cd = get_movie_cd(movie_cd)
                    
            movie_element.send_keys(Keys.ENTER)
            
            current_window = driver.current_window_handle
            
            driver.switch_to.window(current_window)
                        
            movie_image = driver.find_element(By.CSS_SELECTOR, 'div.ovf.info.info1 > a').get_attribute('href')
            
            driver.find_element(By.CSS_SELECTOR, 'div.hd_layer > a:nth-child(3)').send_keys(Keys.ENTER)

            driver.switch_to.window(parent_window)
            
            movie_name = movie_info.find_element(By.ID, 'td_movie').text
            movie_date = movie_info.find_element(By.ID, 'td_openDt').text
            movie_total_audiences = movie_info.find_element(By.ID, 'td_totAudiAcc')
            movie_total_audiences_number = movie_total_audiences.text
            
            try:
                movie_total_audiences.find_element(By.CSS_SELECTOR, 'img')
                movie_total_audiences_only_seoul = True
            except:
                movie_total_audiences_only_seoul = False
            
            movie = {
                'movie_cd': movie_cd,
                'name': movie_name,
                'date': movie_date,
                'image': movie_image,
                'total_audiences': movie_total_audiences_number,
                'is_only_seoul': movie_total_audiences_only_seoul
            }
            
            movies.append(movie)

        return movies
    
    finally:
        
        driver.close()
