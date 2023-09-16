import requests
from src.shared import sites_constants
from bs4 import BeautifulSoup
from src.database.database import dbService
from src.services.parser_service import get_page_value
from src.services.parser_service import get_soup_value
from src.services.parser_service import has_text_keyword

keywords = ['конкурс', 'грант']

#'Somalia', 'Rescued', 'Кінцевий', 'IPA', '2023', 'Допомога'
def run():
    for link in sites_constants.sites:
        data = sites_constants.sites[link]
        parse(link, data)


def page_load(self, path=None):
    if path is None:
        if self.browser_session is None:
            return -1
        else:
            self.browser_session.get(self.login_page)
    else:
        if self.browser_session is None:
            return -1
        else:
            self.browser_session.get(path)


def parse(link, data, pagination_index=1):
    try:
        pagination_data = data.get('pagination')
        initial_link = link

        if pagination_data:
            match pagination_data.get('method'):
                case 'format':
                    link = link.format(pagination_index)

        print(f'Current link: {link}')
        response = requests.get(link)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            post_vars = data.get('posts')
            posts = get_page_value(soup, post_vars.get("container"))

            print(f'Posts count: {len(posts)}')
            for post in posts:
                if is_valid_post(post, post_vars.get('dataset')):
                    post_data = {}

                    for key, attr in post_vars.get('dataset').items():
                        parsed_data = get_page_value(post, attr)

                        if bool(parsed_data):
                            post_data[key] = get_soup_value(parsed_data)
                        else:
                            print(f'Cannot find {key}!')

                    dbService.insert(data.get('name'), post_data)

            pagination_index += 1
            if pagination_data and pagination_index <= pagination_data.get('maxPage'):
                parse(initial_link, data, pagination_index)
        else:
            print(f'Can`t parce site with link: {link}')
    except ValueError:
        ValueError(f'Can`t parce site with link: {link}')

    return []


def is_valid_post(post, dataset):
    try:
        post_title = get_soup_value(get_page_value(post, dataset.get('title')))
        post_text = get_soup_value(get_page_value(post, dataset.get('text')))
        return has_text_keyword(post_title, keywords) or has_text_keyword(post_text, keywords)
    except ValueError:
        print('Cannot find title or text')
        return False

