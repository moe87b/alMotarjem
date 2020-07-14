import praw
import pdb
import re
import os
from googletrans import Translator

file = open("replied.txt", "r+")
repliedRaw = file.readlines()
replied = []
for entry in repliedRaw:
    replied.append(entry[:-1])


translator = Translator()
reddit = praw.Reddit(client_id='2Qv7SGX2aP_3_A',
                    client_secret='pYjb2DsMz1l1XTt5n_T2zfNbg4c',
                    user_agent='<leb motarjem>',
                    username='alMotarjem',
                    password='tarjem31387875244*')
subreddit = reddit.subreddit("AlMotarjem")

for comment in subreddit.comments(limit=5):
    if(comment. id not in replied):
        commentBody = comment.body
        if('!tarjem' in commentBody):
            if( type(comment.parent()) is praw.models.reddit.submission.Submission):
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
                    file.write(str(comment.id)+"\n")
                else:
                    #print(finalReply+" \n \n +^(I am bot, I work using google translate)")
                    comment.reply(finalReply+" \n \n ^(I am bot, I work using google translate)")
                    file.write(str(comment.id)+"\n")

            else:
                body = comment.parent().body
                commentLanguage = translator.detect(body)
                finalReply = ""
                if(commentLanguage.lang =='ar'):
                    finalReply = translator.translate(body).text
                    finalReply =finalReply+" \n \n ^(I am a bot, I work using google translate)"
                    #print(finalReply)
                    comment.reply(finalReply)
                    file.write(str(comment.id)+"\n")

                else:
                    #print("I can only translate arabic text")
                    comment.reply("I can only translate arabic text")
                    file.write(str(comment.id)+"\n")



    