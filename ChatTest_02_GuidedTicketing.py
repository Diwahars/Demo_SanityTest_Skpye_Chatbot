import unittest

from RestClient import RestClient
from ConfigManager import ConfigManager
from Response_from_API import Response_from_API


class ChatTest_GuidedTicketing(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_newticket_serviceDesk = ["hi", "please raise a ticket for me","mywipro is not working","Service Desk","bye"]
    inputstring_newticket_desktopService = ["hi", "please raise a ticket for me","my keyboard is not working",
                                            "Desktop Customer Support", "bye"]
    ticketID = ""

    resposne_instance = Response_from_API()

    def test_GuidedTicketing_NewTicket_ServiceDesk(self):
        """Test - able to raise Service now ticket """
        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_serviceDesk[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_serviceDesk[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Please provide the ticket description to raise the ticket in servicenow.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_serviceDesk[2])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Please select a category from the options: Custom Application Support,Service Desk')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_serviceDesk[3])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')

        ChatTest_GuidedTicketing.ticketID = convertunicode_to_string[211:222]
        self.assertTrue((convertunicode_to_string.startswith(
            'Ticket has been created in servicenow with following details:')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_serviceDesk[4])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_GuidedTicketing_NewTicket_DesktopService(self):
        """Test - able to raise Service now ticket """
        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_desktopService[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_desktopService[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Please provide the ticket description to raise the ticket in servicenow.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_desktopService[2])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith(
            'Please select a category from the options: Desktop/Laptop Customer Support,Service Desk')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_desktopService[3])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')

        ChatTest_GuidedTicketing.ticketID = convertunicode_to_string[211:222]
        self.assertTrue((convertunicode_to_string.startswith(
            'Ticket has been created in servicenow with following details:')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_newticket_desktopService[4])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    @staticmethod
    def get_active_ticketID():
        """id of the ticket in Service now"""
        return ChatTest_GuidedTicketing.ticketID

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_GuidedTicketing)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_GuidedTicketing)
    unittest.TextTestRunner(verbosity=2).run(suite)