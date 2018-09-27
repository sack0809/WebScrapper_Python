#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 09:45:11 2018

@author: playsafe
"""

from lxml import html
import requests
from lxml import etree

myURL="https://wiprodigital.com"
def create_xml():
        #global myURL
        page= requests.get(myURL)
        tree = html.fromstring(page.content)
        testExtract=tree.xpath('//a/@href')
        usrconfig = etree.Element("urls")
        usrconfig = etree.SubElement(usrconfig,"urls")
        for i in range(len( testExtract)):
                testVar= str(testExtract[i])
                if testVar.startswith(myURL) :
                    
                    
                        usr = etree.SubElement(usrconfig,"childurls")
                        usr.text = testVar
        tree = etree.ElementTree(usrconfig)
        tree.write("details.xml",encoding='utf-8', xml_declaration=True,pretty_print=True)

create_xml()


