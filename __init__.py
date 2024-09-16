from scraping import game_scraper, dollar_price_scraper

def convert_to_toman(price: float):
    DOLLAR_SCRAPER: dollar_price_scraper = dollar_price_scraper()
    toman_price: int = DOLLAR_SCRAPER.get_info()

    print(float(price) * int(toman_price))

def main() -> None:
    GAME_SCRAPER: game_scraper = game_scraper()
    price = GAME_SCRAPER.get_info()

    convert_to_toman(price[0][1])

if __name__ == "__main__":
    main()
