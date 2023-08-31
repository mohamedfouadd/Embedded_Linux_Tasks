#!/usr/bin/python3

import webbrowser

options=['google','facebook','instagram','youtube','spotify']
print(options)
x=input(str())

if x == 'google':
 webbrowser.get('firefox').open_new_tab('http://www.google.com')

elif x == 'facebook':

 webbrowser.get('firefox').open_new_tab('https://www.facebook.com/')

elif x == 'instagram':

 webbrowser.get('firefox').open_new_tab('https://www.instagram.com/')

elif x == 'spotify':

 webbrowser.get('firefox').open_new_tab('https://open.spotify.com/')

elif x == 'youtube':

 webbrowser.get('firefox').open_new_tab('https://www.youtube.com')

elif x != options :
 print('invalid input')
