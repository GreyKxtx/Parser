from src.parser.facebook import run as facebook_pages_parce
from src.parser.sites import run as sites_parce


def start():
    sites_parce()
    facebook_pages_parce()
