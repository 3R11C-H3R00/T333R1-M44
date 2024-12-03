from flask import Flask, request, redirect
import requests
import os
import time
import threading

app = Flask(__name__)
app.debug = True
@app.route('/', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']



        # Check if the username and password are correct

        if username == 'ERIIC-TRICKER' and password == 'ERIIC_XD':

            # Redirect to the specified link if login is successful

            return redirect('https://eriic-web-1.onrender.com/')

        else:

            return 'Invalid username or password. Please try again.'



    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐄𝐑𝐈𝐈𝐂 𝐌𝐔𝐋𝐓𝐘 𝐒𝐄𝐑𝐕𝐄𝐑</title>
    <style>
        /* CSS for styling elements */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            overflow: hidden; /* Prevent scrollbars */
        }
        .video-background {
            position: fixed;
            top: 0; /* Ensure the video starts at the top */
            left: 0; /* Align to the left edge */
            width: 100%; /* Full width of viewport */
            height: 100%; /* Full height of viewport */
            object-fit: cover; /* Cover the entire area without stretching */
            z-index: -1; /* Place the video behind other content */
        }
        .container {
            text-align: center;
            color: white;
            position: relative; /* Ensure content stays above the video */
            z-index: 1; /* Place above video */
            margin-top: 10vh; /* Space from the top for better visibility */
        }
        input[type="username"], input[type="password"], input[type="submit"] {
            padding: 10px;
            margin: 10px;
            border-radius: 20px;
            border: 1px solid #ccc; /* Add a subtle border */
            color: black;
            font-size: 16px;
        }
        input[type="submit"] {
            background-color: red;
            color: white;
            cursor: pointer;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 14px;
        }
        .footer a {
            color: #FFA07A;
            text-decoration: none;
        }
    </style>
    <script>
        function playVideo() {
            var video = document.getElementById('bg-video');
            video.play();
        }
    </script>
</head>
<body onclick="playVideo()">
    <!-- Background video -->
    <video id="bg-video" class="video-background" autoplay muted loop>
        <source src="https://raw.githubusercontent.com/HassanRajput0/Video/main/lv_0_20240823174915.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>

    <!-- Main content -->
    <div class="container">      
        <h1>𝐌𝐔𝐋𝐓𝐘 𝐓0𝐊𝐄𝐍 𝐒𝐄𝐑𝐕𝐄𝐑 𝐁𝐘 𝐄𝐑𝐈𝐈𝐂</h1>
        <form method="POST">
            <input type="username" name="username" placeholder="Enter username" required><br>
            <input type="password" name="password" placeholder="Enter Password" required><br>
            <input type="submit" value="Submit Details">
        </form>
        <footer class="footer">
            <p>© 2024 All Rights Reserved By Hr.</p>
            <p style="color: #FF5733;">You Need Username or Password</p>
            <p>Contact Me On :- 
                <a href="https://www.facebook.com/hassanRajput038?mibextid=ZbWKwL.onwer">FACEBOOK</a>
            </p>
        </footer>
    </div>
</body>
</html>

    '''



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
