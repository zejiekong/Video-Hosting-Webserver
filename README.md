# Video-Hosting-Webserver
A flask webserver to host videos saved in dropbox using dropbox SDK. List of dependecies used can be found in requirements.txt.

Dropbox SDK : https://dropbox-sdk-python.readthedocs.io/en/latest/

Requirements:

Version : Python 3.8

Dropbox account (with Token)

1.) Clone repo to machine

``` git clone https://github.com/zejiekong/Video-Hosting-Webserver.git ```

2.) Hard code dropbox token in video.py

```
# Token Generated from dropbox
#TOKEN = ""
```
3.) Execute (for Unix)
- On command line, go to repo directory
- ``` source venv/bin/activate```
- ``` python3 __init__.py ```
