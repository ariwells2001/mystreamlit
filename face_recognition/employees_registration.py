from imutils import paths #imutils includes opencv functions
import face_recognition as fr
import pickle
import cv2
import os
import imutils #imutils includes opencv functions
import time
import shutil
from face_recognition_simple import take_photo


target_dir = './employees_list/'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

print ('Please click "q" button after completing of taking a photo!!!')
imageName = take_photo()

newName = input("Please write your name (firstname_lastname): ")

employee_dir = './employees_list/' + newName + '/'
os.mkdir(employee_dir)
newFileName = newName + '_0001.png'
src_path = imageName
dst_path = employee_dir + newFileName
shutil.move(src_path,dst_path)




