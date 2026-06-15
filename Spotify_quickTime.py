import subprocess
import time
import os

spotify_was_playing = False
previous_quicktime_state = False


def quicktime_playing():
    try:
        result = subprocess.check_output([
            "osascript",
            "-e",
            'tell application "QuickTime Player" to playing of front document'
        ]).decode().strip().lower()

        return result == "true"

    except:
        return False


def spotify_playing():
    try:
        result = subprocess.check_output([
            "osascript",
            "-e",
            'tell application "Spotify" to player state as string'
        ]).decode().strip().lower()

        return result == "playing"

    except:
        return False


print("Monitoring QuickTime...")

while True:

    current_quicktime_state = quicktime_playing()

    # QuickTime started playing
    if current_quicktime_state and not previous_quicktime_state:

        spotify_was_playing = spotify_playing()

        if spotify_was_playing:
            os.system(
                """osascript -e 'tell application "Spotify" to pause'"""
            )

            print("QuickTime started → Spotify paused")

    # QuickTime stopped/paused
    elif not current_quicktime_state and previous_quicktime_state:

        if spotify_was_playing:
            os.system(
                """osascript -e 'tell application "Spotify" to play'"""
            )

            print("QuickTime paused → Spotify resumed")

    previous_quicktime_state = current_quicktime_state

    time.sleep(0.5)
