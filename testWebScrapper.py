#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 09:45:11 2018

@author: playsafe
"""

from lxml import html
import requests
from lxml import etree


def create_xml():
        page= requests.get("http://wiprodigital.com")
        tree = html.fromstring(page.content)
        testExtract=tree.xpath('//a/@href')
        usrconfig = etree.Element("urls")
        usrconfig = etree.SubElement(usrconfig,"urls")
        for user in range(len( testExtract)):
                usr = etree.SubElement(usrconfig,"childurls")
                usr.text = str(testExtract[user])
        tree = etree.ElementTree(usrconfig)
        tree.write("details.xml",encoding='utf-8', xml_declaration=True,pretty_print=True)

create_xml()
