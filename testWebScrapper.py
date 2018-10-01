#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 09:45:11 2018

@author: playsafe
"""


import requests
import xml.etree.ElementTree as ET
from lxml import etree,html


current_level = 0
visited = set()


myURL="https://wiprodigital.com"
queue = [myURL]

        
def conquer(childURL):
    global queue
    global visited
    #print("expanding Node " + childURL)
    p = requests.get(childURL)
    t = html.fromstring(p.content)
    child_nodes = t.xpath('//@href')
    root = etree.Element("root")
    new_nodes = [x for x in child_nodes if x not in list(visited) and x.startswith(myURL)]
    if new_nodes != []:
            child = etree.SubElement(root,"output")
            child.text = childURL 
            #print ("Child URL" + childURL)
            mydata = ET.tostring(child) 
            myfile = open("results.xml", "ab")  
            myfile.write(mydata+"\n".encode('ascii'))
            queue.extend(new_nodes)
        
    
    
def simpleWebScrap(current_level):
    global queue
    global visited
    for childURL in queue:
        if childURL.startswith(myURL) and childURL not in visited:
            visited.add(childURL)
            #print ("Parent URL :" + childURL)
            conquer(childURL)
           

def main ():
   simpleWebScrap(0)


if __name__ == "__main__": main()


        
            
        

