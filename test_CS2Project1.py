from CS2Project1 import *
import sys
import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import unittest


class Test(unittest.TestCase):
    def setup_method(self):
        self.p1 = Ui_MainWindow()

    def teardown_method(self):
        del self.p1



    def test_defaults(self):
        self.assertEqual(self.p1.username_input.text(), '')
        self.assertEqual(self.p1.password_input.text(), '')

    def test_openWindow(self):
        self.p1.username_input.setText('user1')
        self.p1.password_input.setText('password1')
        assert self.p1.ui.balancenumber_label.text == '$100.00'

        self.p1.username_input.setText('ur2')
        self.p1.password_input.setText('password2')
        assert self.p1.errormessage_label.text == 'Error- Username and/or Password do not match.'

        self.p1.username_input.setText('user3')
        self.p1.password_input.setText('incorrect')
        assert self.p1.errormessage_label.text == 'Error- Username and/or Password do not match.'

if __name__ == '__main__':
    unittest.main()