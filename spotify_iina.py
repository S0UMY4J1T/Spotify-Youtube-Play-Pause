import socket
import json
import subprocess
import time
import os

IINA_SOCKET = "/tmp/iina-socket"

spotify_was_playing = False
previous_iina_playing = False


def get_iina_playing():
    """Return True if IINA is currently playing."""

    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(IINA_SOCKET)

        command = {
            "command": ["get_property", "pause"]
        }

        s.sendall((json.dumps(command) + "\n").encode())

        response = s.recv(4096).decode()
        s.close()

        data = json.loads(response)

        # mpv pause property:
        # false = playing
        # true  = paused

        return not data.get("data", True)

    except Exception:
        return False


def get_spotify_playing():
    """Return True if Spotify is currently playing."""

    try:
        result = subprocess.check_output([
            "osascript",
            "-e",
            'tell application "Spotify" to player state as string'
        ]).decode().strip().lower()

        return result == "playing"

    except Exception:
        return False


def spotify_pause():
    subprocess.run([
        "osascript",
        "-e",
        'tell application "Spotify" to pause'
    ])


def spotify_play():
    subprocess.run([
        "osascript",
        "-e",
        'tell application "Spotify" to play'
    ])


print("🎬 IINA ↔ Spotify Sync")
print("Monitoring IINA...")
print("Press Ctrl+C to stop.\n")


while True:

    current_iina_playing = get_iina_playing()

    # IINA started playing
    if current_iina_playing and not previous_iina_playing:

        spotify_was_playing = get_spotify_playing()

        if spotify_was_playing:
            spotify_pause()
            print("▶️ IINA PLAYING → Spotify PAUSED")

        else:
            print("▶️ IINA PLAYING → Spotify was already stopped")

    # IINA paused/stopped
    elif not current_iina_playing and previous_iina_playing:

        if spotify_was_playing:
            spotify_play()
            print("⏸️ IINA PAUSED → Spotify RESUMED")

            spotify_was_playing = False

    previous_iina_playing = current_iina_playing

    time.sleep(0.5)
