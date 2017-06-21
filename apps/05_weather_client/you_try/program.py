import requests
import bs4
import collections


WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')

def main():
    print_header()
    code = input('What zipcode do you want the weather for (97201)? ')
    html = get_html_data(code)
    report = get_weather_from_html(html)
    print('The weather in {} is {}{} and {}.'.format(report.loc, report.temp, report.scale, report.cond))


def print_header():
    print('--------------------------------')
    print('          WEATHER APP')
    print('--------------------------------')
    print()


def get_html_data(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = get_city_and_state_from_loc(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)


def cleanup_text(text:str):
    if not text:
        return text

    text = text.strip()
    return text


def get_city_and_state_from_loc(loc:str):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()
