import string
from PyGlow import PyGlow
from time import sleep
import urllib2
import json

pyglow=PyGlow()
f = urllib2.urlopen('http://api.thingspeak.com/channels/1417/field/1/last.json')
json_string = f.read()
parsed_json = json.loads(json_string)

cheer = parsed_json["field1"]
print "Current color is %s" % (cheer)
f.close()
pyglow.all(0)

if cheer == "red":
    pyglow.color("red", 255)
elif cheer == "green":
    pyglow.color("green", 255)
elif cheer == "blue":
    pyglow.color("blue", 255)
elif cheer == "cyan":
    pyglow.color("blue", 255)
    pyglow.color("green", 255)
elif cheer == "white":
    pyglow.color("white", 255)
elif cheer == "warmwhite" or cheer == "oldlace":
    pyglow.color("red", 253)
    pyglow.color("white", 255)
elif cheer == "purple":
    pyglow.color("red", 255)
    pyglow.color("blue", 255)
elif cheer == "magenta":
    pyglow.color("red", 255)
    pyglow.color("white", 150)
elif cheer == "yellow":
    pyglow.color("yellow", 255)
elif cheer == "orange":
    pyglow.color("orange", 255)
elif cheer == "pink":
    pyglow.color("red", 255)
    pyglow.color("white", 190)
        
