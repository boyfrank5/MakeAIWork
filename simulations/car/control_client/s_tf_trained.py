import numpy as np
import tensorflow as tf
keras = tf.keras

filename = '/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/s_test_data.samples'

sonar_data = np.loadtxt(filename, dtype=float, max_rows= 1000, usecols= (0,1,2,))
sonar_steeringAngle = np.loadtxt(filename, dtype=float, max_rows= 1000, usecols= (3,))

sonar_data_val = sonar_data[500:700]
sonar_steeringAngle_val = sonar_steeringAngle[500:700]

model = tf.keras.Sequential([
  tf.keras.Input(shape=(3,)),   # input; sensoren 1 t/m 3.
  tf.keras.layers.Dense(16, activation='relu'), # hidden layer nr1. Relu is het NN trainingsproces koppeld gewichten aan de output.
  tf.keras.layers.Dense(16, activation='relu'), # hidden layer nr2.
  tf.keras.layers.Dense(1)   # output; 1 x stuurhoek.
])

#compiler2, configureren berekening
model.compile(optimizer='adam',   # Adam is een vervanger van gradient decent met als voordeel deze minder 'snel' blijft hangen tussen bepaalde waarde. 
  loss=tf.keras.losses.MeanSquaredError(),  # De loss functie verteld hoeveel de voorspelde output in het model verschilt met de 'echte' output. 
  metrics=['accuracy'])

model.fit(sonar_data, sonar_steeringAngle, epochs=500)

print()
print('Evaluation:')
model.evaluate(sonar_data_val, sonar_steeringAngle_val)
print()


# model.save('/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/s_tf_model')


'''
# learing rate option. However, showed compiler2 showed better results.

model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001),
  loss=tf.keras.losses.MeanSquaredError(),
  metrics=['accuracy'])
'''

# use the below code in the drivingAgent.
#model.save('/Users/boyfrankclaesen/MakeAIWork/simulations/car/control_client/s_tf_model')
#predictions = new_model.predict([sonar_data])

