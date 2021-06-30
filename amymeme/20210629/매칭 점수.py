import re
from collections import defaultdict


def get_ex_link(body):
    return re.findall("<a href=\"https://(\S+)\"", body)


def get_score(page, word):
    return [x.lower() for x in re.findall(r'[a-zA-Z]+', page)].count(word.lower())


def get_url(page):
    return re.findall("<meta property=\"og:url\" content=\"https://(\S+)\"", page)[0]


def solution(word, pages):
    web_pages = defaultdict(dict)

    for idx, page in enumerate(pages):
        url = get_url(page)

        web_pages[url]['index'] = idx
        web_pages[url]['score'] = get_score(page, word)
        web_pages[url]['ex_links'] = get_ex_link(page)
        web_pages[url]['link_score'] = 0

    for key, value in web_pages.items():
        for ex_link in web_pages[key]['ex_links']:
            if ex_link in web_pages.keys():
                web_pages[ex_link]['link_score'] += web_pages[key]['score'] / len(web_pages[key]['ex_links'])
    for key, value in web_pages.items():
        print("key:", key)
        print("value:", value)
        print()
    max_match_score = max(map(lambda x: x['score'] + x['link_score'], web_pages.values()))
    return sorted(filter(lambda x: x[1]['score'] + x[1]['link_score'] == max_match_score, web_pages.items()),
                  key=lambda x: x[1]['index'])[0][1]['index']
