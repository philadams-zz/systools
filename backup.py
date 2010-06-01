#!/usr/bin/env python

"""
convenience script to backup various folders to an external hd via rsync
"""

import subprocess

EXTERNAL_PATH = '/Volumes/Calvin/Backup/current/'
TO_SYNC = ['/Users/phil/Code', # no trailing slash
           '/Users/phil/Documents',
           '/Users/phil/Movies',
           '/Users/phil/Music',
           '/Users/phil/Pictures',
           '/Users/phil/Sites',
           '/Users/phil/todo.txt']
CMD = ['rsync', '-a', '-v', '--delete-after', '--exclude=.DS_Store']

print('syncing folders:')
for local_dir in TO_SYNC:
    print('\n%s...' % local_dir)
    retcode = subprocess.call(CMD + [local_dir, EXTERNAL_PATH])
print('sync complete')
