from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf


#Data
train_data = open('ALGO_DATA.csv', 'r')
test_data = open('ALGO_DATA.csv', 'r')

#Neural Network Mode
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

#Optimizer
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


#Fit Model
model.fit(train_data, test_data, epochs=5)

#Evaluate Model
model.evaluate(x_test, y_test)
