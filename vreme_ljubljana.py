import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "4cb395500bmsh7ca4738812909a8p127940jsnab3936735aec",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

conn.request("GET", "/weather?q=Ljubljana&lat=0&lon=0&callback=test&id=2172797&lang=null&units=%22metric%22&mode=xml%2C%20html", headers=headers)

res = conn.getresponse()
data = res.read()


file=open("uros.txt","w")
file.write(data.decode("utf-8"))
file.close()

file=open("uros.txt","r")
print(file.read())


