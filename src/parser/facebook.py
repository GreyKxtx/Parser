import time
from src.services.parser_service import fb_login
from src.services.parser_service import initiate_chrome
from src.services.parser_service import load_page
from src.services.parser_service import fb_scroll
from src.shared.facebook_constants import facebook_datasets
from src.shared.facebook_constants import fb_login_page
from src.shared.facebook_constants import fb_scroll_count
from selenium.webdriver.common.by import By
from src.database.database import dbService
from src.services.parser_service import has_text_keyword
from selenium.common.exceptions import NoSuchElementException

browser_session = initiate_chrome()


def run():
    global browser_session
    init()

    for data in facebook_datasets:
        for link in data.get('links'):
            print(f'Link: {link}')
            load_page(browser_session, link)
            parse(data.get('dataset'))

    print('Done')


def init():
    global browser_session
    load_page(browser_session, fb_login_page)
    fb_login(browser_session)
    time.sleep(1.5)


def parse(dataset):
    try:
        global browser_session
        scroll_posts()

        page_source = browser_session.find_element(By.CSS_SELECTOR, dataset.get('source')).text
        post_container = browser_session.find_element(By.XPATH, dataset.get('container'))
        posts = post_container.find_elements(By.CSS_SELECTOR, dataset.get('posts'))

        for post in posts:
            post_text = get_post_text(post, dataset)

            if has_text_keyword(post_text, dataset.get('keywords')):
                post_info = post.find_element(By.CSS_SELECTOR, dataset.get('post_info'))
                post_link = post_info.get_attribute("href").split('?')[0]
                post_date = post_info.get_attribute("aria-label")
                post_data = {
                    "title": page_source,
                    "text": post_text,
                    "date": post_date,
                    "link": post_link
                }

                dbService.insert("Facebook", post_data)

    except ValueError:
        return


def scroll_posts():
    for _ in range(fb_scroll_count):
        fb_scroll(browser_session, 'page')
        time.sleep(1)

    print(f'Page scrolled {fb_scroll_count} times')


def get_post_text(post, dataset):
    try:
        text_block = post.find_element(By.CSS_SELECTOR, dataset.get('text_block'))
        return text_block.get_attribute('innerText')
    except NoSuchElementException:
        return ''
