# Spotify to YouTube Music Playlist Migrator

This Python project simplifies the process of migrating your Spotify playlists to YouTube Music, ensuring a smooth transition of your music preferences.

## Key Features

* **Playlist Transfer:** Seamlessly migrate your Spotify playlists to YouTube Music.
* **Intelligent Match:** Accurately finds corresponding songs on YouTube Music.
* **Playlist Generation:** Automatically creates new YouTube Music playlists based on your Spotify data.

## Prerequisites

* **Python 3:** Download and install the latest Python version from [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **Developer Accounts:**
    * **Spotify:** Create an account at [https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/).
    * **Google Cloud Project:** Set up a project and enable the YouTube Data API v3 at [https://console.cloud.google.com/](https://console.cloud.google.com/).

## Setup Instructions

1. **Clone the Repository:** Use Git to clone the project to your local machine.
2. **Install Dependencies:** Run `pip install -r requirements.txt` in your terminal to install required packages.
3. **Create `credentials.py`:**  Create a file named `credentials.py` (See the project structure for an example).
4. **Obtain API Keys:**  Follow the instructions on the Spotify and Google developer portals to get your API keys. Add these keys to your `credentials.py` file.

## Disclaimer

Please note that due to limitations in APIs and differences between music platforms, we cannot guarantee a 100% perfect migration in all cases.  


## Contributing

We welcome your contributions! If you have ideas for improvements or bug fixes, please feel free to submit pull requests. 

## Additional Enhancements (Future Work)

* **Progress Indicator:** Provide visual feedback during the migration process.
* **Error Handling:** Implement more informative error messages for easier troubleshooting.
* **Command-Line Interface (CLI):** Develop a user-friendly CLI for a wider audience.




# Project Gallary
**Playlist I want to migrate**

![1](https://github.com/PrajwalChittora/Spotify-to-YouTube-Music-Migrator/assets/109464358/960378d0-a45c-4ac7-9126-1fbab070b7aa)

**Reading user playlist via Spotify API**

![2](https://github.com/PrajwalChittora/Spotify-to-YouTube-Music-Migrator/assets/109464358/606263f2-ca5d-42b3-900a-723f753232f5)

**Completing Youtube Oauth 2.0 verification**

2![3](https://github.com/PrajwalChittora/Spotify-to-YouTube-Music-Migrator/assets/109464358/824d3fcf-119b-44c8-b831-5c3463be8f07)

**Target playlist is migrated**

![4](https://github.com/PrajwalChittora/Spotify-to-YouTube-Music-Migrator/assets/109464358/5c7525d1-7889-4015-ba10-be3c75c43227)


