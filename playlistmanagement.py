import random
playlist = ["rock"]
manage = ""
while manage != "0":
   print("\nPlaylist managenment")
   print("1 Do you want to view playlist") 
   print("2 Do you want to add a song to playlist")
   print("3 remove a song from playlist")
   print("4  Do you want to shuffled playlist playlist")
   print("5 Do you want to sort playlist")
   print("6 Do you want to save playlist: ")
   print("7 Do you want to upload a playlist: ")
   manage = input("Please enter which would you like to do?: ")
   if manage == "1":
     print("Playlist: ", playlist)
   elif manage == "2":
      new_adds = []
      while True:
         add = input("Enter a new song (or type 'done' to stop:) ")
         if add.lower() == "done":
            break
         new_adds.append(add)
         playlist.append(add)
      print("New songs addded: ", new_adds )
      print("Playlist with added song: ", playlist)
   elif manage == "3":
     remove = input("Enter the song you want to remove: ")
     playlist.remove(remove)
     print("Song removed is: ", remove)
    
   elif manage =="4":
    random.shuffle(playlist)
    print("Shuffled Playlist:", playlist)
   elif manage =="5":
    playlist.sort()
    print("Sorted playlist: ", playlist)
   elif manage =="6":
    save_file = input("Enter your save file name: ")
    with open(f"{save_file}.txt", "w") as L:
     for sound in playlist:
      L.write(f"{sound}\n")
      print("Playlist is saved to file ", save_file + ".txt")
   elif manage == "7":
     load = input(" Enter playlist from your file: ")
     play = open(load)
     for line in play:
      print(line)
