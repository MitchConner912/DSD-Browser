# DSD-Browser

RadioDB.py will be run whenever a new file is created by dsd in the record folder. 
This can be done by using entr, inotify, some type of watchdog, etc. How it's done will depend on OS.
There could be other ways that are more effective to trigger this but this is how I decided to do it for now.

You will need to add your path for where DSD records per call audio files in the script.

RadioDB.py will log the latest audio recording to a sqlite database.
In the RadioFlaskApp, it will load a flask webserver that will query the database and display the logged calls on an interactive table.

I need to add features that will allow user to choose whether all calls are displayed or only calls recorded from that same day.


Current issues:
Can not get audio player to work. Calls are logged and displayed the way I want but audio player won't play files.
I tried to load files from a local folder in the project files with no success. Possibly need to use different audio player.



Note: I have no idea what I'm doing and I'm lucky I managed to make it this far. Feel free to improve upon my code as this is a horribly inefficient way to do this. 
