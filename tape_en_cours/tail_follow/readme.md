# Concept

Pure python implementation of a tail -f 
It uses coroutine to read an infinite message stream

# How to use 

1. launch `fake_server_log.py` to create a continuous message stream in the file `log.txt`
    * this needs an example apache log file to work (takes the one in the medias)
1. launch `tail_follow.py` to see the tail -f equivalent in pure python 