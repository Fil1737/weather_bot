import lxml

from bs4 import BeautifulSoup
import requests

def save_html_page(latitude, longitude): # сначала широта
    url = f"https://yandex.ru/pogoda?lat={latitude}&lon={longitude}"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text

    with open("page.html", "w", encoding="utf8") as file:
        file.write(src)
    # сохраняем страницу с введёнными кордами


def str_data_from_page(class__):
    with open("page.html", encoding="utf8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    str = soup.find(class_=f"{class__}").text
    return(str)



def weather_data():
    if len(str_data_from_page("fact__unit")) == 6:
        wind_from = str_data_from_page("fact__unit")[-1]
    else:
        wind_from = f"{str_data_from_page("fact__unit")[-2]}{str_data_from_page("fact__unit")[-1]}"
    
    try:
        wind_speed = str_data_from_page("wind-speed")
    except:
        wind_speed = "no data"
        wind_from = "no data"

    weather_data = {
        "temp": str_data_from_page("temp__value temp__value_with-unit"),
        "condition": str_data_from_page("link__condition day-anchor i-bem"),
        "wind_speed": wind_speed,
        "wind_from": wind_from
    }
    return(weather_data)