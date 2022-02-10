from imutils import paths #imutils includes opencv functions
import face_recognition as fr
import pickle
import cv2
import os
import imutils #imutils includes opencv functions
import time
from face_recognition_simple import take_photo

def retraining():
    imagePath = list(paths.list_images('employees_list'))
    kEncodings = []
    kNames = []


    #to find path of xml file containing haarCascade file
    cfp = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
    # load the harcaascade in the cascade classifier
    fc = cv2.CascadeClassifier(cfp)
    # load the known faces and embeddings saved in last file
    data = pickle.loads(open('face_enc', "rb").read())
    kEncodings = data["encodings"]
    kNames = data["names"]
    print (kNames)
    # loop over the image paths
    for (i, ip) in enumerate(imagePath):
    # extract the person name from the image path
        name = ip.split(os.path.sep)[-2]
    # load the input image and convert it from BGR
        image = cv2.imread(ip)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = fr.face_locations(rgb,model='hog')
        # compute the facial embedding for the any face
        encodings = fr.face_encodings(rgb, boxes)
        # loop over the encodings
        print("No. of people is {} .".format(i))
        for encoding in encodings:
            kEncodings.append(encoding)
            kNames.append(name)
            

    #save emcodings along with their names in dictionary data
    data = {"encodings": kEncodings, "names": kNames}
    #use pickle to save data into a file for later use
    f = open("face_enc", "wb")
    f.write(pickle.dumps(data))#to open file in write mode
    f.close()#to close file
    return 0

if __name__ == '__main__':
    retraining()