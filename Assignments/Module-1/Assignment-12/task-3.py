# List of song durations in minutes
song_durations = [3, 4, 5, 2, 6]

# Convert minutes to seconds using lambda and map()
durations_in_seconds = list(map(lambda x: x * 60, song_durations))

print(durations_in_seconds)