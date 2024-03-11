# Spotify-to-YouTube Music Migrator

This Python project facilitates the migration of your Spotify playlists to YouTube Music.

**Features**

*   Transfers user playlists.
*   Searches for matching tracks on YouTube Music
*   Creates new YouTube Music playlists.

**Prerequisites**

1.  Python 3
2.  Spotify Developer Account ([https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/))
3.  Google Cloud Project with YouTube Data API v3 enabled ([https://console.cloud.google.com/](https://console.cloud.google.com/))

**Setup**

1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Create a `credentials.py` file (see project structure).
4.  Obtain API keys from Spotify and Google and insert them into `credentials.py`.

**Usage**

   ```bash
   python main.py
Use code with caution.
The script will guide you through playlist selection and migration.
```
Disclaimer

Due to API limitations and variances in music catalogs, a perfect 1:1 migration might not always be possible.
 * For refrence purpose you can also view the project gallary to view how the process looks like.
Contributing

Feel free to improve the matching algorithm, suggest new features, and submit pull requests!


**Let me know if you'd like any elaborations or additional features added
