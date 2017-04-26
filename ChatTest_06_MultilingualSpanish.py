# -*- coding: utf-8 -*-
import unittest

from RestClient import RestClient
from ConfigManager import ConfigManager
from Response_from_API import Response_from_API

class ChatTest_MultiLingualSpanish(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_notscheduled = ["hola", "reiniciar server", "uno", "12.34.56.12", "16:07 28/05/2017", "no"]
    inputstring_scheduled = ["hola", "reiniciar server", "uno", "12.34.56.12", "16:07 28/05/2017", "si"]

    def test_ServerReboot_OneServer_Scheduled_Cancel(self):
        """To test - able to reboot the server"""
        response = Response_from_API.input_value_json(self, self.inputstring_notscheduled[0])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue(convertunicode_to_string.startswith("hola, Soy tu Bot de TI. Puedo ayudarle con sus problemas"))


        response = Response_from_API.input_value_json(self, self.inputstring_notscheduled[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertEquals("Desea reiniciar uno o varios servidores? Escriba uno o varios.", convertunicode_to_string)

        response = Response_from_API.input_value_json(self, self.inputstring_notscheduled[2])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertEquals("Proporcione el nombre de host o ip del servidor?", convertunicode_to_string)

        response = Response_from_API.input_value_json(self, self.inputstring_notscheduled[3])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue(convertunicode_to_string.endswith("como GMT."))


        response = Response_from_API.input_value_json(self, self.inputstring_notscheduled[4])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertEquals(
            "Desea reiniciar 12.34.56.12 en 16:07 28/05/2017.Por favor confirme para continuar (si / no).",
            convertunicode_to_string)

        response = Response_from_API.input_value_json(self, self.inputstring_notscheduled[5])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertEquals(" Gracias, que tengas un gran dia", convertunicode_to_string)

    def test_ServerReboot_OneServer_Scheduled(self):
        """To test - able to reboot the server scenario with invalid scenario"""
        response = Response_from_API.input_value_json(self, self.inputstring_scheduled[0])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue(convertunicode_to_string.startswith("hola, Soy tu Bot de TI. Puedo ayudarle con sus problemas"))

        response = Response_from_API.input_value_json(self, self.inputstring_scheduled[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertEquals("Desea reiniciar uno o varios servidores? Escriba uno o varios.", convertunicode_to_string)

        response = Response_from_API.input_value_json(self, self.inputstring_scheduled[2])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertEquals("Proporcione el nombre de host o ip del servidor?", convertunicode_to_string)

        response = Response_from_API.input_value_json(self, self.inputstring_scheduled[3])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue(convertunicode_to_string.endswith("como GMT."))

        response = Response_from_API.input_value_json(self, self.inputstring_scheduled[4])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertEquals(
            "Desea reiniciar 12.34.56.12 en 16:07 28/05/2017.Por favor confirme para continuar (si / no).",
            convertunicode_to_string)

        response = Response_from_API.input_value_json(self, self.inputstring_scheduled[5])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue(convertunicode_to_string.endswith("en 16:07 28/05/2017. Gracias que tenga un gran dia."))


    @staticmethod
    def suite():
            """TestProject for this class"""
            suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_MultiLingualSpanish)
            unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChatTest_MultiLingualSpanish)
    unittest.TextTestRunner(verbosity=2).run(suite)