import tensorflow as tf
mark1 = tf.constant("Detectrone Mark I")
session = tf.Session()
print(session.run(mark1))
print("Merhaba Dünya")
print("Merhaba Oğuz")
print("Merhaba Detectrone")
print("Again Merhaba Detectrone Family")
print(tf.__version__)

