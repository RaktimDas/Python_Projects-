# Importing The Required Modules
from bs4 import BeautifulSoup, get_text
import requests
import smtplib
# Email and Password For Sending The Mail to The Desired Address.
EMAIL = "sender-email"
PASSWORD = "sender-password"
# URL of The Product From Amazon India
URL = "https://www.amazon.in/BenQ-23-8-inch-Monitor-Built/dp/B073NTCT4Q/ref=sr_1_5?dchild=1&keywords=monitor&qid=1631012056&sr=8-5"
# Necessary Headers
params = {
    "Accept-Language": "get-it-on my-http-header",
    "User-Agent": "get-it-on my-http-header"
}
# Getting The Response From The Product Url
response = requests.get(URL, headers=params)
response_text = response.text
# Scraping The Details From The Product
soup = BeautifulSoup(response_text, "html.parser")
# Getting The Price
price = soup.find(name="span", id="priceblock_ourprice").getText()
# Removing The Currency Symbol Form the Digits
split_price_symbol = price.split("₹")[1]
# Removing The Commas Between The Digits
remove_price_comma = split_price_symbol.replace(",", "")
# Changing The Type Str to Float Of The
price_conversion = float(remove_price_comma)
# Getting The Title Of The Product
product_title = soup.find(name="span", id="productTitle").getText()

# If The Current Price is Less Than a Specified Price Then The Email Will Be Sent, Eg:Discounts.
# Currently The Email Will Be Sent At Current Price.
if price_conversion:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="gamerfunky619@gmail.com",
                            msg=f"Subject:Product Details-{product_title}\n{price}\n{URL}".encode("utf-8"))
        connection.close()
        print("Email Sent.")  # For Confirmation That It is Exceuted
