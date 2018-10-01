#!/bin/bash


pwd
PROPERTY_FILE=Webscrapper.properties
URL_NAME=`cat $PROPERTY_FILE | grep 'URL_NAME'| cut -d '=' -f2`
echo $URL_NAME
#rm -i results.xml
echo "WebScrapper is Running"
python testWebScrapper.py $URL_NAME
echo "WebScrapping Completed"
