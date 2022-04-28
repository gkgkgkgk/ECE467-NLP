import tensorflow as tf
import numpy as np
import os
import time

trainingFile = "starwars.txt"
rawText = open(trainingFile, 'rb').read().decode('utf-8')
print("Succesfully read training file. Length:", len(rawText))
print("Beginning of text:", rawText[:1000])

characters = sorted(list(set(rawText)))
print("Total unique characters:", len(characters))

ids = tf.keras.layers.StringLookup(vocabulary=characters, mask_token=None)
ids = ids(rawText)
idsDataset = tf.data.Dataset.from_tensor_slices(ids)

