import random

def suggest_song(mood, genre):

    song_database = {
        "happy": {
            "pop": ["shape of us", "ashiq tera", "if your happy"],
            "rock": ["humraah", "panida", "malang"]
        },
        "sad": {
            "pop": ["khani suno", "Sanam re", "chalaya"],
            "rock": ["ranjhio", "shayad", "tere vaste"]
        },
    }

    if mood in song_database and genre in song_database[mood]:
        suggested_song = random.choice(song_database[mood][genre])
        return suggested_song
    else:
        return "No matching songs found for your preferences."

user_mood = input("Enter your mood (happy, sad, etc.): ")
user_genre = input("Enter your preferred genre (pop, rock, etc.): ")

suggested_song = suggest_song(user_mood, user_genre)
print(f"Suggested Song: {suggested_song}")
