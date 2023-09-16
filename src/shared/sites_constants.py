sites = {
     'https://www.gov.uk/search/news-and-communications': {
         'name': 'GOV.UK',
         'posts': {
             'container': {
                 'tag': 'li',
                 'selector': 'class',
                 'method': 'find_all',
                 'path': 'gem-c-document-list__item'
             },
             'dataset': {
                'title': {
                    'tag': 'div',
                    'method': 'find',
                    'selector': 'class',
                    'path': 'gem-c-document-list__item-title'
                },
                'date': {
                     'tag': 'time',
                     'method': 'find'
                },
                'text': {
                    'tag': 'p',
                    'method': 'find',
                    'selector': 'class',
                    'path': 'gem-c-document-list__item-description'
                },
                'link': {
                    'tag': 'div',
                    'method': 'find',
                    'selector': 'class',
                    'path': 'gem-c-document-list__item-title',
                    'events': {
                        'tag': 'a',
                        'method': 'find',
                        'events': {
                            'method': 'extract_value',
                            'selector': 'href',
                            'events': {
                                'method': 'append_before',
                                'value': 'https://www.gov.uk'
                            }
                        }
                    }
                }
             }
         }
     },
    'https://www.gurt.org.ua/news/grants/?page={}': {
        'name': 'UA EMB',
        'pagination': {
            'method': 'format',
            'maxPage': 5
        },
        'posts': {
            'container': {
                'tag': 'div',
                'selector': 'class',
                'method': 'find_all',
                'path': 'newstxt'
            },
            'dataset': {
                'title': {
                    'tag': 'table',
                    'method': 'find_previous_sibling',
                    'events': {
                        'tag': 'a',
                        'selector': 'class',
                        'method': 'find'
                    }
                },
                'date': {
                    'tag': 'div',
                    'method': 'find_previous',
                    'selector': 'id',
                    'path': 'newshd'
                },
                'text': {},
                'link': {
                    'tag': 'table',
                    'method': 'find_previous_sibling',
                    'events': {
                        'tag': 'a',
                        'selector': 'class',
                        'method': 'find',
                        'events': {
                            'method': 'extract_value',
                            'selector': 'href',
                            'events': {
                                'method': 'append_before',
                                'value': 'https://www.gurt.org.ua'
                            }
                        }
                    }
                },
            }
        }
    },
    'https://www.prostir.ua/category/grants/?next_page={}': {
        'name': 'Prostir',
        'pagination': {
            'method': 'format',
            'maxPage': 5
        },
        'posts': {
            'container': {
                'tag': 'div',
                'selector': 'class',
                'method': 'find_all',
                'path': 'newsblock'
            },
            'dataset': {
                'title': {
                    'tag': 'a',
                    'method': 'find',
                    'events': {
                        'method': 'extract_value',
                        'selector': 'title'
                    }
                },
                'text': {
                    'tag': 'p:nth-child(4)',
                    'method': 'select',
                    'events':  {
                        'method': 'get_by_index',
                        'index': 0
                    }
                },
                'date': {
                    'tag': 'div',
                    'method': 'find',
                    'selector': 'class',
                    'path': 'date_cloud_news',
                    'events': {
                        'tag': 'p',
                        'method': 'find'
                    }
                },
                'link': {
                    'tag': 'a',
                    'method': 'find',
                    'events': {
                        'method': 'extract_value',
                        'selector': 'href'
                    }
                },
            }
        }
    },
    'https://www.ua.emb-japan.go.jp/itpr_uk/ua_oda.html': {
        'name': 'UA EMB',
        'posts': {
            'container': {
                'tag': 'div',
                'selector': 'id',
                'method': 'find',
                'path': 'section2',
                'events': {
                    'tag': 'a',
                    'method': 'find_all'
                }
            },
            'dataset': {
                'link': {
                    'method': 'extract_value',
                    'selector': 'href',
                    'events': {
                        'method': 'append_before',
                        'value': 'https://www.ua.emb-japan.go.jp'
                    }
                },
                'text': {}
            }
        }
    }
}