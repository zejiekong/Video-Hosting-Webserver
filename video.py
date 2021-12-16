
# importing necessary libraries
import dropbox
import re
from flask import Flask, render_template
import json

app = Flask(__name__)

file_list = []
link_list = []

# Token Generated from dropbox
#TOKEN = ""
  
# Establish connection
def connect_to_dropbox():
    
    try:
        dbx = dropbox.Dropbox(TOKEN)
        print('Connected to Dropbox successfully')
      
    except Exception as e:
        print(str(e))
      
    return dbx
  
dbx = connect_to_dropbox()
for entry in dbx.files_list_folder('/vids/', recursive=True).entries:
    if isinstance(entry, dropbox.files.FileMetadata):
        file_list.append(entry.path_display)

for i in file_list:
    link = str(dbx.sharing_list_shared_links(i))
    link_list.append((re.findall("url='(.*)dl=0'",link)[0])+ "raw=1#t=0.001'")


json_object = json.dumps(link_list)

@app.route('/')
def hi():
    return render_template("index.html",vid_link=json_object)

if __name__ == "__main__":
    app.run()

