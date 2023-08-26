# SHARING VIRTUAL FACEBOOK - WITH TERMUX
<div align="center">
  <img src="Data/Sharing.png">
  <br>
  <br>
  <p>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/rozhakxd/Sharing">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/rozhakxd/Sharing">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/rozhakxd/Sharing">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/rozhakxd/Sharing">
    <img alt="Maintenance" src="https://img.shields.io/maintenance/no/2023">
  </p>
  <h4> Get Unlimited Share On Facebook Using Termux Only ! </h4>
</div>

##

### What is Sharing?
[**Sharing**](https://github.com/RozhakXD/Sharing) is a script to get lots of shares on a Facebook post in bulk or spam. This script uses page cookies to login and share posts.

### Termux command?
You can also see how to use this script on my [**Youtube**](https://youtu.be/JEoh5QkHJs0).

Download the [Termux](https://f-droid.org/repo/com.termux_118.apk) application then enter all commands in the Termux application.
```
$ apt update -y && apt upgrade -y
$ pkg install git python-pip
$ git clone https://github.com/RozhakXD/Sharing
$ cd "Sharing"
$ python -m pip install -r requirements.txt
$ python Run.py
```

```
$ cd "$HOME/Sharing" && git pul
$ python Run.py
```

### Requirements for logging in?

- If you use a Facebook page, make sure the page is the latest version.
- Accounts or Pages cannot be in free mode.
- You have to use a fake account or a new account to login.
- Facebook page uses "Indonesian Language".

### Why does it fail on login?

- The account cannot be in free mode or logged out.
- You must obtain page cookies through the desktop site or **"https://web.facebook.com"**.
- You entered the wrong facebook cookies.

### Post link requirements?

- Get the post link on Facebook Lite and you have to replace **"www.facebook.com"** to **"mbasic.facebook.com"**.
- Posts must have a share button (required).
- Facebook account is unlocked and posts are in public settings.

### Logout account problem?

- You must get facebook cookies at **web.facebook.com** using desktop mode.
- The account must be in an online state.
- Use 2-factor authentication and complete the account with a phone number.

### Facebook page blocked?

- Don't use the script too often, make sure to take a short break.
- You must use a delay of more than 60 seconds.
- Use cookies randomly by using a comma in each new cookies.

### Why failed to share?

- Logout page cookies or blocked account for 24 hours or more.
- Your post doesn't have a share button.
- You entered the wrong post link, you should check first.

### Message from the developers?
As a developer, I am not responsible if you use a real Facebook account or an original Facebook page. 

##
```python
print("Good luck hope it works!")
```
##
