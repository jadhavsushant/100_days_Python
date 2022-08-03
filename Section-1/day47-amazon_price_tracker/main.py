
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

amz_product_url = "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/ref=sr_1_1?crid=31OCUKY4XG4OP&keywords=apple+13&qid=1659530576&sprefix=apple+1%2Caps%2C231&sr=8-1"

headers = {
    "authority": "www.amazon.com",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/103.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-dest": "document",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
}

url_response = requests.get(amz_product_url, headers=headers)


url_response_text = url_response.text
soup = BeautifulSoup(url_response_text, "lxml")
product_details = soup.find(name="span", id="productTitle")
product_name = product_details.getText().strip()
product_value = soup.find(name="span", class_="a-price-whole")
current_item_price = int(product_value.getText().replace(",", "").removesuffix("."))

print(f"Product Name:", product_name)
print(f"Product price:", current_item_price)

expected_price = 70000


def check_price(current_price, expecting_price):
    return current_price <= expecting_price


sender = 'sus099@gmail.com'
receivers = ['sus099@gmail.com']
message = f"""From: From Person {sender}
To: To Person {receivers}
Subject: Price Low !!! {product_name}

Low price alerts
"Product Name:", {product_name} - {expected_price}
"""


def send_email():
    smtp_obj = smtplib.SMTP("smtp.gmail.com", port=587)
    smtp_obj.sendmail(sender, receivers, message)


try:
    if check_price(current_price=current_item_price, expecting_price=expected_price):
        send_email()
        print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")
    print(smtplib.SMTPException.strerror)
