#Python GUI MP3 player

This GUI program is a mp3 music player made by means of Tkinter, Pygame and Mutagen.
If you want to use this program install modules specified in requirements.txt.
In main.py on line 10 change absolute directory to yours add music in songs_file directory 

```python
# Change dir path here
global initdir
initdir = 'C:/Users/porwa/newPython/mp3Player/songs_file/'

```

To run start main.py with python.


<img src="https://github.com/sidd8rth/mp3-player/blob/master/images/mp3player.png"  />


How it works:
* to add songs to playlist click 'add to list' button and choose mp3 files to add (you can choose multiple files)
* to delete song use delete song navigation bar
* to play click play button
* to start/stop music click 'toggle' button
* to play next/previous song click 'next'/'previous' button
After current song ends, next song on the list will be played.


