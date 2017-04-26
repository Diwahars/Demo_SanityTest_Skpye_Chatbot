import unittest

from RestClient import RestClient
from ChatTest_02_GuidedTicketing import ChatTest_GuidedTicketing
from Response_from_API import Response_from_API
from ConfigManager import ConfigManager

class ChatTest_TicketQuerying(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_tikcetstatus = ["hi","please let me know the status of ticket ",
                    "bye"]


    resposne_instance = Response_from_API()

    def test_TicketQuery_TicketStatus_Valid(self):
        activeticket_id = ChatTest_GuidedTicketing.ticketID
        """To test - able to see the valid ticket status"""
        response = self.resposne_instance.input_value_json(self, self.inputstring_tikcetstatus[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_tikcetstatus[1]+activeticket_id)
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Following is the status:')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_tikcetstatus[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_TicketQuery_TicketStatus_Invalid(self):
        """To test - able to see the invalid ticket status"""
        response = self.resposne_instance.input_value_json(self, self.inputstring_tikcetstatus[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_tikcetstatus[1]+"ICN0000000")
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Ticket Details not found')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_tikcetstatus[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])
    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_TicketQuerying)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_TicketQuerying)
    unittest.TextTestRunner(verbosity=2).run(suite)