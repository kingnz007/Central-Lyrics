# Central-Lyrics
A music lyrics website that works with the genius API.
Central Lyrics pulls the data from the <a href="https://genius.com/">genius</a> through its API.
It has features such as searching for a song, fetching lyrics, test cases, cache loading, etc.....<br />
But first, you need to get your CLIENT_ACCESS_TOKEN which is free. You can get it from 
<a href="https://genius.com/api-clients">here.</a><br />
Then, add the CLIENT_ACCESS_TOKEN to the ACCESS_TOKEN variable at <i>'central/views.py'</i>
```
10. # Enter your CLIENT ACCESS TOKEN
11. ACCESS_TOKEN = "YOUR CLIENT ACCESS TOKEN HERE"
```
Then, run the following command on terminal.
```
python manage.py runserver
```
Also make sure you've django and lyricsgenius installed in your environment.<br />
Central lyrics doesn't have its own database and completely depends on Genius API for its content. <br /><br />
Feel free to contribute to this project.
&hearts; &hearts; &hearts;
