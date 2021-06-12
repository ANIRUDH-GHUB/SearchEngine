# from flask import Flask, render_template, request, redirect, url_for
# from wikipedia.wikipedia import summary
# from prediction import recognizer
# from wiki import give_details
# import os
# from PIL import Image
# import base64
# import io
# app = Flask(__name__)

# @app.route('/')
# def index():
    # image1,image2,image3=getImageData("taj")
    # return render_template("index.html")
    # return render_template("Home.html",image1=image1,image2=image2,image3=image3)
#     # return render_template('Home.html',place="taj")

# @app.route('/', methods=['POST'])
# def upload_file():
#     uploaded_file = request.files['file']
#     if uploaded_file.filename != '':
#         uploaded_file.save(uploaded_file.filename)
#         res = recognizer(uploaded_file.filename)
#         summary = give_details(res)
#         os.remove(uploaded_file.filename)
#     return render_template("Home.html", res = summary)


# if __name__ == '__main__':
#    app.run(debug = True)
from flask import Flask, render_template, request, redirect, url_for
from wikipedia.wikipedia import summary
from prediction import recognizer
from wiki import give_details
import os
from PIL import Image
import base64
import io
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        res = recognizer(uploaded_file.filename)
        summary = give_details(res)
        os.remove(uploaded_file.filename)
    image1,image2,image3=getImageData("taj")
    return render_template("Home.html",image1=image1,image2=image2,image3=image3)
def getImageData(monument):
    li=[]
    for i in range(3):
        im = Image.open("images/"+monument+"/"+monument+str(i+1)+".jpg")
        data = io.BytesIO()
        im.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())
        img_data=encoded_img_data.decode('utf-8')
        li.append(img_data)
    return li	
if __name__ == '__main__':
   app.run(debug = True)