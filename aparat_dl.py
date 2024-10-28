import getTitles
import getLinks
import getDownloadLinks
import convertToMP4
import downloader

url = input("Enter The Aparat Playlist Url: ")

print("Getting Titles and writing to titles.txt: ")
getTitles.get_titles(url)
print("Getting Links and writing to links.txt: ")
getLinks.get_links(url)
print("Getting download links and writing to download_links.txt: ")
getDownloadLinks.get_download_links(url)
convertToMP4.convertToMp4()
print("It's time to download :)")
downloader.download()