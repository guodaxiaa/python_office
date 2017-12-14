#!/usr/bin/python
#coding:utf-8
#单元测试练习
import unittest
from Student import Student
class TestStudent(unittest.TestCase):
    def test_80_100(self):
        s1=Student('lucy',80)
        s2=Student('lily',95)
        self.assertEqual(s1.get_grade(),'A')
        self.assertEqual(s2.get_grade(),'A')
    def test_60_80(self):
        s1=Student('lucy',60)
        s2=Student('lily',79)
        self.assertEqual(s1.get_grade(),'B')
        self.assertEqual(s2.get_grade(),'B')
    def test_0_60(self):
        s1=Student('lucy',0)
        s2=Student('lily',59)
        self.assertEqual(s1.get_grade(),'C')
        self.assertEqual(s2.get_grade(),'C')
    def test_invalid(self):
        s1=Student('lucy',-1)
        s2=Student('lily',101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
if __name__ =='__main__':
    unittest.main()
