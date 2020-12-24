import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "b3b98f9843mshb1737632f7164f8p1d0a7bjsne579d6304f33",
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
}

conn.request("GET", "/query?function=GLOBAL_QUOTE&symbol=PLTR", headers=headers)
# TSLA
# PLTR
# HCAC

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
