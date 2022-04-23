import requests
import random
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
  "Host": "rovskin-th.com",
  "content-length": "59",
  "accept": "*/*",
  "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-mobile": "?0",
  "user-agent": ua.random,
  "sec-ch-ua-platform": "Android",
  "origin": "https://rovskin-th.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://rovskin-th.com/"
}

data = {
  "type":"Facebook",
  "taikhoan":random.choice(ua.chrome),+"@gmail.",
  "matkhau":"3838282iekks"
}

for i in range(1000):
  name = requests.post("https://rovskin-th.com/assets/ajax/tocchien.php",data=data, headers=headers)
  print(name.text)