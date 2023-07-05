#!/usr/bin/env python
from html.parser import HTMLParser
import os
import shutil
import requests
from bs4 import BeautifulSoup
import threading

def fromIndexToList(index: requests.Response):
    soup = BeautifulSoup(index.content, 'html.parser');
    anchors = soup.find_all('a');
    elemList = [];
    for anchor in anchors:
        elemList.append(anchor["href"]);
    return (elemList);


def downloaderEngine(url: str, currPath: str, dirList: list[str]):
    subThread = None;
    for dirName in dirList:
        if len(dirName) == 27 and dirName[-1] == '/':
            dirPath = currPath + dirName;
            if not os.path.exists(dirPath):
                os.makedirs(dirPath, exist_ok=True)
            tempIndex = requests.get(url + dirPath, allow_redirects=True)
            elemList = fromIndexToList(tempIndex)
            subThread = threading.Thread(
                target=downloaderEngine,
                args=(url, currPath + dirName, elemList)
            );
            subThread.start()
        elif dirName[-1] != '/':
            downloadedFile = requests.get(url + currPath + dirName, allow_redirects=True)
            if not os.path.exists(currPath):
                os.makedirs(currPath, exist_ok=True)
            fd = open(currPath + dirName, "w")
            fd.write(downloadedFile.content.decode())
            fd.close()
    if subThread != None:
        subThread.join()

def main():
    url = "http://172.16.91.134/";
    rootIndex = requests.get(url + '.hidden/', allow_redirects=True);
    if not os.path.exists(".hidden"):
        os.mkdir(".hidden");
    rootElemList = fromIndexToList(rootIndex)
    downloaderEngine(url, ".hidden/", rootElemList)
    os.rename(".hidden", "hidden")

if os.path.exists("hidden"):
    shutil.rmtree("hidden")
main()
