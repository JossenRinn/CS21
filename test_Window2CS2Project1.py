from Window2CS2Project1 import *
import sys
import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import unittest

class Test(unittest.TestCase):
    def setup_method(self):
        self.p1 = Ui_SecondWindow()

    def teardown_method(self):
        del self.p1



    def test_defaults(self):
        self.assertEqual(self.p1.deposit_input.text(), '')
        self.assertEqual(self.p1.withdraw_input.text(), '')

    def test_deposit(self):
        self.p1.balancenumber_label.setText('100.00')
        self.p1.deposit_input.setText('400')
        QTest.mouseClick(self.p1.deposit_button, Qt.LeftButton)
        self.assertEqual(self.p1.balancenumber_label.text(), '$500.00')


    def test_withdraw(self):
        self.p1.balancenumber_label.setText('400.00')
        self.p1.deposit_input.setText('100')
        QTest.mouseClick(self.p1.withdraw_button, Qt.LeftButton)
        self.assertEqual(self.p1.balancenumber_label.text(), '$300.00')

if __name__ == '__main__':
    unittest.main()