
import subprocess
import time

CHROME_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


def load_windows(windows):
    for window in windows:
        subprocess.Popen([CHROME_PATH, window[0], '--new-window'])
        time.sleep(1)
        for i in range(1, len(window)):
            subprocess.Popen([CHROME_PATH, window[i]])


def main():
    window_1 = ['https://www.youtube.com/', 'https://web.whatsapp.com/',
                'https://outlook.live.com/mail/0/', 'https://trakt.tv/dashboard',
                'https://www.reddit.com/']
    window_2 = ['https://teams.microsoft.com/_#/calendarv2', 'https://rwsportal.cloud.com',
                'https://stackoverflow.com/']
    windows = [window_1, window_2]
    load_windows(windows)


if __name__ == '__main__':
    main()
