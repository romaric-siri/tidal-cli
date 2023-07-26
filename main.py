from pprint import pprint
import blessed
import vlc
import tidalapi
import sys
print(chr(27) + "[2J")
# print(dir(session))
# print()
# pprint(session._config)
# print()
#LOSSLESS 
# print(session._config.__dict__)
# tracks = session.get_album_tracks(album_id=52370055)
# for track in tracks:
#     print(track.id)




def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %r" % (attr, getattr(obj, attr)))

def print_table(table):
    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 3)
        for i in range(len(table[0]))
    ]
    row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])
    for row in table:
        print(row_format.format(*row))




term=blessed.Terminal()

def connect_to_api(username, password):
    session = tidalapi.Session()
    session.login(username, password)
    session._config.quality='LOSSLESS'

    return session

def login_ui(title, form, footer):
    print(chr(27) + "[2J")
    with term.location(y=term.height+1):
        print(footer)
    with term.location(y=0):
        print(title)
    with term.location(y=term.height // 2):
        print(term.center(form))
        a=input(term.move(int(term.height/2)+1, int(term.width/3)))
    return a

def player(track_id):
    session = tidalapi.Session()
    session.login('romaric.sirii@gmail.com', 'Romaricc10&*')
    session._config.quality='LOSSLESS'
    track = session.get_track_url(track_id=track_id)

    p = vlc.MediaPlayer(track)
    print(chr(27) + "[2J")
    
    print(f"{term.home}{term.black_on_skyblue}{term.clear}")
    print("press 'q' to quit.")
    with term.cbreak():
        val = ''
        p.play()
        while val.lower() != 'q':
            val = term.inkey(timeout=0.5)
            if not val:
               print(int(p.get_time()/1000))
            elif val.is_sequence:
               print("got sequence: {0}.".format((str(val), val.name, val.code)))
               p.pause()
            elif val:
               print("got {0}.".format(val))
        print(f'bye!{term.normal}')

menu = []

def search():

     print(chr(27) + "[2J")
     print(f"{term.home}{term.clear}")
     search = input("Search : ")
     o = session.search('track', search, 10)
     for i in range(len(o.tracks)):
         # print(o.tracks[i].name)
         menu.append([o.tracks[i].name, o.tracks[i].id])

def display_screen(selection):
    term = blessed.Terminal()
    print(term.clear())

    for (idx, m) in enumerate(menu):
        if idx == selection:
            print('{t.bold_white_reverse}{title}'.format(t=term, title=m[0]))
        else:
            print('{t.normal}{title}'.format(t=term, title=m[0]))


def run_selection(selection):
    print(term.green_reverse('Running {}'.format(menu[selection][0])))

username = login_ui('Titre', 'Username : ', 'Please')
password = login_ui('Titre', 'Password : ', 'Please')
session = connect_to_api('romaric.sirii@gmail.com', 'Romaricc10&*')

search()
# o = session.search('track', 'double fuck', 10)
with term.fullscreen():
    selection = 0
    display_screen(selection)
    
    
    print(chr(27) + "[2J")

    selection_inprogress = True
    with term.cbreak():
        while selection_inprogress:
            display_screen(selection)
            key = term.inkey()
            if key.is_sequence:
                if key.name == 'KEY_TAB':
                    selection += 1
                if key.name == 'KEY_DOWN':
                    selection += 1
                if key.name == 'KEY_UP':
                    selection -= 1
                if key.name == 'KEY_ENTER':
                    selection_inprogress = False
                    print(menu)
                    player(menu[selection][1])
            elif key:
                print("got {0}.".format(key))

            selection = selection % len(menu)

            display_screen(selection)

# dump(o.tracks[0])
# dump(o.tracks[1])
# dump(o.tracks[2])
# a = login('Please login', 'Email : ', 'footer')
# a = login('Please login', 'password', 'footer')
#print(a)
# player()











while True:
    pass


username = login_ui('Titre', 'Username : ', 'Please')
password = login_ui('Titre', 'Password : ', 'Please')
session = connect_to_api('romaric.sirii@gmail.com', 'Romaricc10&*')

search()

# o = session.search('track', 'double fuck', 10)

# dump(o.tracks[0])
# dump(o.tracks[1])
# dump(o.tracks[2])
# a = login('Please login', 'Email : ', 'footer')
# a = login('Please login', 'password', 'footer')
#print(a)
# player()











while True:
    pass



