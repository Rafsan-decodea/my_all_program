from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
import subprocess

print '-'*100
print '[+]Youtube Downloader'
print '    [+]Code By Md Rafsan jani shazid'
print '        [+]Email: shazidno123@gmail.com'
print '-'*100


def download_from_youtube():
  try:
   link = raw_input('input Link====>')
   byte_stream = {}
   with youtube_dl.YoutubeDL(byte_stream) as ydl:
        ydl.download([link])
   print '-'*100
   print '[+]Download in the Same derectiory'
  except:
    print '[!]Some Thing Wrong When Dowloding'
  subprocess.call(['pause'],shell=True)




if __name__ == '__main__':
    download_from_youtube()


