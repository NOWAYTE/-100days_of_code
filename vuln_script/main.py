#!/usr/bin/python3
import requests, json, time


def get(urlm=""):
    if not urlm:
        print("enter a valid url !")
        exit(0)
    url = 'https://app.pluralsight.com/learner/content/courses/' + urlm
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'okhttp/3.11.0'
    }
    print("\n")
    response = requests.get(url, headers=headers)
    modulesArray = json.loads(response.content.decode("utf-8")).get("modules")

    for i in range(len(modulesArray)):
        print(i, "==>", modulesArray[i].get("title"))
        clipsArray = modulesArray[i].get("clips")
        for clip in clipsArray:
            print("\t", clip.get("title"), "\t", clip.get("playerUrl"), "\n\n")
            post(clipId=clip.get("clipId"), clip_title=clip.get("title"))


def post(post="https://app.pluralsight.com/video/clips/v3/viewclip", clipId="", clip_title=""):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'okhttp/3.11.0'
    }
    print("Using Quality 1280x720\n Note=> IF Failed, try changing Quality OR Server!", "\n\n")

    data = r'{"clipId":"' + clipId + '","mediaType":"mp4","quality":"1280x720","online":true,"boundedContext":"course","versionId":"a2f8df11-2442-4b03-abd7-ff6836b4549d"}'

    response = requests.post(post, data=data, headers=headers)

    if response.status_code != 200:
        print(response.status_code, " user not authorized")
        return 0

    urlsArray = json.loads(response.content.decode("utf-8")).get("urls")
    print(f"{len(urlsArray)} Servers available for clip ==>{clip_title} :- \n", "@" * 50)
    for cdn in urlsArray:
        print("\t", cdn.get("url"), "\n")
    target = urlsArray[0].get("url")
    print("[+]Downloading from Server 1 ", target)
    print(f"{clip_title} , {clipId}")
    dnld_headers = {
        'User-Agent': 'okhttp/3.11.0'
    }
    info = requests.head(target, headers=dnld_headers)
    print("[+] %s.mp4 File lengtht=>%.2f MB" % (clip_title, int(info.headers['Content-Length']) / (1024 ** 2)))
    print("Downloading in progress ")
    mp4data = requests.get(target, headers=dnld_headers).content
    print("writing to disk...")
    with open(clip_title + '.mp4', "wb") as mp4file:
        mp4file.write(mp4data)
    print(f"Downloaded {clip_title}.mp4 !!!")
    print("*x*" * 50)
    time.sleep(5)


def main():
    print("\n", "*" * 20 + " By @ALoneGhost for | @RedBlueTM Hit | @Hide01) " + "*" * 20, "\n")
    try:
        print("enter public course Url \n(for example => "
              "https://app.pluralsight.com/library/courses/investigations-incident-management \n")
        get(urlm=input().split("/")[-1])

    except Exception as e:
        print("Problem:", e)


if __name__ == "__main__":
    main()
