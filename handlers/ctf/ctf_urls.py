#-*- coding:utf-8 -*-
#!usr/bin/python3


from ctf_handler import EnterHandler,ScoreBoardHandler,MyTeamHandler,NoticeHandler,ManageHandler,ChallengeHandler,TitleListHandler,DeleteHandler

ctf_url = [
    (r'/ctf/index',EnterHandler),
    (r'/ctf/scoreboard',ScoreBoardHandler),
    (r'/ctf/myteam',MyTeamHandler),
    (r'/ctf/notice',NoticeHandler),
    (r'/ctf/manage',ManageHandler),
    (r'/ctf/challenge',ChallengeHandler),
    (r'/ctf/list',TitleListHandler),
    (r'/ctf/delete',DeleteHandler),

]