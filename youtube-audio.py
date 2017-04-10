#!/usr/bin/env python3

import subprocess
import sys
import os

class YoutubeError(Exception):
    def __init__(self, args):
        self.args = args

    def display(self):
        print(''.join(self.args))

def exe(command):
    command = command.strip()
    c = command.split()
    output, error = subprocess.Popen(c,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE).communicate()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    return (output, error)

def get_youtube_streams(url):
    print("Getting stream urls...")
    cli = "youtube-dl -g {}".format(url)
    output, error = exe(cli)
    stream_urls = output.split("\n")
    url = {}
    url['audio'] = stream_urls[1]
    url['video'] = stream_urls[0]
    print("Fetched stream urls...")
    return url

def run_cvlc(stream_url):
    cli = "cvlc '{}'".format(stream_url)
    os.system(cli)

def main():
    args = sys.argv[1::]
    if args:
        url = args[0]
        stream = get_youtube_streams(url)
        run_cvlc(stream['audio'])


if __name__ == "__main__":
    main()

