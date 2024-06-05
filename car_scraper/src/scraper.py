import requests
from bs4 import BeautifulSoup


def scrape():

    url = 'https://www.acko.com/two-wheeler-insurance/best-mileage-bikes-in-india/'


    response = requests.get(url)



    data=[]
    soup = BeautifulSoup(response.content, 'html.parser')
    

    elements = soup.find('table')

    rows= elements.find_all('tr')

    headers = [header.text.strip() for header in rows[0].find_all('th')]


    data.append(headers)

    for row in rows[1:]:
        columns = row.find_all('td')
        columns_data = [column.text.strip() for column in columns]
        data.append(columns_data)

    sample = []

    for prop in data:
           
        if prop == data[0]:
            continue
        SlNo, Name, Mileage, Price=prop
            
        sample.append({"sr": SlNo, "name": Name, "mileage": Mileage, "price": Price})  


    

    return sample 



