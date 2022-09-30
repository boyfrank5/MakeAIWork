import numpy as np
import tensorflow as tf
keras = tf.keras

filename = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/sonar_log1.samples' #Use copy path

sonar_data = np.loadtxt(filename, dtype=float, max_rows= 1500, usecols= (0,1,2,))
# print(sonar_data)

sonar_steeringAngle = np.loadtxt(filename, dtype=float, max_rows= 1500, usecols= (3,))
# print(sonar_steeringAngle)


model = tf.keras.Sequential([
  tf.keras.Input(shape=(3,)),
  tf.keras.layers.Dense(15, activation='relu'),
  tf.keras.layers.Dense(15, activation='relu'),
  tf.keras.layers.Dense(1)
])

model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001),
  loss=tf.keras.losses.MeanSquaredError(),
  metrics=['accuracy'])


model.fit(sonar_data, sonar_steeringAngle, epochs=10)







