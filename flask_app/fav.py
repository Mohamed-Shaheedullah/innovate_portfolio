fav_songs = [{"artist":"fontain dc", "song_name" : "televised mind", "genre":"indy", "release year":2019},
{"artist":"bombay bicycle club", "song_name" : "eat, sleep , wake", "genre":"indy", "release year":2018},
{"artist":"khruangbin", "song_name" : "Texas", "genre":"thai funk", "release year":2015},
{"artist":"muse", "song_name" : "starlight", "genre":"indy", "release year":2008}]

fave_bands =[]

for dict_i in fav_songs:
    # brackets, append 1, list 1, values 2, index no goes outside list
    # but inside append
    fave_bands.append(list(dict_i.values())[0])
#    print(list(dict_i.values())[0])

# print(fave_bands)

def add_to_list(band):
    fave_bands.append(band)

def del_from_list(band):
    fave_bands.remove(band)
    

