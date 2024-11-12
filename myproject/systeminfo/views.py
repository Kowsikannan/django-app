from django.http import HttpResponse
import os
import time
import subprocess

def htop(request):
    # Get system info
    name = "Kowsalya"  # Replace with your full name
    username = os.getlogin()
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Run the top command and capture output
    top_output = subprocess.check_output(['top', '-n', '1'], universal_newlines=True)

    # Return HTML response formatted like the screenshot
    return HttpResponse(f"""
    <html>
    <head><title>System Information</title></head>
    <body>
        <h1>System Info</h1>
        <p>Name: {name}</p>
        <p>Username: {username}</p>
        <p>Server Time (IST): {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """)
