# -*- coding: utf-8 -*-
from django.test import TestCase
import datetime
from homePage.models import kid,subject,News, Question, Choice, Meeting
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
        News.objects.create(title="TestNews",content="TestTestTest")
		
		#Create Question
        #Question.objects.create(question_text="TEST")
		
		#Create Choice
        Choice.objects.create(question=Question.objects.create(question_text="TEST"), choice_text="TEST1",votes=1)

        #Create Meeting
        Meeting.objects.create(Meeting_Link="test", date="test1")
		
    
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
        for x in News.objects.all():
            if(x.title=="TestNews"):
                self.assertEqual(x.title,"TestNews")
                self.assertEqual(x.content,"TestTestTest")
                date = datetime.datetime(1900,1,1)
                #x.ticket_date = date
                self.assertNotEqual(x.ticket_date.replace(microsecond=0),date)
            else:
                self.assertNotContains()
    
    def test_Question_Choices(self):
        for x in Question.objects.all():
            if(x.question_text=="TEST"):
                for c in Choice.objects.all():
                    if(c.question == x):
                        self.assertEqual(c.votes,1)
                        self.assertEqual(c.choice_text,"TEST1")

    def test_Meeting(self):
        meet1 = Meeting.objects.get(Meeting_Link="test")
        self.assertEqual(meet1.date,"test1")
