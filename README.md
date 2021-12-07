# Py_Insta-Bot
MAKE NEW INSTA ACCOUNT IF YOU'RE TRYING THIS.

So in this project we basically log in into our instagram account and than searched the account with 10K followers and than send follow request to those followers,
if already request is sent than we skip them

So it's very straighforward, we mentioned some constants in terms of env variables then, we've initialized our selenium web driver, than we call a login method,
in which we grab username, password fields put our username and password in it and press ENTER to log in.
after that it will ask us to remember our pass so we've pressed not_now button.

than we call find_followers method here we open target instagram account, and than head up to followers of that account, than in follower pop up it scrolled to make all the 
followers visible. (i've run this loop 10 times, you can change as much as you want.

than we call follow method, in this we grab all follow buttons and than one by one click on each of them, send request to new on skip the previous one,
after all it's done we quit the window.
