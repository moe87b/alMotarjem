import praw
import pdb
import re
import os
import mysql.connector
from mysql.connector import Error
from googletrans import Translator

connection = mysql.connector.connect(host='sql7.freemysqlhosting.net',
                                         database='sql7354856',
                                         user='sql7354856',
                                         password='x7iHmNhExD')    
cursor = connection.cursor()
cursor.execute("SELECT * FROM replied")
result = cursor.fetchall()
realRes = []

for entry in result:
    realRes.append(entry[0])

print(realRes)



translator = Translator()
reddit = praw.Reddit(client_id='2Qv7SGX2aP_3_A',
                    client_secret='pYjb2DsMz1l1XTt5n_T2zfNbg4c',
                    user_agent='<leb motarjem>',
                    username='alMotarjem',
                    password='tarjem31387875244*')
subredditsArray = ['AlMotarjem', 'lebanese']

for sub in subredditsArray:
    subreddit = reddit.subreddit(sub):
    for comment in subreddit.comments(limit=20):
        commentBody = comment.body
        
        if( ('!tarjem' in commentBody) and comment.id not in realRes):
            print("inside")
            if( type(comment.parent()) is praw.models.reddit.submission.Submission):
                insertsql = "INSERT INTO replied (identifier) VALUES ('"+comment.id+"')"
                print("replying to post")
                finalReply = ""
                title = comment.parent().title
                titleLanguage = translator.detect(comment.parent().title)
                if titleLanguage.lang == 'ar':
                    translatedTitle = translator.translate(title)    
                    finalReply = "Title: "+translatedTitle.text+"\n \n"
                body = comment.parent().selftext
                bodyLanguage = translator.detect(body).lang 
                if bodyLanguage == 'ar':
                    translatedBody = translator.translate(body)    
                    finalReply = finalReply + "Post: "+translatedBody.text+" \n \n"
                if finalReply == "" :
                    #print("I can only translate from arabic to english" )
                    comment.reply("I can only translate from arabic to english")
                    cursor.execute(insertsql)
                else:
                    #print(finalReply+" \n \n +^(I am bot, I work using google translate)")
                    comment.reply(finalReply+" \n \n ^(I am bot, I work using google translate)")
                    cursor.execute(insertsql)
            else:
                body = comment.parent().body
                commentLanguage = translator.detect(body)
                finalReply = ""
                if(commentLanguage.lang =='ar'):
                    finalReply = translator.translate(body).text
                    finalReply =finalReply+" \n \n ^(I am a bot, I work using google translate)"
                    #print(finalReply)
                    cursor.execute(insertsql)
                    comment.reply(finalReply)
                else:
                    #print("I can only translate arabic text")
                    comment.reply("I can only translate arabic text")
                    cursor.execute(insertsql)
        connection.commit()

    