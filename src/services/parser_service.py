from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.shared.facebook_constants import fb_email
from src.shared.facebook_constants import fb_password


def get_page_value(soup, data):
    if not soup:
        print('Invalid soup')
        return ''

    try:
        if data and not is_default_method(data.get('method')):
            next_events = data.get('events')

            match data.get('method'):
                case 'find_previous_sibling':
                    soup_result = soup.find_previous_sibling(data.get('tag'))
                    return get_page_value(soup_result, next_events)
                case 'find_previous':
                    attrs = {}

                    if data.get('selector') and data.get('path'):
                        attrs = {
                            data.get('selector'): data.get('path')
                        }

                    soup_result = soup.find_previous(data.get('tag'), attrs)
                    return get_page_value(soup_result, next_events)
                case 'extract_value':
                    return get_page_value(soup.get(data.get('selector')), next_events)
                case 'append_before':
                    return get_page_value(f'{data.get("value")}{soup}', next_events)
                case 'get_by_index':
                    return get_page_value(soup[data.get('index')], next_events)
        elif data:
            method = getattr(soup, data.get('method'))
            attrs = {}

            if data.get('selector') and data.get('path'):
                attrs = {
                    f"{data.get('selector')}": data.get('path')
                }

            result = method(data.get('tag'), attrs=attrs)

            if result and data.get('events'):
                return get_page_value(result, data.get('events'))
            else:
                return result
        else:
            return soup
    except ValueError:
        print('Cannot find var with path', data.get('path'))
        return ''


def is_default_method(method):
    if method == 'find_all' or method == 'find' or method == 'select':
        return True
    else:
        return False


def get_soup_value(soup):
    if soup:
        if isinstance(soup, str):
            return soup
        else:
            return soup.text.strip()
    else:
        return None


def initiate_chrome():
    options = Options()

    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")
    options.add_experimental_option(
        "prefs", {
            "profile.default_content_setting_values.notifications": 1
        }
    )

    return webdriver.Chrome(options=options)


def close_session(browser_session):
    browser_session.close()
    browser_session.quit()
    return None


def load_page(browser_session, url):
    return browser_session.get(url)


def fb_login(browser_session):
    email_field = browser_session.find_element(By.XPATH, "//input[@id='email']")
    password_field = browser_session.find_element(By.XPATH, "//input[@id='pass']")

    email_field.send_keys(fb_email)
    password_field.send_keys(fb_password, Keys.ENTER)

    return browser_session


def find_in_element(element, xpath):
    return element.find_element(By.CSS_SELECTOR, xpath)


def fb_scroll(browser_session, method):
    match method:
        case 'top':
            browser_session.execute_script("window.scrollTo(0, 0)")
        case 'page':
            browser_session.execute_script(
                "window.scrollTo(0, document.body.clientHeight)")


def has_text_keyword(text, keywords):
    if not text:
        return False
    else:
        return any([x.lower() in text.lower() for x in keywords])
