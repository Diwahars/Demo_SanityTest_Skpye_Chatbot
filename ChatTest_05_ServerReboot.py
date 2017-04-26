
import unittest
from ConfigManager import ConfigManager
from RestClient import RestClient
from Response_from_API import Response_from_API


class ChatTest_ServerReboot(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_notscheduled =["hi","server reboot","one","12.34.56.12","16:07 28/05/2017","no"]
    inputstring_scheduled = ["hi", "server reboot", "one", "12.34.56.12", "16:07 28/05/2017", "yes"]

    def test_ServerReboot_OneServer_Scheduled_Cancel(self):
            """To test - able to reboot the server"""
            response = Response_from_API.input_value_json(self,self.inputstring_notscheduled[0])
            self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.", response['text'])


            response = Response_from_API.input_value_json(self,self.inputstring_notscheduled[1])
            self.assertEquals("Would you like to reboot one or multiple servers ? Type One or Multiple.",response['text'])


            response = Response_from_API.input_value_json(self,self.inputstring_notscheduled[2])
            self.assertEquals("Please provide hostname or ip of the server ?",response['text'])


            response = Response_from_API.input_value_json(self,self.inputstring_notscheduled[3])
            self.assertEquals("When would you like to reboot the server 12.34.56.12? Enter in the following format hh:mm dd/mm/yyyy. NOTE:All times will be taken as GMT.", response['text'])


            response = Response_from_API.input_value_json(self,self.inputstring_notscheduled[4])
            self.assertEquals("You would like to reboot 12.34.56.12 at 16:07 28/05/2017.Please confirm to proceed (yes/no).",
                response['text'])


            response = Response_from_API.input_value_json(self,self.inputstring_notscheduled[5])
            self.assertEquals("Thank you, have a Great Day.",response['text'])

    def test_ServerReboot_OneServer_Scheduled(self):
            """To test - able to reboot the server scenario with invalid scenario"""
            response = Response_from_API.input_value_json(self, self.inputstring_scheduled[0])
            self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                              response['text'])

            response = Response_from_API.input_value_json(self, self.inputstring_scheduled[1])
            self.assertEquals("Would you like to reboot one or multiple servers ? Type One or Multiple.", response['text'])

            response = Response_from_API.input_value_json(self, self.inputstring_scheduled[2])
            self.assertEquals("Please provide hostname or ip of the server ?", response['text'])

            response = Response_from_API.input_value_json(self, self.inputstring_scheduled[3])
            self.assertEquals(
                "When would you like to reboot the server 12.34.56.12? Enter in the following format hh:mm dd/mm/yyyy. NOTE:All times will be taken as GMT.",
                response['text'])

            response = Response_from_API.input_value_json(self, self.inputstring_scheduled[4])
            self.assertEquals(
                "You would like to reboot 12.34.56.12 at 16:07 28/05/2017.Please confirm to proceed (yes/no).",
                response['text'])

            response = Response_from_API.input_value_json(self, self.inputstring_scheduled[5])
            self.assertEquals(" Server 12.34.56.12 will be rebooted at 16:07 28/05/2017. Thank you, have a Great Day.",
                              response['text'])

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_ServerReboot)
        unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_ServerReboot)
    unittest.TextTestRunner(verbosity=2).run(suite)



