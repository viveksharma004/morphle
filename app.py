from flask import Flask, render_template
import os
import subprocess
import datetime
import getpass 

app = Flask(__name__)

@app.route("/htop")
def htop_endpoint():
    name = "Vivek Sharma"  

    try:
        username = getpass.getuser() 
    except Exception as e:
        username = f"Error getting username: {e}"

    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    server_time_ist = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    try:
        top_output = subprocess.check_output(['top', '-n', '1', '-b'], text=True)
    except subprocess.CalledProcessError as e:
        top_output = f"Error executing top: {e}"

    return render_template("htop.html", name=name, username=username, server_time=server_time_ist, top_output=top_output)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)