# Favorite Book Function

def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(f"One of my favorite books is {title}.")

# City Function

def describe_city(city, country="Nigeria"):
    """Describe a city and its country."""
    print(f"{city} is in {country}.")

# Make Album Function

def make_album(artist, title, tracks=None):
    """Return a dictionary describing a music album."""
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album
