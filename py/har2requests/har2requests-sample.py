import requests

s = requests.Session()

s.headers.update(
    {
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://petstore.swagger.io/",
        "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    }
)

r = s.get(
    "https://petstore.swagger.io/v2/swagger.json",
    headers={"accept": "application/json,*/*"},
)


s.headers.update({"accept": "application/json"})

r = s.get(
    "https://petstore.swagger.io/v2/pet/findByStatus",
    params={"status": "available"},
)


r = s.get(
    "https://petstore.swagger.io/v2/pet/findByStatus",
    params={"status": "available"},
)


r = s.get(
    "https://petstore.swagger.io/v2/pet/1234567890",
)


r = s.get(
    "https://petstore.swagger.io/v2/pet/1234567890",
)


r = s.get(
    "https://petstore.swagger.io/v2/store/inventory",
)


r = s.get(
    "https://petstore.swagger.io/v2/store/inventory",
)


r = s.get(
    "https://petstore.swagger.io/v2/store/order/5",
)
