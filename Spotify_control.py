from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import subprocess

spotify_was_playing = False

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        global spotify_was_playing

        if self.path == "/pause":

            result = subprocess.check_output([
                "osascript",
                "-e",
                'tell application "Spotify" to player state as string'
            ]).decode().strip()

            spotify_was_playing = (result == "playing")

            if spotify_was_playing:
                os.system(
                    """osascript -e 'tell application "Spotify" to pause'"""
                )

        elif self.path == "/play":

            if spotify_was_playing:
                os.system(
                    """osascript -e 'tell application "Spotify" to play'"""
                )

        self.send_response(200)
        self.end_headers()

server = HTTPServer(("localhost", 8765), Handler)
print("Listening on port 8765...")
server.serve_forever()
