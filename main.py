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
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HENRY WEB</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
   <link rel="stylesheet" href="style.css" type="text/css" media="all" />
    <style>
        *{

    box-sizing: border-box;

    margin: 0;
    padding: 0;
}
body {
            margin: 0;
            padding: 0;
            font-family: Popins, sans-serif;
            background-color: black;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            padding: 0;
}
        .container {
            max-width: 50px auto; /* Decreased max-width */
            margin: 50px auto; /* Adjusted margin */
            padding: 20px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
}
h3{
    font-size: 12px;
    color: white;
    text-align: center;
}
h2{
    text-align: center;
    font-size: 19px;
    font-family: cursive;
    color: white;
}
.nav-bar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    list-style: none;
    position: relative;
    background-color: var(--color2);
    padding: 12px 20px;
}
.logo img {width: 40px;}
.menu {display: flex;}
.menu li {padding-left: 30px;}
.menu li a {
    display: inline-block;
    text-decoration: none;
    color: var(--color1);
    text-align: center;
    transition: 0.15s ease-in-out;
    position: relative;
    text-transform: uppercase;
}
.menu li a::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 1px;
    background-color: var(--color1);
    transition: 0.15s ease-in-out;
}
.menu li a:hover:after {width: 100%;}
.open-menu , .close-menu {
    position: absolute;
    color: var(--color1);
    cursor: pointer;
    font-size: 1.5rem;
    display: none;
}
.open-menu {
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
}
.close-menu {
    top: 20px;
    right: 20px;
}
#check {display: none;}
@media(max-width: 610px){
    .menu {
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 80%;
        height: 100vh;
        position: fixed;
        top: 0;
        right: -100%;
        z-index: 100;
        background-color: var(--color2);
        transition: all 0.2s ease-in-out;
    }
    .menu li {margin-top: 40px;}
    .menu li a {padding: 10px;}
    .open-menu , .close-menu {display: block;}
    #DOWNLOAD: DOWNLOADED ~ .menu {center: 0;}
}

.convo{
    box-shadow: rgba(0, 0, 0, 1.35) 0px 15px 20px;
    width: 250px;
    height: 120px;
    background-color: yellow;
    margin-left: 55px;
}
h1{
    margin-top: 10px;
    color: white;
    font-size: 12px;
    text-align: center;
}

details{
    color: red;
}
.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: white 50 10px 20px -10px;
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 30px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 250px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 50px rgba(5, 0, 0, 1.35);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.imager-containe{

  position: relative;


  width: 300px; /* adjust the width to your image size */
  height: 250px; /* adjust the height to your image size */
  margin: 2px;
  box-shadow: 0 0 50px rgba(5, 0, 0, 1.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 30px;
}

.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 50px rgba(5, 0, 0, 1.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 50px rgba(5, 0, 0, 1.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 50px rgba(5, 0, 0, 1.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 50px rgba(5, 0, 0, 1.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 30px rgba(0, 0, 0, 1.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 30px;
}

.video-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}

.button-34 {
  background: whit;
  border-radius: 999px;
  box-shadow: white 5 10px 10px -10px;
  box-sizing: border-box;
  color: red;
  cursor: pointer;
  font-family: Inter,Helvetica,"Apple Color Emoji","Segoe UI Emoji",NotoColorEmoji,"Noto Color Emoji","Segoe UI Symbol","Android Emoji",EmojiSymbols,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans",sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
  opacity: 1;
  outline: 5 solid white;
  padding: 8px 18px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: zooming;
  width: fit-content;
  word-break: break-word;
  border: 5;
  margin-bottom: 20px;
}

.footer {
    text-align: center;
    margin-top: 10px;
    color: white;
}
h4{
    color: white;
    font-family: bold;
    text-align: center;
}
    </style>
    </head>
    
<body>
    <header>
    <nav>
        <ul class='nav-bar'>
            <div class="text-2xl text-primary">: ̗̀➛ 𝐇𝐄𝐍𝐑𝐘 𝐗 𝐒𝐀𝐌𝐀𝐑 ★</div>
            <input type='checkbox' id='check' />
            <span class="menu">
                <li><a href="">WEB TO WEB SINGLE</a ></li>
                                <li><a href="">WEB TO WEB STICKER</a></li>
                <li><a href="">MULTY COOKIE PAGE+SIMPLE ID POST</a></li>
                
                    <li><a href="">MULTY TOKEN CONVO</a></li>
                                        <li><a href="">AUTO POST SHARE + MULTY POST</a></li>
                <li><a href="">POST BOOKMARK TOOL </a></li>
                </li>
                <label for="check""><i class="fas fa-times"></i></label>
            </span>
            <label for="check" class="open-menu"><i class="fas fa-bars"></i></label>
        </ul>
    </nav>
    </header>
    <br />
    <h2>𝗚𝗘𝗧 𝗙𝗥𝗘𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 ➤ 𝙃𝙚𝙣𝙧𝙮 𝙓 𝙎𝙖𝙢𝙖𝙧</h2>
    <br />
    
        <div class="content">
        <body>
        <img src="https://i.imgur.com/x34jjuk.jpeg" style="width: 100%; height: auto; border-radius: 18px;">
</body>
        <h1>Officail WEB</h1>
 <h1>╰┈➤ 🩷 𝗙𝗿𝗲𝗲 𝗦𝗲𝗿𝘃𝗲𝗿 𝗔𝗽𝗽 𝗕𝘆 𝗛𝗲𝗻𝗿𝘆 𝗫 𝗦𝗮𝗺𝗮𝗿 ᯓ★</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://www.mediafire.com/file/dotpunuezc9ji5p/HENRY_X_SAMAR_APK_.apk/file'">⊲ DOWNLOAD ⊳</button>
    <br />
    <br />

    <div class="footer">
    <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
      <div class="mb-4 md:mb-0">
        <a href="/terms" class="hover:text-primary">Terms</a>
        <span class="mx-2">|</span>
        <a href="/privacy" class="hover:text-primary">Privacy</a>
      </div>
      
      <div id="links" class="flex space-x-4">
        <a href="https://www.facebook.com/Henry.inxide" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
        <a href="https://wa.me/+919235741670" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
        <a href="https://github.com/Henryinxid3/" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
      </div>
      
      <div class="mt-4 md:mt-0 text-center">
        <p>© 2024 Henry Dwn. All Rights Reserved.</p>
        <p>Made with ❤️ by <a href="">HENRY INXIDE</a></p>
      </div>
        <br />
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
