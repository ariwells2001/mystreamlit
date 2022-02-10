import sys
import os
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense, Activation
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras import callbacks
import time
from keras.models import load_model
from keras import backend as K
from PIL import Image
from pathlib import Path
import os



def retrain():
    start = time.time()

    DEV = False
    argvs = sys.argv
    argc = len(argvs)

    if argc > 1 and (argvs[1] == "--development" or argvs[1] == "-d"):
      DEV = True

    if DEV:
      epochs = 2
    else:
      epochs = 4

    train_data_path = 'C:/Users/rkarm/Downloads/Data/Train/'
    validation_data_path = 'C:/Users/rkarm/Downloads/Data/Test/'
    
    """
    Parameters
    """
    img_width, img_height = 300,300
    batch_size = 32
    samples_per_epoch = 400
    validation_steps = 300
    nb_filters1 = 64
    nb_filters2 = 32
    conv1_size = 5
    conv2_size = 3
    pool_size = 3
    classes_num = 4
    lr = 0.002

 


# Ari Wells
    def load_image(image_file):
        img = Image.open(image_file)
        return img


    test_path = 'C:/Users/rkarm/Downloads/Data/Test'


    target_dir = './ariwells/'

    if not os.path.exists(target_dir):
         os.mkdir(target_dir)


#Load the pre-trained models
    model_weights_path = './models/weights.h5'
    model_path = './models/model.h5'
    model = load_model(model_path)
    model.load_weights(model_weights_path)
    #model.compile(loss='categorical_crossentropy',
     #             optimizer="adam",
     #             metrics=['accuracy'])

    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        train_data_path,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical')

    validation_generator = test_datagen.flow_from_directory(
        validation_data_path,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical')

    """
    Tensorboard log
    """
    log_dir = './tf-log/'
    tb_cb = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0)
    cbks = [tb_cb]

    model.fit_generator(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        callbacks=cbks,
        validation_steps=validation_steps)

    #target_dir = './models/'
    #if not os.path.exists(target_dir):
      #os.mkdir(target_dir)
    model.save('./models/model.h5')
    model.save_weights('./models/weights.h5')

    #Calculate execution time
    end = time.time()
    dur = end-start

    if dur<60:
        print("Execution Time:",dur,"seconds")
    elif dur>60 and dur<3600:
        dur=dur/60
        print("Execution Time:",dur,"minutes")
    else:
        dur=dur/(60*60)
        print("Execution Time:",dur,"hours")


if __name__ == "__retrain__":
    retrain()