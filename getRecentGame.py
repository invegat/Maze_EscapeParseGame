#!/home/mark/.local/share/virtualenvs/python-9hqMudcv/bin/python3

import glob
import os
import re
import subprocess
from gi.repository import GLib
downloads_dir = GLib.get_user_special_dir(
    GLib.UserDirectory.DIRECTORY_DOWNLOAD)
# from parseGame import parseGame

list_of_files = glob.glob(downloads_dir + '/game-*.json')
latest_file = max(list_of_files, key=os.path.getctime)
# print(re.match(r".+?/game\-(\d{7})", latest_file).group(1))
tempDir = os.environ['TEMP_PARSE_GAME']
subprocess.check_call("./parseGame.py " + latest_file + " > " + tempDir + "parseGame-" +
                      re.match(r".+?/game\-(\d{7})", latest_file).group(1) + ".txt", shell=True)
subprocess.check_call("code -r " + tempDir + "parseGame-" +
                      re.match(r".+?/game\-(\d{7})", latest_file).group(1) + ".txt", shell=True)
