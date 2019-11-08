import sys
import webbrowser
import pyperclip

def main():
    url = 'https://www.google.com/maps/place/'

    # For Google Chrome on Windows: brower_path usually = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
    browser_path = 'your browser here'

    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    browser = webbrowser.get(browser_path)
    browser.open(url + address)


if __name__ == '__main__':
    main()