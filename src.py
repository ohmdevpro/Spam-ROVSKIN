import requests

headers = {
  "Host": "rovskin-th.com",
  "content-length": "59",
  "accept": "*/*",
  "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  "x-requested-with": "XMLHttpRequest",
  "sec-ch-ua-mobile": "?0",
  "user-agent": "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
  "sec-ch-ua-platform": "Android",
  "origin": "https://rovskin-th.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://rovskin-th.com/"
}

data = {
  "type":"Facebook",
  "taikhoan":"Ihere@hee.com",
  "matkhau":"3838282iekks"
}

for i in range(1000):
  name = requests.post("https://rovskin-th.com/assets/ajax/tocchien.php",data=data, headers=headers)
  print(name.text)