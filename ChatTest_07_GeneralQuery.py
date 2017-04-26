# -*- coding: utf-8 -*-
import unittest

from RestClient import RestClient
from ConfigManager import ConfigManager
from Response_from_API import Response_from_API


class ChatTest_GeneralQuery(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_general_gandhi = ["hi", "who is Indira Gandhi", "bye"]
    inputstring_general_trump = ["hi", "who is Donald Trump", "bye"]
    inputstring_general_holmes = ["hi", "what is wipro holmes", "bye"]
    resposne_instance = Response_from_API()

    def test_GeneralQuery_IndiraGandhi(self):
        """Test - able to assert the  General Query"""
        response = Response_from_API.input_value_json(self, self.inputstring_general_gandhi[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])
        response = Response_from_API.input_value_json(self, self.inputstring_general_gandhi[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            "Indira Priyadarshini Gandhi was an Indian politician and central figure of the")))

        response = self.resposne_instance.input_value_json(self, self.inputstring_general_gandhi[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_GeneralQuery_DonaldTrump(self):
        """Test - able to assert the  General Query"""
        response = Response_from_API.input_value_json(self, self.inputstring_general_trump[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])
        response = Response_from_API.input_value_json(self, self.inputstring_general_trump[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            "Donald John Trump (born June 14, 1946) is the 45th and current President of the")))

        response = self.resposne_instance.input_value_json(self, self.inputstring_general_trump[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_GeneralQuery_WiproHolmes(self):
        """Test - able to assert the  General Query"""
        response = Response_from_API.input_value_json(self, self.inputstring_general_holmes[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])
        response = Response_from_API.input_value_json(self, self.inputstring_general_holmes[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            "Wipro HOLMES  Artificial Intelligence Platform is a rich set of cognitive")))

        response = self.resposne_instance.input_value_json(self, self.inputstring_general_holmes[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])
    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_GeneralQuery)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_GeneralQuery)
    unittest.TextTestRunner(verbosity=2).run(suite)