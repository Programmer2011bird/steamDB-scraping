from scraping import game_scraper, dollar_price_scraper
from colorama import Fore


def convert_to_toman(additional_input: str , price: float):
    DOLLAR_SCRAPER: dollar_price_scraper = dollar_price_scraper()
    toman_price: int = DOLLAR_SCRAPER.get_info()
    converted_price = float(price) * float(toman_price)

    print(f"{additional_input} {converted_price}")

def main() -> None:
    GAME_SCRAPER: game_scraper = game_scraper(Game_Id="1985810")
    GAME_PRICE: list[tuple[str, float]] = GAME_SCRAPER.get_info()

    for _, game_price in enumerate(GAME_PRICE):
        convert_to_toman(f"{Fore.LIGHTGREEN_EX}{game_price[0]} : {Fore.CYAN}", game_price[1])

if __name__ == "__main__":
    main()
