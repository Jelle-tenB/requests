import requests
from twilio.rest import Client

# twilio needs
account_sid = "AC2bc5726229b561ebbb2316c9ad087f2d"
auth_token = "a098023576b6e3ffcd9a3c0e18b9263e"
client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "QUSD5JV3G3L01KDG"
NEWS_API = "b67dbbe956a240c89ddfdecfdb6f24b3"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API, 
}

news_params = {
    "apiKey": NEWS_API,
    "q": COMPANY_NAME,
    "searchIn": "title",
    "pageSize": 3,
}

response_stock = requests.get(STOCK_ENDPOINT, params=stock_params)
response_stock.raise_for_status()
stock_data = response_stock.json()['Time Series (Daily)']
stock_list = [value for (key, value) in stock_data.items()]
today_data = stock_list[0]
price_today = float(today_data["4. close"])
yesterday_data = stock_list[1]
price_yesterday = float(yesterday_data["4. close"])

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

percentage_change = round(((price_today - price_yesterday) / price_yesterday) * 100)
if percentage_change < 0:
    emoji = "🔻"
else:
    emoji = "🔺"
if abs(percentage_change) >= 5:
    print(f"the change is greater then 5%: {percentage_change}%")
    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    response_news.raise_for_status()
    news_data = response_news.json()
    new_list = [{"title": article["title"], "url": article["url"]} for article in news_data["articles"]]
    for item in new_list:
        message = client.messages.create(
            body=f"{STOCK}: {emoji}{abs(percentage_change)}%\nHeadline: {item['title']}\nLink: {item['url']}",
            from_="+12055193852",
            to="+31652593317",
        )
else:
    print(f"the change is smaller then 5%: {percentage_change}%")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

