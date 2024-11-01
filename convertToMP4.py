import codecs

def convertToMp4():
    links = []

    with codecs.open("download_links.txt", "r", "utf-8") as f:
        lines = f.readlines()
        for line in lines:
            links.append(line.replace(".apt?", ".mp4?"))

    with codecs.open("download_links.txt", "w", "utf-8") as f:
        for link in links:
            f.write(link)