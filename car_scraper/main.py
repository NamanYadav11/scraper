from src.scraper import scrape
from src.store import input_data


def main():
    data=scrape()

    # print(data)
    input_data(data)

    

    
   

if __name__ == "__main__":
    main()