import tensorflow as tf
import brainvision as bv
import os


header: str = "/data/test.vhdr"
header2: str = "/data/blastnice_20141023_21.vhdr"
cwd = os.getcwd()

#hello = tf.constant('Hello, TensorFlow!')
#sess = tf.Session()
#print(sess.run(hello))

print(cwd+header)
bv.read_brainvis_triplet(cwd+header2)
#bv.read_header(cwd+header)

