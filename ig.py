from blessings import Terminal
import vlc
import tidalapi
import sys



# with term.location(0, term.height - 1):
#     print('Here is the bottom.')
# print('This is back where I came from.')

session = tidalapi.Session()
session.login("XXXXcom", "XXXX")
session._config.quality='LOSSLESS'



term = Terminal()
a=""
choices=[]
print(term.clear())
while True:
    with term.location(y=term.height):

        search = input(">" )
        
        if search.startswith(":s"):
            print("Selected!")
            track = session.get_track_url(track_id=o.tracks[int(search.split()[1])].id)
            p = vlc.MediaPlayer(track)
            p.play()
        elif search.startswith(":p"):
            p.pause()
        else:
            o = session.search('track', search, 9)


        print(term.clear())

    with term.location(y=1):
        for i in range(len(o.tracks)):
          # print(o.tracks[i].name)
           choices.append([o.tracks[i].name, o.tracks[i].id])
           print(str(i) + ". " + "["+o.tracks[i].artist.name + "] "+o.tracks[i].name)

        #print("oui")

while True:
    pass
