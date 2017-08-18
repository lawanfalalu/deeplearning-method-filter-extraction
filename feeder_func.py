# -*- coding: utf-8 -*-
"""
Created on Tue May 30 02:07:34 2017

@author: FALALU
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:05:44 2017

@author: FALALU
"""
import numpy as np

import imageReader
import tensorflow as tf
import matplotlib.pyplot as plt # just to display images

#Getting List image files and Labels from function getImagesLabel()
files,labels = imageReader.getImageLabel()
#Initializing the graph
 -----------------------------------------------------------------------------

############## Defining the inputs placeholders##############
images_placeholder = tf.placeholder(tf.float32, shape=[None, 2352]) # 28 by 28 by 3-color channel(RBG)
labels_placeholder = tf.placeholder(tf.string, shape=[None])

############### Defining the variables to optimize ###############
weights = tf.Variable(tf.zeros([2352, 10]))
biases = tf.Variable(tf.zeros([10]))

############image reading function()###############
def read_file_format(filenames_queue):
  reader = tf.WholeFileReader()
  _, value = reader.read(filenames_queue)
  img = tf.image.decode_jpeg(value,3)
  return img
############End of read_file_format()##############

                                                   
input_images = read_file_format(tf.train.string_input_producer(files,shuffle=False))
img = tf.convert_to_tensor(input_images)

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  # Start populating the filename queue.
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)
  
  for i in range(len(files)-298): #length of the filename list
    image = sess.run(input_images) #here is the image Tensor :) 
    print(image)
    plt.imshow(image)
    #plt.imshow(mani)
    plt.show()
  coord.request_stop()
  coord.join(threads)
