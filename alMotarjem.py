import praw
import pdb
import re
import os
from firebase import firebase
from googletrans import Translator


firebase = firebase.FirebaseApplication('https://almotarjem-eca52.firebaseio.com/', None)

result = firebase.get('/almotarjem-eca52/', '')

replied = []
for comment in result:
    replied.append(result[comment])


translator = Translator()
reddit = praw.Reddit(client_id='2Qv7SGX2aP_3_A',
                    client_secret='pYjb2DsMz1l1XTt5n_T2zfNbg4c',
                    user_agent='<leb motarjem>',
                    username='alMotarjem',
                    password='tarjem31387875244*')

subredditsArray = ['AlMotarjem', 'lebanese', 'lebanon', 'Arabs']

for sub in subredditsArray:
    subreddit = reddit.subreddit(sub)
    for comment in subreddit.comments(limit=20):
        commentBody = comment.body
        if(('!tarjem' in commentBody or '! tarjem' in commentBody) and comment.id not in replied):
            print(commentBody)
            if( type(comment.parent()) is praw.models.reddit.submission.Submission):
               submissionTitle = comment.parent().title
               submissionText = comment.parent().selftext
               titleLanguage = translator.detect(submissionTitle)
               postLanguage = translator.detect(submissionText)
               if postLanguage.lang =='ar' or titleLanguage.lang =='ar':
                   titleTranslation = translator.translate(submissionTitle).text
                   postTranslation = translator.translate(submissionText).text
                   titleReply = "Title: "+titleTranslation+"\n \n"
                   bodyReply = "Body: "+postTranslation+"\n \n"
                   finalReply = titleReply+" "+bodyReply+" \n \n ^(I am a bot, I work using google translate \n \n have any questions? visit r/alMotarjem)"
                   comment.reply(finalReply)                  
               else: 
                   print("I only translate from arabic to english ^(I am a bot, I work using google translate  \n \n have any questions? visit r/alMotarjem)")
            else:
                commentBody = comment.body
                text = comment.parent().body
                language = translator.detect(text)
                if language.lang =='ar':
                    translatedText = translator.translate(text).text
                    comment.reply(translatedText+" \n \n ^(I am a bot, I work using google translate. Have any questions? visit r/alMotarjem)")
                else:
                    comment.reply("I only translate from arabic to english \n \n ^(I am a bot, I work using google translate \n \n have any questions? visit r/alMotarjem)")
            firebase.post('/almotarjem-eca52/', comment.id)           
        