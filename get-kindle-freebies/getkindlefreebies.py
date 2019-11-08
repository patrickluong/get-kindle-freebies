import sys
import datetime
import os
import webbrowser
import praw

# input format:
# python main.py {required bool: auto-open browser} {optional int: posts limit}

def main():
    mapping = {
        'True' : 1,
        'true' : 1,
        't': 1,
        '1' : 1,
        'False' : 0,
        'false' : 0,
        'f' : 0,
        '0' : 0
    }

    should_open_browser = None
    posts_limit = 10
    reddit = praw.Reddit('kindle-freebies-collector')

    # sys.argv does not include 'python'
    should_open_browser = bool(mapping[sys.argv[1]])
    
    if len(sys.argv) > 2:
        posts_limit = int(sys.argv[2])

    browser_path = None
    browser = None

    if should_open_browser:
        # For Google Chrome on Windows: brower_path usually = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
        browser_path = "your browser here"
        browser = webbrowser.get(browser_path)

    for submission in reddit.subreddit('KindleFreebies').new(limit=posts_limit):
        print('\n' + '-' * 52 + ' POST ' + '-' * 52 + '\n')        
        print(submission.title + '\n')
        print(datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S') + ' UTC\n')
        print(submission.url + '\n')
        print('-' * 110)

        if browser != None:
            browser.open_new_tab(submission.url)

    print()


if __name__ == '__main__':
    main()