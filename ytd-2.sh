#!/bin/bash

sudo youtube-dl  -ci --playlist-items $2 --extract-audio --audio-format mp3 --audio-quality 6 -o '%(title)s.%(ext)s' $1
