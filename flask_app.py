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

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <!-- <meta http-equiv="Content-Security-Policy" content="script-src 'none'"> -->
    <!-- <meta http-equiv="Content-Security-Policy" content="frame-ancestors 'none'"> -->
    <!-- <meta http-equiv="Content-Security-Policy" content="sandbox 'none'"> -->
    <!-- <meta http-equiv="Content-Security-Policy" content="object-src 'none'"> -->
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
<div class="container col-sm-4 col-md-7 col-lg-4 mt-5">
    <div class="card">
        <h3 class="card-header" id="monthAndYear"></h3>
        <table class="table table-bordered table-responsive-sm" id="calendar">
            <thead>
            <tr>
                <th>Sun</th>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
            </tr>
            </thead>

            <tbody id="calendar-body">

            </tbody>
        </table>

        <div class="form-inline">

            <button class="btn btn-outline-primary col-sm-6" id="previous" onclick="previous()">Previous</button>

            <button class="btn btn-outline-primary col-sm-6" id="next" onclick="next()">Next</button>
        </div>
        <br/>
        <form class="form-inline">
            <label class="lead mr-2 ml-2" for="month">Jump To: </label>
            <select class="form-control col-sm-4" name="month" id="month" onchange="jump()">
                <option value=0>Jan</option>
                <option value=1>Feb</option>
                <option value=2>Mar</option>
                <option value=3>Apr</option>
                <option value=4>May</option>
                <option value=5>Jun</option>
                <option value=6>Jul</option>
                <option value=7>Aug</option>
                <option value=8>Sep</option>
                <option value=9>Oct</option>
                <option value=10>Nov</option>
                <option value=11>Dec</option>
            </select>


            <label for="year"></label><select class="form-control col-sm-4" name="year" id="year" onchange="jump()">
            <option value=1990>1990</option>
            <option value=1991>1991</option>
            <option value=1992>1992</option>
            <option value=1993>1993</option>
            <option value=1994>1994</option>
            <option value=1995>1995</option>
            <option value=1996>1996</option>
            <option value=1997>1997</option>
            <option value=1998>1998</option>
            <option value=1999>1999</option>
            <option value=2000>2000</option>
            <option value=2001>2001</option>
            <option value=2002>2002</option>
            <option value=2003>2003</option>
            <option value=2004>2004</option>
            <option value=2005>2005</option>
            <option value=2006>2006</option>
            <option value=2007>2007</option>
            <option value=2008>2008</option>
            <option value=2009>2009</option>
            <option value=2010>2010</option>
            <option value=2011>2011</option>
            <option value=2012>2012</option>
            <option value=2013>2013</option>
            <option value=2014>2014</option>
            <option value=2015>2015</option>
            <option value=2016>2016</option>
            <option value=2017>2017</option>
            <option value=2018>2018</option>
            <option value=2019>2019</option>
            <option value=2020>2020</option>
            <option value=2021>2021</option>
            <option value=2022>2022</option>
            <option value=2023>2023</option>
            <option value=2024>2024</option>
            <option value=2025>2025</option>
            <option value=2026>2026</option>
            <option value=2027>2027</option>
            <option value=2028>2028</option>
            <option value=2029>2029</option>
            <option value=2030>2030</option>
            <option value=2031>2031</option>
            <option value=2032>20302</option>
            <option value=2033>2033</option>
            <option value=2034>2034</option>
            <option value=2035>2035</option>
            <option value=2036>2036</option>
            <option value=2037>2037</option>
            <option value=2038>2038</option>
            <option value=2039>2039</option>
            <option value=2040>2040</option>
        </select></form>
    </div>
</div>
<script type="text/javascript">
today = new Date();
currentMonth = today.getMonth();
currentYear = today.getFullYear();
selectYear = document.getElementById("year");
selectMonth = document.getElementById("month");

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

monthAndYear = document.getElementById("monthAndYear");
showCalendar(currentMonth, currentYear);


function next() {
    currentYear = (currentMonth === 11) ? currentYear + 1 : currentYear;
    currentMonth = (currentMonth + 1) % 12;
    showCalendar(currentMonth, currentYear);
}

function previous() {
    currentYear = (currentMonth === 0) ? currentYear - 1 : currentYear;
    currentMonth = (currentMonth === 0) ? 11 : currentMonth - 1;
    showCalendar(currentMonth, currentYear);
}

function jump() {
    currentYear = parseInt(selectYear.value);
    currentMonth = parseInt(selectMonth.value);
    showCalendar(currentMonth, currentYear);
}

function showCalendar(month, year) {

    let firstDay = (new Date(year, month)).getDay();

    tbl = document.getElementById("calendar-body"); // body of the calendar

    // clearing all previous cells
    tbl.innerHTML = "";

    // filing data about month and in the page via DOM.
    monthAndYear.innerHTML = months[month] + " " + year;
    selectYear.value = year;
    selectMonth.value = month;

    // creating all cells
    let date = 1;
    for (let i = 0; i < 6; i++) {
        // creates a table row
        let row = document.createElement("tr");

        //creating individual cells, filing them up with data.
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                cell = document.createElement("td");
                cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }
            else if (date > daysInMonth(month, year)) {
                break;
            }

            else {
                cell = document.createElement("td");
                cellText = document.createTextNode(date);
                if (date === today.getDate() && year === today.getFullYear() && month === today.getMonth()) {
                    cell.classList.add("bg-info");
                } // color today's date
                cell.appendChild(cellText);
                row.appendChild(cell);
                date++;
            }


        }

        tbl.appendChild(row); // appending each row into calendar body.
    }

}


// check how many days in a month code from https://dzone.com/articles/determining-number-days-month
function daysInMonth(iMonth, iYear) {
    return 32 - new Date(iYear, iMonth, 32).getDate();
}
</script>
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
        <meta http-equiv="Content-Type" content="text/html">
        <meta http-equiv="Content-Type" content="multipart/form-data; boundary=something">
        <title>Youtube Downloader Website Open Source</title>
        <link rel="icon" href="https://i.pinimg.com/236x/45/3f/77/453f7773cd911372728a3147f17f8a3d.jpg" type="image/x-icon">
        <meta property="og:image" content="https://i.pinimg.com/236x/45/3f/77/453f7773cd911372728a3147f17f8a3d.jpg">
        <meta property="og:title" content="Youtube Download By Indra">
        <meta name="description" content="Buat download Video dan Lagu dari Youtube">
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
        </audio.
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
