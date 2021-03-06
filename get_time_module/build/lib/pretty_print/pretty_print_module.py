from datetime import datetime

from get_time_package.get_time_module import get_time


def print_time_pretty(unixtime):
    formatted_time = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_time)


def main():
    time = get_time()
    print_time_pretty(time)


if __name__ == '__main__':
    main()