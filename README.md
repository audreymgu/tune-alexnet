![](https://zenodo.org/badge/DOI/10.5281/zenodo.1037359.svg)

# Notes

This neural network is a fork of Frederik Kratzert's implementation of Alexnet in Tensorflow. It has been configured for training on the two included data sets. Original commentary from Kratzert below; please note, however, that a number of aspects of the discussion below are outdated as a result of alterations to the structure of the repository. There is no longer a **finetune.py** nor **caffe_classes.py**; instead, there are specific tuning scripts and class containers for each dataset, with a two-letter prefix indicating which set each belongs to. The **hd** prefix refers to the "hot dog" dataset, while **ob** refers to the 101 Objects dataset. Checkpoints and tensorboard information are also respectively sorted by dataset under **data/**. As with the original repository, pretrained weights will need to be downloaded in order for this implementation to be run; however, note that this file should be placed in **data/** as opposed to the root directory. This network was trained using tensorflow-cpu 1.4.0.

# Finetune AlexNet with Tensorflow

**Update 15.06.2016**

I revised the entire code base to work with the new input pipeline coming with TensorFlow >= version 1.12rc0. You can find an explanation of the new input pipeline in a new [blog post](https://kratzert.github.io/2017/06/15/example-of-tensorflows-new-input-pipeline.html) You can use this code as before for finetuning AlexNet on your own dataset, only the dependency of OpenCV isn't necessary anymore. The old code can be found in [this past commit](https://github.com/kratzert/finetune_alexnet_with_tensorflow/tree/5d751d62eb4d7149f4e3fd465febf8f07d4cea9d).

This repository contains all the code needed to finetune [AlexNet](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) on any arbitrary dataset. Beside the comments in the code itself, I also wrote an article which you can fine [here](https://kratzert.github.io/2017/02/24/finetuning-alexnet-with-tensorflow.html) with further explanation.

All you need are the pretrained weights, which you can find [here](http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/) or convert yourself from the caffe library using [caffe-to-tensorflow](https://github.com/ethereon/caffe-tensorflow).
If you convert them on your own, take a look on the structure of the `.npy` weights file (dict of dicts or dict of lists).

**Note**: I won't write to much of an explanation here, as I already wrote a long article about the entire code on my blog.

## Requirements

- Python 3
- TensorFlow >= 1.12rc0
- Numpy


## TensorBoard support

The code has TensorFlows summaries implemented so that you can follow the training progress in TensorBoard. (--logdir in the config section of `finetune.py`)

## Content

- `alexnet.py`: Class with the graph definition of the AlexNet.
- `finetune.py`: Script to run the finetuning process.
- `datagenerator.py`: Contains a wrapper class for the new input pipeline.
- `caffe_classes.py`: List of the 1000 class names of ImageNet (copied from [here](http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/)).
- `validate_alexnet_on_imagenet.ipynb`: Notebook to test the correct implementation of AlexNet and the pretrained weights on some images from the ImageNet database.
- `images/*`: contains three example images, needed for the notebook.

## Usage

All you need to touch is the `finetune.py`, although I strongly recommend to take a look at the entire code of this repository. In the `finetune.py` script you will find a section of configuration settings you have to adapt on your problem.
If you do not want to touch the code any further than necessary you have to provide two `.txt` files to the script (`train.txt` and `val.txt`). Each of them list the complete path to your train/val images together with the class number in the following structure.

```
Example train.txt:
/path/to/train/image1.png 0
/path/to/train/image2.png 1
/path/to/train/image3.png 2
/path/to/train/image4.png 0
.
.
```
were the first column is the path and the second the class label.

The other option is that you bring your own method of loading images and providing batches of images and labels, but then you have to adapt the code on a few lines.
