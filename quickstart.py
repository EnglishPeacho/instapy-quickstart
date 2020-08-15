import random

from instapy import InstaPy
from instapy import smart_run


insta_username = ''
insta_password = ''




session = InstaPy(username=insta_username,
                  password=insta_password,
                  bypass_security_challenge_using='Email',
                  headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)


with smart_run(session):


    
    session.unfollow_users(amount=30, nonFollowers=True, style="RANDOM", unfollow_after=8*60*60)    
    session.like_by_feed(amount=20, randomize=True, unfollow=False, interact=False)
    yes=['egirlaesthetic','grungevibes','aestheticblog','vintageoutfit','tumblrgirl','grungeoutfit',
         '90svintage','aestheticfeed','aestheticoutfit','indieaesthetic','grungefeed','vintageaesthetic','lightaesthetic']
   #'gothgirl','gothoutfit','egirloutfit','gothgirl',

    no=['gym','beast','workout','exercise ','bar',
        'cross','cardio','weights','abs','squats','shredded',
        'fitcouple','couple','gains','food','healthy',
        'motivation','likefor','like','gym']
    
    session.set_dont_like(no)
    session.set_do_follow(enabled=True, percentage=89)
    
    session.set_do_comment(enabled=True, percentage=50)
    
    comments=[u':two_hearts: :two_hearts: :sparkles: cute fit ',
              u':fire: adoring this :two_hearts: ',
              u':yellow_heart: adoring this :two_hearts: :sparkles: ',
              u':innocent: :heart: love this post :heart: ',
              u':heartpulse: :two_hearts: sweet fit :innocent: ',
              u':heart_eyes: :heart_eyes: love your posts ',
              u':revolving_hearts: gorgeous aesthetic :revolving_hearts: :dizzy: ',
              u':sparkling_heart: adoring the aesthetic :revolving_hearts: ',
              u':heart: :heart:  cute aesthetic :fire: ',
              u':innocent: adoring the look :revolving_hearts: :revolving_hearts: ',
              u' :two_hearts: :heart: stunning aesthetic :sparkles:',
              u'  :sparkles: this fit :sparkles: :fire:',
              u' adoring the fit :revolving_hearts:',
              u':fire:  :sparkles: :sparkles: love thisss fit',
              u'kwute fitt  :revolving_hearts: :dizzy:',
              u':sparkles: :yellow_heart: adoring the aesthetic tbh ',
              u':heart: :two_hearts: on the fit ',
              u'really loving your recent :revolving_hearts: :fire: :fire: ',
              u'sweet fit and drip posts :heart eyes: :heart:',
              u'adoring the aesthetic drip :sparkles: :heart: ',
              u' cute and aesthetic :two_hearts: :heartpulse:',
              u'beaut aesthetic :fire: :fire: to the point',
              u' :two_hearts: :two_hearts: beaut sweet fit man',
              u'nice aesthetic and feed  xx',
              u'loving the drip and aesthetic recents  xx',
              u'damn, adoring the drip xx',
              u'this is quite the aesthetic :heart_eyes: :dizzy:',
              u'what a sweet fit :heart: :sparkles:',
              u' this is :heart: :heart:'
              ]
              
    session.set_comments(comments,media='Photo')
    
    session.set_do_like(True, percentage=97)
    session.set_delimit_liking(enabled=True, max_likes=None, min_likes=1)
    session.set_delimit_commenting(enabled=True, max_comments=None, min_comments=None)
    
                  
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", 
                                                          "unfollows","server_calls_d"], sleepyhead=True, 
                               stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=100,
                              peak_likes_daily=700,
                              peak_comments_hourly=40,
                              peak_comments_daily=200,
                              peak_follows_hourly=70,
                              peak_follows_daily=None,
                              peak_unfollows_hourly=30,
                              peak_unfollows_daily=500,
                              peak_server_calls_hourly=None,
                              peak_server_calls_daily=500000)
    session.set_action_delays(enabled=True,
                              like=18,
                              comment=21,
                              follow=35,
                              unfollow=16,
                              story=19,randomize=True,random_range_from=71,
                              random_range_to=111)
    
    session.set_user_interact(amount=2, randomize=True, percentage=95,
                              media='Photo')
    
    session.like_by_tags(random.sample(yes, 13), amount=random.randint(30, 80), interact=True)
    
    session.set_do_story(enabled = True, percentage = 56, simulate = True)
    session.story_by_tags(yes)
    

