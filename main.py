import yagmail
import credentials
import pprint
import datetime

gmail_user = credentials.gmail_user
gmail_password = credentials.gmail_password

yag = yagmail.SMTP( {gmail_user: "Daily Thoughts"}, gmail_password)

receipient = credentials.receipient

def send_mail(contents):
    d_date = datetime.datetime.now()
    reg_format_date = str(d_date.strftime("%Y-%m-%d"))
    title = reg_format_date
    yag.send(receipient, title, contents=contents)

with open('./question_list.txt') as f:
    questions_1 = f.read().splitlines()

with open('./question_list_2.txt') as f:
    questions_2 = f.read().splitlines()

day_of_year = datetime.datetime.now().timetuple().tm_yday

contents_1 = questions_1[day_of_year]
contents_2 = questions_2[day_of_year]

contents = contents_1+"\n\n"+contents_2

send_mail(contents)


#https://www.marcandangel.com/2011/03/14/365-thought-provoking-questions-to-ask-yourself-this-year/
