import math
import http.client
import string
import json

from collections import namedtuple

conn = http.client.HTTPSConnection("www.yokaiswap.com")
payload = "{\"query\":\"query pools {\\n  now: pairs(where: {id_in: [\\\"0x268aaeed47d031751db1cbba50930fe2991f0ed0\\\"]}, orderBy: trackedReserveNative, orderDirection: desc) {\\n  token1Price\\n volumeUSD\\n    token0 {\\n         symbol\\n      }\\n    }\\n}\",\"variables\":{}}"

headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/subgraphs/name/yokaiswap/exchange", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))
json_object = json.loads(data.decode("utf-8"))
print ("DRM PRICE : $",json_object["data"]["now"][0]["token1Price"])
print ("VolumeUSD : $",json_object["data"]["now"][0]["volumeUSD"])
