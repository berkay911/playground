grades_master_list = [
    ["alice", [90,92]],
    ["charlie",[78,95]]   
]

grades_dict = {}
grades_dict["alice"] = [[90,92],98]
grades_dict["charlie"] = [[70,72],78]

#print(grades_dict)


song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"

def map_song_dict(song):
    song_dict = {}
    song_list_splitted = song.split(" ")
    word_counts = []
    for word in song_list_splitted:
        word_count = song_list_splitted.count(word)
        word_counts.append((word, word_count))
    for word, count in word_counts:
        song_dict[word] = count


    return song_dict

print(map_song_dict(song))




