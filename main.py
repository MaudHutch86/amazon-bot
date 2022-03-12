import requests
from bs4 import BeautifulSoup
import smtplib



nutri_url = "https://www.amazon.fr/NUTRIBULLET-900-technologie-pr%C3%A9parations-Pr%C3%A9parateur/dp/B01N80V2NY/ref=sr_1_5?crid=30UCOI00YJMHD&keywords=nutribullet&qid=1647087829&sprefix=nutri%2Caps%2C80&sr=8-5"
response = requests.get(nutri_url)
url_content = response.text
soup = BeautifulSoup(url_content, 'html.parser')
price_element = soup.find(name="span", class_="a-offscreen")

new_price = (price_element.getText().split('€'))
dec_price = ((new_price[0]).split(','))
price = int(dec_price[0])
target_price = 100

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("yourgmail.com", "yourpassword")
        connection.sendmail(
            from_addr="yourgmail.com",
            to_addrs="receivergmail.com",
            msg=f"Subject:Time to buy!\n\nThe Nutribullet is now {price}€"
        )

