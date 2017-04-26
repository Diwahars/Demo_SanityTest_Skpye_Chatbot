# -*- coding: utf-8 -*-
import unittest

from RestClient import RestClient
from ConfigManager import ConfigManager
from ChatTest_02_GuidedTicketing import ChatTest_GuidedTicketing
from Response_from_API import Response_from_API

class ChatTest_MultilingualHindi(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_ticketstatus = ["hi", " टिकट की स्थिति क्या है?","bye"]
    ticketID = ""

    resposne_instance = Response_from_API()

    def test_TicketQuery_TicketStatus_Valid(self):
        """To test - able to see the valid ticket status"""
        activeticket_id = ChatTest_GuidedTicketing.ticketID
        response = self.resposne_instance.input_value_json(self, self.inputstring_ticketstatus[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])
        print "Returned value",ChatTest_GuidedTicketing.ticketID
        response = self.resposne_instance.input_value_json(self, activeticket_id+self.inputstring_ticketstatus[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Following is the status:')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_ticketstatus[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_TicketQuery_TicketStatus_Invalid(self):
        """To test - able to see the invalid ticket status"""
        response = self.resposne_instance.input_value_json(self, self.inputstring_ticketstatus[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self,  "ICN0000000 टिकट की स्थिति क्या है?")
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Ticket Details not found')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_ticketstatus[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_MultilingualHindi)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_MultilingualHindi)
    unittest.TextTestRunner(verbosity=2).run(suite)