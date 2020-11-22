import webbrowser
import subprocess
import time

#subprocess.Popen('C:\\\Windows\\System32\\notepad.exe')
subprocess.Popen('C:\\\Program Files (x86)\\Microsoft Office\\root\\Office16\\onenote.exe')
subprocess.Popen('C:\\\Program Files (x86)\\Microsoft Office\\root\\Office16\\outlook.exe')
subprocess.Popen('C:\\\Windows\\system32\\mstsc.exe')
#subprocess.Popen('C:\\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
#subprocess.Popen('C:\\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')


edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
webbrowser.get(edge_path).open('http://www.google.com')
time.sleep(1)
webbrowser.get(edge_path).open_new_tab('http://www.youtube.com')

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('http://www.youtube.com')
time.sleep(1)
webbrowser.get(chrome_path).open_new_tab('http://www.yahoo.com')






