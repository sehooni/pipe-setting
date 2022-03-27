from urllib import request
from urllib.parse import urlencode, quote_plus
import json
import datetime
import math
from datetime import datetime, time, timedelta
now=datetime.now()
now_str=str(now)
YYYY=now_str[0:4]
MM=now_str[5:7]
dd=now_str[8:10]
hh=now_str[11:13]
mm=now_str[14:16]

A=int(YYYY+MM+dd)


url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'VcPx+a/ZUgz9pk9wlubqDmH8Us9onodXLXSJ0Af2/qObffixZEUGOkUjN8FOZtTz8HVCK3ZYCff0FHwgRLDLKw==', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('base_date') : A, quote_plus('base_time') : input("시간을 입력하세요 : "), quote_plus('nx') : '59', quote_plus('ny') : '123' })

rq = request.urlopen(url + queryParams)
rq.get_method = lambda: 'GET'
response_body = rq.read()

r_dict = json.loads(response_body)
r_response = r_dict.get("response")
r_body = r_response.get("body")
r_items = r_body.get("items")
r_item = r_items.get("item")

result = {}
for item in r_item:
        if(item.get("category") == "T1H"):
                result = item
                break
for item in r_item:
        if(item.get("category") == "RN1"):
                result2 = item
                break

print("시간 : ",result.get("baseTime")[:-2], "시")
print("예상온도 : " + result.get("obsrValue") + " C")
print("예상강수량 : " + result2.get("obsrValue") + " mm")

