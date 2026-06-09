# 🎵 YouTube ↔ Spotify Auto Sync (macOS)

Automatically pause Spotify when a YouTube video starts playing and resume Spotify when the video is paused.

Unlike most media-control scripts, this project remembers Spotify's previous state:

* ✅ If Spotify was already playing, it will resume after you pause YouTube.
* ✅ If Spotify was not playing, it will stay stopped.
* ✅ Works with Brave, Chrome, Edge, and other Chromium-based browsers.
* ✅ Lightweight and easy to set up.

---

## 🚀 Demo

### Scenario 1: Spotify was already playing

```text
Spotify Playing
      ↓
Play YouTube Video
      ↓
Spotify Pauses
      ↓
Pause YouTube Video
      ↓
Spotify Resumes
```

### Scenario 2: Spotify was not playing

```text
Spotify Stopped
      ↓
Play YouTube Video
      ↓
No Action
      ↓
Pause YouTube Video
      ↓
Spotify Remains Stopped
```

---

## 🛠 Requirements

Before starting, make sure you have:

* macOS
* Spotify Desktop Application
* Python 3
* Brave / Chrome / Edge Browser
* Tampermonkey Extension

---

# 📦 Installation Guide

Follow the steps below carefully.

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/yt-spotify-sync.git
cd yt-spotify-sync
```

Or simply download the repository as a ZIP file.

---

## Step 2: Install Tampermonkey

Tampermonkey allows JavaScript to run on YouTube pages.

### Install Tampermonkey

Visit:

https://www.tampermonkey.net/

or install directly from your browser's extension store.

After installation:

1. Click the Tampermonkey icon.
2. Select **Dashboard**.
3. Click **Create a New Script**.

---

## Step 3: Add the Userscript

Delete everything inside the editor and paste:

```javascript
// ==UserScript==
// @name         YouTube Spotify Sync
// @namespace    https://github.com/YOUR_USERNAME
// @version      1.0
// @description  Pause Spotify when YouTube plays and resume when paused
// @match        https://www.youtube.com/*
// @grant        none
// ==/UserScript==

(function() {
    console.log("YOUTUBE SCRIPT LOADED");

    const interval = setInterval(() => {
        const video = document.querySelector("video");

        if (video) {
            console.log("VIDEO FOUND");

            video.addEventListener("play", () => {
                fetch("http://localhost:8765/pause");
            });

            video.addEventListener("pause", () => {
                fetch("http://localhost:8765/play");
            });

            clearInterval(interval);
        }
    }, 1000);
})();
```

Save the script using:

```text
Cmd + S
```

You should now see the script listed under Tampermonkey.

---

## Step 4: Enable Developer Mode (Important)

Some browsers may not inject userscripts correctly until Developer Mode is enabled.

Open:

```text
brave://extensions
```

or

```text
chrome://extensions
```

Enable:

```text
Developer Mode
```

located in the top-right corner.

---

## Step 5: Run the Python Backend

Open Terminal.

Navigate to the repository folder:

```bash
cd yt-spotify-sync
```

Run:

```bash
python3 spotify_control.py
```

Expected output:

```text
Listening on port 8765...
```

Leave this terminal window open.

---

## Step 6: Grant Spotify Automation Permission

The first time the script tries to control Spotify, macOS may display a permission popup.

Allow:

```text
Terminal → Control Spotify
```

or

```text
Python → Control Spotify
```

depending on your setup.

---

## Step 7: Test the Setup

1. Start Spotify and play a song.
2. Open YouTube.
3. Play a video.

Spotify should pause automatically.

Now pause the YouTube video.

Spotify should resume automatically.

---

# 🧪 Troubleshooting

## Spotify Does Not Pause

Test manually:

```bash
osascript -e 'tell application "Spotify" to pause'
```

If Spotify pauses, AppleScript is working correctly.

---

## Userscript Does Not Run

Check:

```text
Browser Extensions → Tampermonkey → Site Access → On All Sites
```

Ensure:

* Tampermonkey is enabled
* The userscript is enabled
* Developer Mode is enabled

---

## Python Server Not Running

Verify:

```bash
python3 spotify_control.py
```

and ensure:

```text
Listening on port 8765...
```

appears.

---

# 📂 Project Structure

```text
yt-spotify-sync/
│
├── spotify_control.py
├── README.md
└── LICENSE
```

---

# 🔮 Future Improvements

* [ ] Automatic startup on macOS login
* [ ] Safari support
* [ ] Apple Music support
* [ ] GUI configuration panel
* [ ] Native macOS application packaging

---

# 🤝 Contributing

Pull requests are welcome.

If you find a bug or have a feature request, please open an issue.

---

# 📬 Connect With Me

### Soumyajit Samanta

* GitHub: https://github.com/YOUR_GITHUB_USERNAME
* LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN_USERNAME
* Portfolio: https://YOUR_PORTFOLIO_URL

---

⭐ If this project helped you, consider starring the repository.

