import essentials
import config
import json
from urllib.parse import quote
from urllib.request import Request, urlopen


def make_request(url):
    request = Request(url)
    request.add_header("X-Naver-Client-Id", essentials.client_id)
    request.add_header("X-Naver-Client-Secret", essentials.client_secret)

    return request


def make_url(node, kwrd, start, display):
    # https://openapi.naver.com/v1/search/news.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=sim
    base = "https://openapi.naver.com/v1/search"
    node = f"{node}.json"
    parameter = f"query={quote(kwrd)}&start={start}&display={display}"

    return f"{base}/{node}?{parameter}"


def get_response(request):
    try:
        return urlopen(request)
    except Exception as e:
        print(f"Error: {e}")
        return None


def naver_search(node, kwrd, start=1, display=config.CRAWLL_LIMIT):
    req = make_request(make_url(node, kwrd, start, display))
    response = get_response(req)

    if not response:
        return None

    res_code = response.getcode()

    if res_code == 200:
        pass
    else:
        print(f"HTTP Code: {res_code}")

    return response.read().decode("utf-8")


def save_at_file(file_name, data_dict):
    with open(f"{file_name}.json", "w", encoding="utf-8") as file:
        json.dump(data_dict, file, indent=4, ensure_ascii=False)


def main():
    node = "news"
    kwrd = "날씨"

    stream_json = naver_search(node, kwrd)

    if not stream_json:
        print("리퀘스트 실패")
        return

    save_at_file(f"{node}_naver_{kwrd}", json.loads(stream_json))


if __name__ == "__main__":
    main()

    # import time
    # from email.utils import formatdate

    # # pubDate = "Wed, 27 May 2026 10:40:00 +0900"
    # formatted_time = formatdate(time.time(), localtime=True)
    # print(formatted_time)

    # timeObj = time.strptime(formatted_time, "%a, %d %b %Y %H:%M:%S +0900")
    # print(timeObj)
