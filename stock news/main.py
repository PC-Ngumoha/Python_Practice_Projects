import requests
import smtplib
from email.message import EmailMessage

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API Keys
STOCK_API_KEY = 'TY9YTC1XW6776R3O'
NEWS_API_KEY = 'bc80c14d529f447d9d37e66bb134907d'

# Email setup
EMAIL_TIMEOUT = 120
EMAIL_APP_PASSWORD = 'xznskpnfqgcgfqfg'
SENDER_ADDRESS = 'chukwuemekalearning@gmail.com'
RECEIVER_ADDRESS = 'chukwuemekangumoha@proton.me'

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
# print(daily_closing_rates)
# Get yesterday's closing stock price
closing_prices = [days for (_, days) in data.items()]
day1 = float(closing_prices[0]['4. close'])

# Get the day before yesterday's closing stock price
day2 = float(closing_prices[1]['4. close'])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20
diff = day1 - day2
abs_diff = abs(diff)

# Work out the percentage difference in price between the two days under consideration.
percent_diff = (abs_diff / day1) * 100

# If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff > 2:
    # print('Get News')

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_articles = response.json()['articles']

    # Use Python slice operator to create a list that contains the first 3 articles
    top_3_articles = news_articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    # Create a new list of the first 3 article's headline and description using list comprehension.
    core_info = [{'headline': article['title'], 'description': article['description']}
                    for article in top_3_articles]

    # Send each article as a separate email message.
    try:
        for piece in core_info:
            with smtplib.SMTP('smtp.gmail.com', port=587, timeout=EMAIL_TIMEOUT) as conn:
                conn.starttls()
                conn.login(user=SENDER_ADDRESS, password=EMAIL_APP_PASSWORD)
                symbol = '🔻' if diff < 0 else '🔺'

                # This approach enables me to send non-ascii characters as part of email message
                msg = EmailMessage()
                msg['Subject'] = f"{STOCK_NAME}: {symbol}{percent_diff:.2f}%"
                msg['From'] = SENDER_ADDRESS
                msg['To'] = RECEIVER_ADDRESS
                msg.set_content(f"Headline: {piece['headline']}\nBrief: {piece['description']}")
                conn.send_message(msg=msg)

        print('Email sent Successfully !!!')
    except Exception as e:
        print(f'Error sending email: {e}')



#Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

