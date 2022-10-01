import numpy as np
import tensorflow as tf
keras = tf.keras

filename = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/sonar_log1.samples' #Use copy path

sonar_data = np.loadtxt(filename, dtype=float, max_rows= 500, usecols= (0,1,2,))
# print(sonar_data)

sonar_steeringAngle = np.loadtxt(filename, dtype=float, max_rows= 500, usecols= (3,))
# print(sonar_steeringAngle)

#if False:
model = tf.keras.Sequential([
  tf.keras.Input(shape=(3,)),
  tf.keras.layers.Dense(16, activation='relu'),
  tf.keras.layers.Dense(32, activation='relu'),
  tf.keras.layers.Dense(16, activation='relu'),
  tf.keras.layers.Dense(1)
])

# model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001),
#   loss=tf.keras.losses.MeanSquaredError(),
#   metrics=['accuracy'])

model.compile(optimizer='adam',
  loss=tf.keras.losses.MeanSquaredError(),
  metrics=['accuracy'])


model.fit(sonar_data, sonar_steeringAngle, epochs=150)

model.save('/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/sonar_trained_model')

#new_model = tf.keras.models.load_model('/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/trainedModel')
#predictions = new_model.predict([sonar_data])
#print(predictions)

