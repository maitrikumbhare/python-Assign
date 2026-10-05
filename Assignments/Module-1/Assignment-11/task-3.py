def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers} followers")


friends = {
    "kashish": "2.3K",
    "yushra": "5.1K",
    "vidhya": "1.8K",
    "Aksha": "2.2k",
}

display_friends(friends)