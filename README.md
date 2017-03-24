## Traffic

A web forum where users can share:

1. traffic updates (jams,diversions,construction work etc.) for other users and 
2. alert law enforcement moderators to traffic violations (someone jumping a light at an intersection where police isn't deployed, a hit and run) along with details of the culprits vehicle if they can.

Details

- Landing Page (Home Page) - Basic HTML script.
- Forum - [phpBB3](https://www.phpbb.com/ "phpBB3") based (no registration/login required) - Only admin and moderator login.
- Reporting - Tweets to state traffic police using Twitter API.

How to use - 

Create local host using laragon/xampp then

1. Paste landing page files in C:\laragon\www
2. Paste phpbb3 folder in C:\laragon\www
3. Type 'localhost/Home.html'  in browser URL to open landing page
4. Type 'localhost/phpbb3' in browser URL to run Traffic forum
5. The "Forum" tab (in Home.html) has to be linked to the "index.php" file (in phpbb3).





