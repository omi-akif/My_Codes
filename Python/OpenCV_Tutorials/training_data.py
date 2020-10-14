#tasted on python 3
import cv2
import imutils.paths as paths

import face_recognition
import pickle
import os
dataset = "G:\\Codes\\Python\\OpenCV_Tutorials\\data\\"
#G:\\Codes\\Python\\OpenCV_Tutorials\\data\\    
#/mnt/g/codes/python/OpenCV_tutorials/data/
# path of the data set #/home/uddin/face_recognition/dsu/
module = "G:\\Codes\\Python\\OpenCV_Tutorials\\encoding2.pickle"
#G:\\Codes\\Python\\OpenCV_Tutorials\\encoding1.pickle  
# #mnt/codes/python/Open_CV_Tutorials/encoding1.pickle"     
# were u want to store the pickle file 
#/home/uddin/face_recognition/encoding1.pickle


imagepaths = list(paths.list_images(dataset))
knownEncodings = []
knownNames = []
for (i, imagePath) in enumerate(imagepaths):
    print("[INFO] processing image {}/{}".format(i + 1,len(imagepaths)))
    name = imagePath.split(os.path.sep)[-2]
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)	
    boxes = face_recognition.face_locations(rgb, model= "hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
       knownEncodings.append(encoding)
       knownNames.append(name)
       print("[INFO] serializing encodings...")
       data = {"encodings": knownEncodings, "names": knownNames}
       output = open(module, "wb") 
       pickle.dump(data, output)
       output.close()