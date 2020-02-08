#!/home/mark/.local/share/virtualenvs/python-9hqMudcv/bin/python3

import glob
import os
import re
import subprocess

# from parseGame import parseGame

list_of_files = glob.glob('/home/mark/Downloads/game-*.json')
latest_file = max(list_of_files, key=os.path.getctime)
#print(re.match(r".+?/game\-(\d{7})", latest_file).group(1))
subprocess.check_call("./parseGame.py " + latest_file + " > /media/mark/hard/Maze_Escape/parseGame-" +
                      re.match(r".+?/game\-(\d{7})", latest_file).group(1) + ".txt", shell=True)
subprocess.check_call("code -r " + "/media/mark/hard/Maze_Escape/parseGame-" +
                      re.match(r".+?/game\-(\d{7})", latest_file).group(1) + ".txt", shell=True)
