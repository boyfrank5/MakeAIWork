import numpy as np
from pandas import array
import tensorflow as tf
keras = tf.keras

filename = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/l_test_data1.samples' 
# filename = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/l_test_data2.samples' 
# filename = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/l_test_data3.samples' # lidar_track aangepast waar de de auto standaard botste in de linker onderhoek

lidar_data = np.loadtxt(filename, dtype=float, max_rows= 5000, usecols= (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
lidar_steeringAngle = np.loadtxt(filename, dtype=float, max_rows= 5000, usecols= (16,))

lidar_data_val = lidar_data[1000:1300]
lidar_steeringAngle_val = lidar_steeringAngle[1000:1300]

model = tf.keras.Sequential([
  tf.keras.Input(shape=(16,)),
  tf.keras.layers.Dense(128, activation='relu'), 
  tf.keras.layers.Dense(128, activation='relu'), 
  tf.keras.layers.Dense(128, activation='relu'), 
  tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', #uitzoeken
  loss=tf.keras.losses.MeanSquaredError(), #uitzoeken
  metrics=['accuracy']) #uitzoeken. Een andere parameter ipv "accurarcy" mogelijk gewenst.

model.fit(lidar_data, lidar_steeringAngle, epochs=150)
print()
print('Evaluation:')
model.evaluate(lidar_data_val, lidar_steeringAngle_val) #uitzoeken
print()

#model.save('/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/l_tf_model')





'''
# use the below code in the drivingAgent.
model.save('/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/l_tf_model')
predictions = new_model.predict([sonar_data])


learing rate option. However, showed compiler2 showed better results. 
model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
  loss=tf.keras.losses.MeanSquaredError(),
  metrics=['accuracy'])
'''
