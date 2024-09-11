data = [
    {
        "createdAt": "2024-08-14 12:23:48.957411 +0300 +0300",
        "id": "7a8fe969-2a57-468e-82c9-1982d22023c5",
        "name": "Чехол-2",
        "price": 33,
        "sellerId": 3452,
        "statistics": {
            "contacts": 0,
            "likes": 0,
            "viewCount": 0
        }
    }
]

headers = {'Server': 'QRATOR',
           'Content-Type': 'application/json',
           'Transfer-Encoding': 'chunked',
           'Connection': 'keep-alive',
           'Keep-Alive': 'timeout=15',
           'X-Frame-Options': 'SAMEORIGIN',
           'X-XSS-Protection': '1; mode=block',
           'X-Content-Type-Options': 'nosniff',
           'Content-Encoding': 'gzip'
}

correct_post_id = "7a8fe969-2a57-468e-82c9-1982d22023c5"

wrong_post_id = "7a8fe969-2a57"
