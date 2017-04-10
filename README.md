# youtube-audio
Run audio from youtube videos in terminal

---------

## Dependencies
`python` version 3 is required.
You need youtube-dl and vlc media player for the script to work. 

```bash
sudo apt-get install vlc
```

```bash
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install youtube-dl
```

------------

## Usage
Just run the script `youtube-audio` along with the url for youtube video as argument.  
Example:

```bash
python youtube-audio.py https://www.youtube.com/watch?v=-qfCrYwdqCA
```

Or simply you can make the script executable using `chmod u+x youtube-audio.py`. Then you will be able to run it as:
```bash
youtube-audio.py https://www.youtube.com/watch?v=-qfCrYwdqCA
```
-----------

## TO-DO
- Checking for valid youtube url
- Parsing the youtube url from a playlist
- Way to add urls to create playlist
- Play from a youtube playlist
