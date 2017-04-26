# coding=utf-8
"""
Created on 27 Oct 2016 5:12 PM

@author : VI299221

"""
import json
import requests
import sys
sys.path.insert(0, r'./client')


class RestClient(object):
    """client for  rest-services"""

    def __init__(self):
        self.__headers_ = {"Content-Type": "application/json", "Accept": "application/json"}

    def post(self, url, data):
        """
                Send the request using post method
            :param url:
            :param data:
            :return :
        """
        print "*****************************************************"
	print "INPUT DATA                   :",json.dumps(data)
        response = requests.post(url, data=data, headers=self.__headers_, verify=False)
        data = response.json(strict=False)
        print "RESPONSE FROM THE CHATBOT    :", data['text']
        print "*****************************************************"
        return data

    def putWithPayload(self, url, data):
        """
                Send the request using post method
            :param url:
            :param data:
            :return :
        """
        response = requests.put(url, data=json.dumps(data), headers=self.__headers_)
        #data = response.json()
        return response 

    def get(self, url):
        """
            Send the request using get method
        :param url:

        """
        response = requests.get(url, headers=self.__headers_)
	print "response from HPSM"
	print response
        data = response.json()
        return data

    def put(self, url):
        """
            Send the request using get method
        :param url:

        """
        response = requests.put(url, headers=self.__headers_)
        data = response.json()
        return data