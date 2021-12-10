from flask import *
import os

song = None


try:
 from youtube_dl import YoutubeDL
except:
 os.system('python3 -m pip install --user youtube_dl')
 from youtube_dl import YoutubeDL


try:
 from youtubesearchpython import Search
except:
 os.system('python3 -m pip install --user youtube-search-python')
 from youtubesearchpython import Search

app = Flask(__name__)


@app.route('/robots.txt')
def noindex():
    r = Response(response="User-Agent: *\nAllow: /\n",status=200, mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r


@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta http-equiv="Content-Security-Policy" content="script-src 'none'">
    <meta http-equiv="Content-Security-Policy" content="frame-ancestors 'none'">
    <meta http-equiv="Content-Security-Policy" content="sandbox 'none'">
    <meta http-equiv="Content-Security-Policy" content="object-src 'none'">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <meta charset=UTF-8>
    <meta http-equiv="Content-Type" content="text/html">
    <meta http-equiv="Content-Type" content="multipart/form-data; boundary=something">
    <title>Youtube Downloader Website Open Source</title>
    <link rel="icon" href="https://i.pinimg.com/236x/45/3f/77/453f7773cd911372728a3147f17f8a3d.jpg" type="image/x-icon">
    <meta property="og:image" content="https://i.pinimg.com/236x/45/3f/77/453f7773cd911372728a3147f17f8a3d.jpg">
    <meta property="og:title" content="Youtube Download By Indra">
    <meta name="description" content="Buat download Video dan Lagu dari Youtube, coded by Xnuvers007">
    <meta property="og:author" content="Xnuvers007">
    <link rel="preload">
    <style>
        font-display: optional;
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <center>
    <iframe src="https://freesecure.timeanddate.com/clock/i7h99ycq/n108/fn7/fs17/tct/pct/ftb/tt0/th1/ta1" frameborder="0" width=100% height="30" allowtransparency="true" title="Jam"></iframe>
    <br>
    </center>
    <center>
    <img src="https://i.pinimg.com/236x/bd/e2/df/bde2df967ccdf8750653064784a3e4b5.jpg"
        srcset="https://i.pinimg.com/236x/bd/e2/df/bde2df967ccdf8750653064784a3e4b5.jpg 4x" width="235" height="393" alt="gambar gan :V">
    <h2>Enter Any Song name or youtube url to download it</h2>
    <h4>
    <form action="/get" method="post">
    <label>
    enter name of the song / url =
	<input type="text" name="song_name">
	</label>
    <p></p>
    <input type="submit" name="get_audio" value="Get Audio">
    <input type="submit" name="get_video" value="Get Video">
    <p>A Simple Python Website for Download Songs</p>
    <p>Created with ❤️️ by Indra/Xnuvers007</p>
    <a href="https://github.com/xnuvers007/">My Github, please visit</a>
    <br>
    <b> Create with python for backend and html for page </b>
    </h4>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>


    </center>
    </body>
    </html>
'''



@app.route('/get', methods=['post'])
def track():
    if request.method == 'POST':
     try:
        song = str(request.form['song_name'])
        if not song:
           return "Please Enter Song Name"
        if 'get_audio' in request.form:
          ty = "mp3"
          opts = {'format':'bestaudio','addmetadata':True,'key':'FFmpegMetadata','writethumbnail':True,'prefer_ffmpeg':True,'geo_bypass':True,'nocheckcertificate':True,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}],'outtmpl':'%(id)s.mp3','quiet':True,'logtostderr':False}
        elif 'get_video' in request.form:
          ty = "mp4"
          opts = {'format':'best','addmetadata':True,'key':'FFmpegMetadata','writethumbnail':True,'prefer_ffmpeg':True,'geo_bypass':True,'nocheckcertificate':True,'postprocessors': [{'key': 'FFmpegVideoConvertor','preferedformat': 'mp4'}],'outtmpl':'%(id)s.mp4','logtostderr':False,'quiet':True}
        else:
            return "Select audio/video Type"
        test = os.listdir()
        if len(test) > 20:
         for item in test:
          if item.endswith(".mp3") or item.endswith(".webp") or item.endswith(".jpg") or item.endswith(".png") or item.endswith(".mp4"):
             os.remove(item)
        if "http" in song:
           url = song
        else:
          songa = Search(f'{song} song', limit = 1)
          songa = songa.result()['result']
          if not songa:
            return "Error Failed to find this song"
          url = songa[0]['link']
        try:
         with YoutubeDL(opts) as rip:
           rip_data = rip.extract_info(url)
        except Exception as e:
           return str(e)
        if ty == "mp3":
           ty2 = f"{rip_data['id']}.mp3"
        else:
           ty2 = f"{rip_data['id']}"
        if os.path.isfile(f"{ty2}.webp"):
            im = f"/static/{ty2}.webp"
        elif os.path.isfile(f"{ty2}.jpg"):
            im = f"/static/{ty2}.jpg"
        else:
            im = f"/static/{ty2}.png"
        return f'''
        <head>
        <meta charset=UTF-8>
        <div color="black" id="kopi-covid"></div>
  <script type="text/javascript">
    var f = document.createElement("iframe");
    f.src = "https://kopi.dev/widget-covid-19/";
    f.width = "100%";
    f.height = 380; <!-- 380 -->
    f.scrolling = "no";
    f.frameBorder = 0;
    var rootEl = document.getElementById("kopi-covid");
    console.log(rootEl);
    rootEl.appendChild(f);
  </script>
        <meta http-equiv="Content-Type" content="text/html">
        <meta http-equiv="Content-Type" content="multipart/form-data; boundary=something">
        <title>Youtube Downloader Website Open Source</title>
        <link rel="icon" href="https://i.pinimg.com/236x/45/3f/77/453f7773cd911372728a3147f17f8a3d.jpg" type="image/x-icon">
        <meta property="og:image" content="https://i.pinimg.com/236x/45/3f/77/453f7773cd911372728a3147f17f8a3d.jpg">
        <meta property="og:title" content="Youtube Download By Indra">
        <meta property="og:description" content="Buat download Video dan Lagu dari Youtube">
        <meta property="og:author" content="Xnuvers007">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
            <center>
    <iframe src="https://freesecure.timeanddate.com/clock/i7h99ycq/n108/fn7/fs17/tct/pct/ftb/tt0/th1/ta1" frameborder="0" width=100% height="30" allowtransparency="true" title="Jam"></iframe>
    </center>
        <center>
        <img src="{im}" alt="Song" width="100%" height="50%">
        <p> </p>
        <h2>{rip_data['title']}</h2>
        <p> </p>
        <h3>
        <video width="350" height="250" controls>
        <source src="/static/{rip_data['id']}.{ty}" type="video/ogg">
        Your browser does not support the video tag.
        </video>
        <p></p>
        <a href="/static/{rip_data['id']}.{ty}" download="{rip_data['title']}.{ty}">Click Here To Download</a>
        </audio>
        </h3>
        <center>
        '''
     except Exception as e:
         return str(e)

@app.route('/find')
def help():
    if not 'song_name' in request.form:
           return "Please Enter Song Name"
    return "ok"
