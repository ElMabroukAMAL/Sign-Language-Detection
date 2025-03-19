from Sign_Language.pipeline.train_pipeline import TrainPipeline
import os, sys
from Sign_Language.exception import SignException
from Sign_Language.utils.main_utils import encodeImageIntoBase64, decodeImage
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
import subprocess # close the camera
import shutil
app = Flask(__name__)
CORS(app)


class ClientAPP:
    def __init__(self):
        """
        Constructor method that initializes the default input image filename.
        """
        self.filename = "inputImage.jpg"


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/train")
def trainRoute(): 
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 



@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image'] # the image in format base64
        decodeImage(image, c1.filename) # decode from base64 to image in "Data/filename"

        # detection
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../Data/inputImage.jpg")

        # after detection, encode the image to base64
        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        # send the image to the frontend
        result = {"image": opencodedbase64.decode('utf-8')}

        shutil.rmtree("yolov5/runs")
        

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)



@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
        shutil.rmtree("yolov5/runs")
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    

if __name__ == "__main__":
    c1 = ClientAPP()
    app.run(host="0.0.0.0", port=8000)

