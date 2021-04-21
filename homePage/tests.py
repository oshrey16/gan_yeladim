# -*- coding: utf-8 -*-

from django.test import TestCase
import datetime
from homePage.models import kid,subject,News
from parentsPage.models import submission

# Create your tests here.

class KidTestCase(TestCase):
    def setUp(self):
        #Create Kid
        kid.objects.create(id=123,firstName="Test",lastName="asd",
        birth_date=datetime.datetime(2020,1,1),favoriteColor="red",favoriteAnimal="Dog",
        siblingsNumber=2,parentName="Asdasd",
        parentPhone="0501111111",parentEmail="Test@gmail.com")

        #Create Subject
        subject.objects.create(nameSubject="testSub",songs="songtest",selfTasks="testTasks")

        #Create News
        News.objects.create("TestNews","TestTestTest")
    
    def test_kid(self):
        kid1 = kid.objects.get(id=123)
        self.assertEqual(kid1.firstName,"Test")
        self.assertEqual(kid1.lastName,"asd")
        date = datetime.datetime(2020,1,1)
        self.assertTrue(kid1.birth_date.replace(microsecond=0),date)
        self.assertEqual(kid1.favoriteColor,"red")
        self.assertEqual(kid1.favoriteAnimal,"Dog")
        self.assertEqual(kid1.siblingsNumber,2)
        self.assertEqual(kid1.parentName,"Asdasd")
        self.assertEqual(kid1.parentPhone,"0501111111")
        self.assertEqual(kid1.parentEmail,"Test@gmail.com")
    
    def test_subject(self):
        sub1 = subject.objects.get(nameSubject="testSub")
        self.assertEqual(sub1.songs,"songtest")
        self.assertEqual(sub1.selfTasks,"testTasks")

    def test_postSubmission(self):
        kid1 = kid.objects.get(id=123)
        sub1 = subject.objects.get(nameSubject="testSub")
        sub = submission.objects.create(kidId=kid1,subjectName=sub1)
    
    def test_News(self):
        test1 = subject.objects.get()