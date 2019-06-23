# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os.path
import requests
import json
import smtplib
from rasa_core_sdk import Action
import mysql.connector
import datetime

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class ActionSendToken(Action):
    def name(self):
        return "action_send_token"

    def run(self, dispatcher, tracker, domain):
        mydb = mysql.connector.connect(host="35.166.18.143",user="emmanuel.annan",passwd="emmanuel.annan",database="webtech_emmanuel_annan")
        mycursor = mydb.cursor()
        f_name = tracker.get_slot('name')
        l_name = tracker.get_slot('last_name')
        # school = tracker.get_slot('last_name')
        # mycursor.execute("SELECT * FROM students WHERE first_name = '" + first_name + ')
        sql = "SELECT * FROM students WHERE first_name = %s AND last_name = %s"
        adr = (f_name,l_name)
        mycursor.execute(sql,adr)
        # mycursor.execute("SELECT * FROM students WHERE first_name = '" + first_name + "' AND last_name = '" +last_name +"'")
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            student = "Sorry " + f_name + " " + l_name +" you are not in our system"
        else:
            student = "Your personal login link is: https:/chalkedu.co/#/login/" + myresult[0][4] + "\nThe characters after the last slash make up your token\nKeep your link safe in your bookmarks!"
        dispatcher.utter_message(student)
        return []

class ActionEnrolStudent(Action):
    def name(self):
        return "action_enrol_student"

    def run(self, dispatcher, tracker, domain):
        mydb = mysql.connector.connect(host="35.166.18.143",user="emmanuel.annan",passwd="emmanuel.annan",database="webtech_emmanuel_annan")
        mycursor = mydb.cursor()
        course_name = tracker.get_slot('course_name')
        f_name = tracker.get_slot('name')
        l_name = tracker.get_slot('last_name')
        studentid = ""
        courseid = ""
        ##Getting course to insert
        sql = "SELECT course_id FROM courses WHERE course_title LIKE %s"
        args = ['%'+course_name+'%']
        mycursor.execute(sql, args)
        course_result = mycursor.fetchone()
        if(len(course_result)==0):
            course_response = "Sorry " + course + " does not exist"
            dispatcher.utter_message(course_response)
            return []
        courseid = course_result[0]
        ##Getting student_id to insert
        sql =  "SELECT student_id FROM students WHERE first_name = %s AND last_name = %s"
        adr = (f_name, l_name)
        mycursor.execute(sql,adr)
        student_result = mycursor.fetchone()
        if(len(student_result)==0):
            student_response = "Sorry " + f_name + " you are not in our system"
            dispatcher.utter_message(student_response)
            return []
        studentid = student_result[0]
        sql = "INSERT INTO student_courses (student_id, course_id) VALUES(%s, %s)"
        adr = (studentid, courseid)
        try:
            mycursor.execute(sql,adr)
        except:
            insert_response = "Looks like you are already registered for this course"
            dispatcher.utter_message(insert_response)
        dispatcher.utter_message(course_name + " " + f_name + " " + l_name)
        mydb.commit()

class ActionListAllCourses(Action):
    def name(self):
        return "action_list_all_courses"

    def run(self, dispatcher, tracker, domain):
        mydb = mysql.connector.connect(host="35.166.18.143",user="emmanuel.annan",passwd="emmanuel.annan",database="webtech_emmanuel_annan")
        mycursor = mydb.cursor()
        sql = "SELECT course_title FROM courses WHERE course_enabled = 1"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        dispatcher.utter_message("Here are the courses available at Chalkboard right now:")
        for i in result:
            dispatcher.utter_message(i[0])

class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):
        output = open('Output.txt')
        smtpserver='smtp.gmail.com:587'
        from_addr = 'insightnetwork.15@gmail.com'
        to_addr_list = ['insightnetwork.15@gmail.com']
        cc_addr_list = ['']
        subject = "Customer query I cannot handle"
        message = output.read()
        login = 'insightnetwork.15@gmail.com'
        password = 'fqpvbcjkwunvzqdk'
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        f_name = tracker.get_slot('name')
        l_name = tracker.get_slot('last_name')
        os.rename("Output.txt", "Errors/"+f_name +"_"+l_name+"_"+date+"_"+".txt")
        open('Output.txt', 'w').close()
        return problems

class ActionSendManual(Action):
    def name(self):
        return "action_send_manual"

    def run(self, dispatcher, tracker, domain):
        file = '30200106.pdf'
        response  = "You will find a complete walkthrough of the application here: https://drive.google.com/file/d/1gZfHbhaDabDfCz3dXBMMoSEnW6L2aAgs/view?usp=sharing"
        dispatcher.utter_attachment(response)

class ActionWriteLog(Action):
    def name(self):
        return "action_write_log"

    def run(self, dispatcher, tracker, domain):
        # with open('Output.txt', 'w') as f:
        #     for key, value in tracker.latest_action_name.items():
        #         f.write('%s:%s\n' % (key, value))
        op = ''
        if(os.path.isfile('Output.txt')):
            op = 'a'
        else:
            op = 'w'
        text_file = open("Output.txt",op)
        ##latest bot utterance via: tracker.lastest_bot_utterance
        text_file.write(tracker.latest_message['text']+'\n')
        text_file.close()
"""
class ActionSendToken(Action):
	def name(self):
		return "action_send_token"

	def run(self, dispatcher, tracker, domain):
		mydb = mysql.connector.connect(host="35.166.18.143",user="emmanuel.annan",passwd="emmanuel.annan",database="webtech_emmanuel_annan")
        mycursor = mydb.cursor()
        f_name = tracker.get_slot('name')
        l_name = tracker.get_slot('last_name')
        sql = "SELECT * FROM students WHERE first_name = %s AND last_name = %s"
        adr = (f_name,l_name)
        mycursor.execute(sql,adr)
	myresult = mycursor.fetchall()
		if len(myresult) == 0:
		    student = "Sorry " + f_name + " " + l_name +" you are not in our system"
		else:
			account_sid = "AC76cd680bb5124eda66ee5bbb80303c65"
			auth_token = "401bafdcb494987ec8e83b44ae622f7d"
			client = Client(account_sid, auth_token)

			message = client.messages \
					.create(
					     body="Your login token is: " + myresult[0][4]] + "\nKeep the token safe!",
					     from_='+13475234873',
					     to=myresult[0][3]
					 )
			student = "Your login URL has been sent to your phone number. Check and let me know if this was helpful"
			dispatcher.utter_message(student)
			return []"""
