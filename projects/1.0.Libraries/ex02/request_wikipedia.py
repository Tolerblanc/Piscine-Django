import requests
import json
import dewiki
import sys


def get_wikipedia_page(title):
    url = f'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles={title}'
    response = requests.get(url)
    data = json.loads(response.text)
    page = next(iter(data['query']['pages'].values()))
    return dewiki.from_string(page['extract'])


def save_wikipedia_page(title):
    try:
        page = get_wikipedia_page(title)
    except Exception as e:
        print(f'Error: {e}')
        return

    with open(f'{title}.wiki', 'w') as file:
        try:
            file.write(page)
        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: request_wikipedia.py <title>')
        sys.exit(1)
    title = sys.argv[1]
    save_wikipedia_page(title)
