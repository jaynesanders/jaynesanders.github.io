head = """<html>
  <head>
    <title>Jayne Sanders</title>
    <script src='js/jquery-1.11.0.min.js'></script>
    <script src='js/lightbox.min.js'></script>
    <link href='css/screen.css' rel='stylesheet' />
    <link href='css/lightbox.css' rel='stylesheet' />
    <link href='css/style.css' rel='stylesheet' />
  </head>
  <body>
    <div id='header'>
      <ul class='nav'>
        <li><a href='index.html'>Jayne Sanders</a></li>
        <li><a href='sculpture.html'>Sculpture</a></li>
        <li><a href='drawing.html'>Drawing</a></li>
        <li><a href='video.html'>Video</a></li>
        <li><a href='bio.html'>Bio</a></li>
        <li><a href='contact.html'>Contact</a></li>
      </ul>
    </div>
    <div id="contents">
"""

tail = """    </div>
  </body>
</html>
"""

import os

folder_files = os.listdir('pages/')

for file in folder_files:
    f1 = open("pages/"+file, "r")
    f2 = open(file, "w")
    f2.write(head)
    f2.write(f1.read())
    f2.write(tail)
    f1.close()
    f2.close()
