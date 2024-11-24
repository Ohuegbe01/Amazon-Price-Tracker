import lxml
import requests
import smtplib
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
                        , headers=header)
data = response.text
# print(data)

soup = BeautifulSoup(data, parser="lxml.parser", features="lxml")
floating_price_data = soup.find(name="span", class_="a-offscreen")
name_of_item_data = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")
name_of_item = name_of_item_data.getText().strip()
# print(name_of_item)
floating_price_text = floating_price_data.getText()
stripped_price = floating_price_text.split("$")
floating_price = float(stripped_price[1])
# print(floating_price)
buying_link = "https://www.amazon.com/gp/buy/payselect/handlers/display.html?_from=cheetah"

connection_gmail = "praiseisawesome52@gmail.com"
if floating_price < 100:
    body = f"Subject:Amazon item Suggestion\n\nItem name:{name_of_item}\nCurrent Price: at the moment is ${floating_price}\nBuying link: you can buy this item at\n{buying_link}"
    msg = body.encode('utf-8')

    with smtplib.SMTP("smtp.gmail.com",) as connection:
        connection.starttls()
        connection.login(user=connection_gmail, password="erua aayt wzga zlkd")
        connection.sendmail(from_addr=connection_gmail, to_addrs=connection_gmail,
                            msg=msg)