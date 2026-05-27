import essentials
import json
import urllib.request
import datetime
import time

CRAWLL_LIMIT = 1


def get_response(url):
    """데이터 가져오기(MAVER)"""
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", essentials.client_id)
    req.add_header("X-Naver-Client-Secret", essentials.client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print(f"[{datetime.datetime.now()}] URL REQUEST SUCCESS")
            # print(f"response: {response.read().decode("utf-8")}")
            return response.read().decode("utf-8")

    except Exception as e:
        print(f"[{datetime.datetime.now()}] URL REQUEST FAIL")
        print(e)
        return None


def get_naver_search(node, search_kwrd, start, display):
    """데이터 검색(NAVER)"""
    base = "https://openapi.naver.com/v1/search"
    node = f"{node}.json"
    url = f"{base}/{node}?query={urllib.parse.quote(search_kwrd)}&start={start}&display={display}"

    response_decoded = get_response(url)

    if response_decoded == None:
        return None
    else:
        return json.loads(response_decoded)


def getPostData(post, jsonResult, cnt):
    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]
    pDate = datetime.datetime.strptime(post["pubDate"], "%a, %d %b %Y %H:%M:%S +0900")
    pDate = pDate.strftime("%Y-%m-%d %H:%M:%S")

    jsonResult.append(
        {
            "cnt": cnt,
            "title": title,
            "description": description,
            "org_link": org_link,
            "link": link,
            "pDate": pDate,
        }
    )

    pass


def main():
    node = "news"
    search_kwrd = input("검색어: ")

    json_result = []
    json_response = get_naver_search(node, search_kwrd, 1, CRAWLL_LIMIT)

    count = 0

    while json_response != None and json_response["display"] != 0 and count < 5:
        for post in json_response["items"]:
            getPostData(post, json_result, count)

        json_response = get_naver_search(
            node,
            search_kwrd,
            json_response["start"] + json_response["display"],
            CRAWLL_LIMIT,
        )

        count += 1

    with open(f"{search_kwrd}_naver_{node}.json", "w", encoding="utf-8") as file:
        json.dump(json_result, file, indent=4, sort_keys=True, ensure_ascii=False)
        # file.write(json_file)


if __name__ == "__main__":
    main()
