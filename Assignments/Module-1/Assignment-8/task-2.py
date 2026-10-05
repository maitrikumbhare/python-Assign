def extract_artist(song_title):
    # Find the position of the dash
    dash_position = song_title.index("-")
    
    # Extract artist name using string slicing
    artist = song_title[dash_position + 1:].strip()
    
    return artist


# Example
song = "Tum Hi Ho - Arijit Singh"
print(extract_artist(song))