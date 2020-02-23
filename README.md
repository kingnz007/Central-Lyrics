# Central-Lyrics
Get lyrics of any song on Central Lyrics.<br />
Central Lyrics gets the data from <a href="https://genius.com/">genius</a> through its API. <br />
It has songs, lyrics, test cases, cache loading, etc features.<br /> <br />
But first, you need to get your CLIENT_ACCESS_TOKEN from <a href="https://genius.com/api-clients">here.</a><br />
Then, add the CLIENT_ACCESS_TOKEN to the ACCESS_TOKEN variable at <i>'central/views.py'</i>.
```
10. # Enter your CLIENT ACCESS TOKEN
11. ACCESS_TOKEN = "YOUR CLIENT ACCESS TOKEN HERE"
```
Make sure you've memcache and lyricsgenius installed in your environment.
```
pip install python-memcached
pip install lyricsgenius
```
It completely depends on Genius API for its content. <br /><br />
Feel free to contribute to the project.
&hearts; &hearts; &hearts;
