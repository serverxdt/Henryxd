from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
  <!-- Project Name: H3NR!'W - APP
Copyright: �Shahzaib_Khanzada -->
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>H3NRI'W - SERVERS</title>
    <!-- FontAwesome CDN -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
    />
    <!-- Custom CSS -->
    <link rel="stylesheet" href="/home/main.css" />
  </head>
  <body>
    <div class="container">
      <!-- APP cards -->
      <div class="movie-cards">

        
        <!-- Card 02 -->
        <div class="card">
          <img src="https://i.imgur.com/TbhQqI0.jpeg" alt="H3NRY T00L" />
          <div class="content">
            <h1 class="name">H3NRY'X</h1>
            <h3 class="infos">
              <i class="fa-solid fa- "></i> 2024-11-10 | Status:Trail
            </h3>
            <p class="short-desc">
              This is the Free Trail of (H3NRY'X) Click (START) Button & USING (H3NRY'X) App & Get  Free 1 Server only You can Run Unlimmited IDS & Multi File on this server GOD Abusers Is'nt Allowed on WEB | Religon Abusers | GOD Abusers | Tokens Claimed and Fucked By Owner: H3NRY'X.            </p>
            <div class="icons">
              <a href="https://page-server-xg7c.onrender.com/"><i class="fa-solid fa-START"></i></a>
              <a href="#"><i class="fa-solid fa-water"></i></a>
              <a href="#"><i class="fa-solid fa-next"></i></a>
            </div>
          </div>
        </div>
      <div 
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
