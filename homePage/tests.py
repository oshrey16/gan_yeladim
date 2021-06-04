# -*- coding: utf-8 -*-
from django.test import TestCase
import datetime
from homePage.models import Message, kid, mashov, parent, subject,News, Question, Choice, Meeting, trackinglog 
from parentsPage.models import submission
from ganenetPage.models import myInfo
# Create your tests here.

class KidTestCase(TestCase):
    def setUp(self):
        #Create Kid
        kid.objects.create(id=123,firstName="Test",lastName="asd",
        birth_date=datetime.datetime(2020,1,1),favoriteColor="red",favoriteAnimal="Dog",
        siblingsNumber=2,parentName="Asdasd",
        parentPhone="0501111111",parentEmail="Test@gmail.com")

        #Create ganenet
        myInfo.objects.create(id=234,firstName="Testt",lastName="aasd",phoneNumber="0509554882",
        address="Asdasd",birthDate=datetime.datetime(2020,1,1))

        #Create Parent
        parent.objects.create(id="1111",firstName="PTest",lastName="PTest",
        kid = kid.objects.get(id="123"),
        birth_date=datetime.datetime(2020,1,1),
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

        #Create Mashov
        ##===AUTOMATIC CREATION===##

        #Create Trackinglog
        trackinglog.objects.create(kid = kid.objects.get(id="123"),message="test test")
		
    
    def test_kid(self):
        kid1 = kid.objects.get(id="123")
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
    
    def test_parent(self):
        kid1 = kid.objects.get(id="123")
        par1 = parent.objects.get(id="1111")
        self.assertEqual(par1.firstName,"PTest")
        self.assertEqual(par1.lastName,"PTest")
        self.assertEqual(par1.kid , kid1)
        date = datetime.datetime(2020,1,1)
        self.assertTrue(par1.birth_date.replace(microsecond=0),date)
        self.assertEqual(par1.parentPhone,"0501111111")
        self.assertEqual(par1.parentEmail,"Test@gmail.com")
    
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


    def test_Ganenet(self):
        gannenet1 = myInfo.objects.get(id=234)
        self.assertEqual(gannenet1.firstName,"Testt")
        self.assertEqual(gannenet1.lastName,"aasd")
        self.assertEqual(gannenet1.phoneNumber,"0509554882")
        self.assertEqual(gannenet1.address,"Asdasd")
        date = datetime.datetime(2020,1,1)
        self.assertTrue(gannenet1.birthDate.replace(microsecond=0),date)
    
    def test_GanenetUpdate(self):
        ganenet1 = myInfo.objects.get(id=234)
        ganenet1.firstName = "NewFirstName"
        ganenet1.lastName = "NewLastname"
        ganenet1.phoneNumber = "0501111111"
        ganenet1.address = "NewAddress"
        ganenet1.birthDate = datetime.date(1900,12,12)
        self.assertEqual(ganenet1.firstName,"NewFirstName")
        self.assertEqual(ganenet1.lastName,"NewLastname")
        self.assertEqual(ganenet1.phoneNumber,"0501111111")
        self.assertEqual(ganenet1.address,"NewAddress")
        self.assertTrue(ganenet1.birthDate,datetime.date(1900,12,12))
    
    def test_mashov(self):
        mashov1 = mashov.objects.get(subject= subject.objects.get(nameSubject="testSub"))
    
    def test_mashov_feedback(self):
        mashov1 = mashov.objects.get(subject= subject.objects.get(nameSubject="testSub"))
        mashov1.v1 = 2
        mashov1.v2 = 1
        mashov1.v3 = 5
        mashov1.v4 = 6
        mashov1.v5 = 2
        self.assertEqual(mashov1.v1,2)
        self.assertEqual(mashov1.v2,1)
        self.assertEqual(mashov1.v3,5)
        self.assertEqual(mashov1.v4,6)
        self.assertEqual(mashov1.v5,2)

    def test_trackinglog(self):
        kid1 = kid.objects.get(id="123")
        tlog = trackinglog.objects.get(kid = kid1)
        self.assertEqual(tlog.message,"test test")

    ######### integration tests #########
    def test_kids(self):
        kids = kid.objects.filter(id="999999999")
        self.assertEqual(kids.count(),0)

        kid.objects.create(id=999999999,firstName="Test",lastName="asd",
        birth_date=datetime.datetime(2020,1,1),favoriteColor="red",favoriteAnimal="Dog",
        siblingsNumber=2,parentName="Asdasd",
        parentPhone="0501111111",parentEmail="Test@gmail.com")

        kids = kid.objects.filter(id="999999999")
        self.assertEqual(kids.count(),1)
    
    def test_subject_mashov(self):
        subjects = subject.objects.filter(nameSubject="TestSubject")
        self.assertEqual(subjects.count(),0)
        mashovs = mashov.objects.filter(subject = subject.objects.filter(nameSubject="TestSubject"))
        self.assertEqual(subjects.count(),0)

        #create subject
        subject.objects.create(nameSubject="TestSubject",songs="songtest",selfTasks="testTasks")
        #mashov created Auto!
        subjects = subject.objects.filter(nameSubject="TestSubject")
        mashovs = mashov.objects.filter(subject = subject.objects.filter(nameSubject="TestSubject"))
        self.assertEqual(subjects.count(),1)
        self.assertEqual(mashovs.count(),1)
    
    def test_trackinglog_kid(self):
        kids = kid.objects.filter(id="111000111")
        self.assertEqual(kids.count(),0)
        trackinglogs = trackinglog.objects.filter(kid = kid.objects.filter(id="111000111"))
        self.assertEqual(trackinglogs.count(),0)
        
        #create kid and check
        kid1 = kid.objects.create(id="111000111",firstName="Test",lastName="asd",
        birth_date=datetime.datetime(2020,1,1),favoriteColor="red",favoriteAnimal="Dog",
        siblingsNumber=2,parentName="Asdasd",
        parentPhone="0501111111",parentEmail="Test@gmail.com")
        kids = kid.objects.filter(id="111000111")
        self.assertEqual(kids.count(),1)

        #create trackinglog
        trackinglog.objects.create(kid = kid1)
        trackinglog1 = trackinglog.objects.filter(kid=kid1)
        self.assertEqual(trackinglog1.count(),1)
    
    def test_Survey_system(self):
        Question1 = Question.objects.filter(question_text='qtest')
        self.assertEqual(Question1.count(),0)
        Choice1 = Choice.objects.filter(question = Question.objects.filter(question_text='qtest'))
        self.assertEqual(Choice1.count(),0)

        #create Qustion
        q = Question.objects.create(question_text='qtest')
        Choice.objects.create(question = q, choice_text="text1")
        Choice.objects.create(question = q, choice_text="text2")
        Choice.objects.create(question = q, choice_text="text3")
        q = Question.objects.filter(question_text='qtest')
        self.assertEqual(q.count(),1)
        Choices = Choice.objects.filter(question = Question.objects.filter(question_text='qtest'))
        self.assertEqual(Choices.count(),3)

        #vote
        c1 = Choices.all().get(choice_text="text1")
        c2 = Choices.all().get(choice_text="text2")
        c3 = Choices.all().get(choice_text="text3")
        c1.votes = 1
        c2.votes = 2
        c3.votes = 3
        self.assertEqual(c1.votes,1)
        self.assertEqual(c2.votes,2)
        self.assertEqual(c3.votes,3)