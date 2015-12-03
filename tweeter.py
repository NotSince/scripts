#!/usr/bin/python

from twython import Twython, TwythonError
import json
import time
import praw

OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
APP_KEY = ''
APP_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

COM_AMOUNT = 25

r = praw.Reddit(user_agent='Porygon-Bot')

subreddit = r.get_subreddit('pokemontrades')

def log_in():
    print '\nLogging in...'
    try:
        r.login('Porygon-Bot', '')
        print 'Logged in succesfully\n'
    except:
        print 'Invalid username or password\n'
        sys.exit() 	

def check_threads():
    topthreads = subreddit.get_hot()
    for submission in topthreads:
        
        if submission.link_flair_text == "Info" and not check_if_done(submission.id):
            try:
                twitter.update_status(status=submission.title + ' ' + submission.short_link)
            except:
                print "error"
            print submission.link_flair_text
            print submission.title
            add_to_done(submission.id)
        elif submission.link_flair_text == "Mod Post" and not check_if_done(submission.id):
            try:
                twitter.update_status(status=submission.title + ' ' + submission.short_link)
            except:
                print "error"
            print submission.link_flair_text
            print submission.title
            add_to_done(submission.id)
        elif submission.link_flair_text == "Daily" and not check_if_done(submission.id):
            try:
                twitter.update_status(status=submission.title + ' ' + submission.short_link)
            except:
                print "error"
            print submission.link_flair_text
            print submission.title
            add_to_done(submission.id)
        elif submission.link_flair_text == "Contest" and not check_if_done(submission.id):
            try:
                twitter.update_status(status= 'New Contest: ' + submission.title + ' ' + submission.short_link)
            except:
                print "error"
            print submission.link_flair_text
            print submission.title
            add_to_done(submission.id)
        elif submission.link_flair_text == "Giveaway" and not check_if_done(submission.id):
            try:
                twitter.update_status(status= 'New Giveaway: ' + submission.title + ' ' + submission.short_link)
            except:
                print "error"
            print submission.link_flair_text
            print submission.title
            add_to_done(submission.id)

def add_to_done(comment_id):
        with open('done.txt', 'a') as done: #NEEDS /PythonScripts/done.txt for Linux
                done.write(comment_id + '\n')
                

def check_if_done(comment_id):
        with open('done.txt', 'r') as done:
                id_list = done.readlines()
        raw_comment_id = comment_id + '\n'
        if raw_comment_id in id_list:
                return True
        else:
                return False

def cut_file():
        with open('done.txt', 'r') as done:
                file_lines = done.readlines()
        if file_lines > COM_AMOUNT:    
                with open('done.txt', 'w') as done:
                        done.writelines(file_lines[-COM_AMOUNT:])
		
def main():
    log_in()
    check_threads()
    cut_file()
	
if __name__ == "__main__":
    main()
