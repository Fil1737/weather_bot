from requestion.requestion import save_html_page, weather_data


def main():
    save_html_page(55.649298, 37.343567)
    print(weather_data())
    

 
if __name__ == "__main__":
    main()