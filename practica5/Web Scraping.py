#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import re


def tel():
    page = requests.get("https://www.uanl.mx")
    soup = bs(page.content, "html.parser")

 
    Telefono = re.compile(r'[(]\d{2}[)]\s\d{4}[-.]\d{4}')

    po = soup.find_all("p")

    for i in range(len(po)):
        pageText = po[i].getText()
        temp = Telefono.findall(pageText)
        if temp:
            print("El teléfono encontrado es el siguiente:", Telefono.findall(pageText))


tel()
