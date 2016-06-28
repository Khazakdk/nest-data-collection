#!/bin/bash
python nest_poll.py >> nest.txt
./Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/nest.csv NestDataDump.csv
