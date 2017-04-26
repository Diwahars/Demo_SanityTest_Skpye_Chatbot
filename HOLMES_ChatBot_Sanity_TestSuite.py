# coding=utf-8

import unittest


from ChatTest_01_SOP import ChatTest_SOP
from ChatTest_02_GuidedTicketing import ChatTest_GuidedTicketing
from ChatTest_03_TicketQuerying import ChatTest_TicketQuerying
from ChatTest_04_MultilingualHindi import ChatTest_MultilingualHindi
from ChatTest_05_ServerReboot import ChatTest_ServerReboot
from ChatTest_06_MultilingualSpanish import ChatTest_MultiLingualSpanish
from ChatTest_07_GeneralQuery import ChatTest_GeneralQuery


class TestSuite_Check(unittest.TestCase):

        if __name__ == '__main__':
                loader = unittest.TestLoader()
                module1 = ChatTest_SOP.suite()
                module2 = ChatTest_GuidedTicketing.suite()
                module3 = ChatTest_TicketQuerying.suite()
                module4 = ChatTest_MultilingualHindi.suite()
                module5 = ChatTest_ServerReboot.suite()
                module6 = ChatTest_MultiLingualSpanish.suite()
                module7 = ChatTest_GeneralQuery.suite()
                suite = unittest.TestSuite([module1,module2,module3,module4,module5,module6,module7])
                unittest.TextTestRunner(verbosity=2).run(suite)


