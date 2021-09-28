import requests

url = "https://nadocoding.tistory.com/"
headers = {
    "User-Ajent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
res = requests.get(url, headers=headers)
# res = requests.get("http://nadocoding.tistroy.com")
# print(res.status_code)
# requests.codes.ok

#  바로 오류출력 프로그램 종로
res.raise_for_status()
print("continue", len(res.text))
with open("tistroy.html", "w", encoding="utf-8") as f:
    f.write(res.text)
