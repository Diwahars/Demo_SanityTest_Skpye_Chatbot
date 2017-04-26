# -*- coding: utf-8 -*-
import unittest
from RestClient import RestClient
from Response_from_API import Response_from_API
from ConfigManager import ConfigManager

class ChatTest_SOP(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_hrpolicy_wbsclaim = ["hi", "what is the education allowance as part of WBS?","bye"]
    inputstring_hrpolicy_mediclaim = ["hi",  "how can i claim for medical reimbursement?","bye"]
    inputstring_hrpolicy_leave = ["hi", "how many leaves do i have while in probation","bye"]
    inputstring_hrpolicy_annualleave = ["hi", "How Annual leave encashment calculated ?","bye"]

    resposne_instance = Response_from_API()

    def test_SOP_HRPolicy_WBSClaims(self):
        """To test the SOP_MASClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_wbsclaim[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_wbsclaim[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.3 Education Allowance as part of WBS')) and (
            convertunicode_to_string.endswith('hostel fee could be produced once in a quarter.')))


        response = self.resposne_instance.input_value_json(self,self.inputstring_hrpolicy_wbsclaim[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_SOP_HRPolicy_Mediclaim(self):
        """To test the SOP_MediClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.4 Allowed under MAS')) and (
            convertunicode_to_string.endswith('diagnosis and treatment of specified illness.')))

        response = self.resposne_instance.input_value_json(self,self.inputstring_hrpolicy_mediclaim[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPolicy_Leave(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.6 Leaves during probation')) and (
            convertunicode_to_string.endswith('start earning 1.75 days of leave every month.')))

        response = self.resposne_instance.input_value_json(self,self.inputstring_hrpolicy_leave[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_SOP_Annual_Leave(self):
        """To test the SOP_AnnualLeave Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.2 Annual leave encashment calculated')) and (
            convertunicode_to_string.endswith('(WBP + *Special Allowance + Provision for car for 1 month)) / 30')))


        response = self.resposne_instance.input_value_json(self,self.inputstring_hrpolicy_annualleave[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_SOP)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_SOP)
    unittest.TextTestRunner(verbosity=2).run(suite)



    print "Finish"