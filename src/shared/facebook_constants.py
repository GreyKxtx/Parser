fb_pages = [
    "https://www.facebook.com/usaidcep.ua",
    "https://www.facebook.com/gizukraine",
    "https://www.facebook.com/ebrdbasukraine/",
    "https://www.facebook.com/ucf.ua",
    "https://www.facebook.com/embassyofjapaninukraine",
    "https://www.facebook.com/usdos.ukraine",
    "https://www.facebook.com/deutschebotschaftkiew/?locale=uk_UA",
    "https://www.facebook.com/NLinUA?locale=uk_UA",
    "https://www.facebook.com/grantmanagement.ua",
    "https://www.facebook.com/ukinukraine",
    "https://www.facebook.com/SwissEmbassyKyiv/?locale=ru_RU",
    "https://www.facebook.com/PolishEmbassyKyiv"
]

fb_groups = [
    "https://www.facebook.com/groups/progrants",
    "https://www.facebook.com/groups/GrantsUA/",
    "https://www.facebook.com/groups/1522599061389938"
]

# Data for parsing
fb_scroll_count = 5
fb_login_page = 'https://www.facebook.com'
fb_email = 'fyodor.voloshin93@gmail.com'
fb_password = 'Gamma7890()'
facebook_datasets = [
    {
        'dataset': {
            'container': '//div[@data-pagelet="ProfileTimeline"]',
            'source': 'h1.x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz',
            'posts': 'div.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z',
            'post_info': 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm',
            'text_block': 'div.x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13',
            "keywords": ["Посол", "Мацуда", "шинкансэн", "початку"]
        },
        'links': fb_pages
    },
    {
        'dataset': {
            'container': '//div[@role="feed"]',
            'source': 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.x1xlr1w8',
            'posts': 'div.x1yztbdb.x1n2onr6.xh8yej3.x1ja2u2z',
            'post_info': 'a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm',
            'text_block': 'div.x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13',
            "keywords": ["друзі", "можливості", "WOS", "хататон 4.0", "гранти", "шановні", "стипендії", "суспільства"]
        },
        'links': fb_groups
    }
]
