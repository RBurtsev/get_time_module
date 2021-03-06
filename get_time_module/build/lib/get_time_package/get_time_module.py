import requests


def get_time():
    url = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
    resp = requests.get(url)
    return resp.json()['unixtime']


def print_time(unixtime):
    print(unixtime)


def main():
    unixtime = get_time()
    print_time(unixtime)


if __name__ == '__main__':
    main()