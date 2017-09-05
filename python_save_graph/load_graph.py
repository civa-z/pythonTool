import tensorflow as tf
import os
import numpy as np
from tensorflow.python.platform import gfile

with gfile.FastGFile("models/graph.pb",'rb') as f:
	graph_def = tf.GraphDef()
	print type(graph_def)
	print dir(graph_def)
	graph_def.ParseFromString(f.read())
	tf.import_graph_def(graph_def, name='')
	with tf.Session() as sess:
		for node in graph_def.node:
			if -1 != node.name.find("nWeights"):
				print sess.run(sess.graph.get_operation_by_name(node.name))
				print node.name
		print sess.run(sess.graph.get_tensor_by_name("c:0"))
