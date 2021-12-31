import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
}

conn.request("GET", "/query?function=GLOBAL_QUOTE&symbol=PLTR", headers=headers)
# TSLA
# PLTR
# HCAC

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
