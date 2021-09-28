import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistroy.com")
# print(res.status_code)
# requests.codes.ok

#  바로 오류출력 프로그램 종로
res.raise_for_status()
print("continue", len(res.text))
with open("google.html", "w", encoding="utf-8") as f:
    f.write(res.text)
