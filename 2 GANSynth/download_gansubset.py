import tensorflow as tf
import tensorflow_datasets as tfds

#tfds.list_builders()
#tfds.load("nsynth/gansynth_subset")
TFDS_DATA_DIR = "/mnt/d/THESIS DUMP/gansubset" #change this to your liking.

tfds.load("nsynth/gansynth_subset",download=True, split="train") #data_dir="gansubset2"
#assert isinstance(load_dataset, tf.data.Dataset)
