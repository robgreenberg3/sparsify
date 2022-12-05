
<!--
Copyright (c) 2021 - present / Neuralmagic, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<h1><img alt="tool icon" src="https://raw.githubusercontent.com/neuralmagic/sparsify/main/docs/source/icon-sparsify.png" />&nbsp;&nbsp;Sparsify APIs</h1>

<h3>Sparsify APIs provide simple pathways to build sparse models, all with a one-line API call. </h3>

<p>
    <a href="https://docs.neuralmagic.com/sparsify/">
        <img alt="Documentation" src="https://img.shields.io/badge/documentation-darkred?&style=for-the-badge&logo=read-the-docs" height=25>
    </a>
    <a href="https://join.slack.com/t/discuss-neuralmagic/shared_invite/zt-q1a1cnvo-YBoICSIw3L1dmQpjBeDurQ/">
        <img src="https://img.shields.io/badge/slack-purple?style=for-the-badge&logo=slack" height=25>
    </a>
    <a href="https://github.com/neuralmagic/sparsify/issues">
        <img src="https://img.shields.io/badge/support%20forums-navy?style=for-the-badge&logo=github" height=25>
    </a>
    <a href="https://github.com/neuralmagic/sparsify/actions/workflows/quality-check.yaml">
        <img alt="Main" src="https://img.shields.io/github/workflow/status/neuralmagic/sparsify/Quality%20Checks/main?label=build&style=for-the-badge" height=25>
    </a>
    <a href="https://github.com/neuralmagic/sparsify/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/neuralmagic/sparsify.svg?style=for-the-badge" height=25>
    </a>
    <a href="https://github.com/neuralmagic/sparsify/blob/main/LICENSE">
        <img alt="GitHub" src="https://img.shields.io/github/license/neuralmagic/sparsify.svg?color=lightgray&style=for-the-badge" height=25>
    </a>
    <a href="https://github.com/neuralmagic/sparsify/blob/main/CODE_OF_CONDUCT.md">
        <img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg?color=yellow&style=for-the-badge" height=25>
    </a>
    <a href="https://www.youtube.com/channel/UCo8dO_WMGYbWCRnj_Dxr4EA">
        <img src="https://img.shields.io/badge/-YouTube-red?&style=for-the-badge&logo=youtube&logoColor=white" height=25>
    </a>
     <a href="https://medium.com/limitlessai">
        <img src="https://img.shields.io/badge/medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white" height=25>
    </a>
    <a href="https://twitter.com/neuralmagic">
        <img src="https://img.shields.io/twitter/follow/neuralmagic?color=darkgreen&label=Follow&style=social" height=25>
    </a>
</p>

## Overview

Use the Sparsify APIs to easily create sparse, performant models. Bring a dense model, a dataset, or just a task; Sparsify APIs will help deliver you a sparse model that is ready and packaged for deployment on your target hardware.

Sparsify APIs make applying state-of-the-art [sparsification](https://docs.neuralmagic.com/main/source/getstarted.html#sparsification) algorithms such as pruning and quantization to any neural network easy with one-command API calls that return packaged, ready-to-deploy sparse models. 
## Available APIs

As of today, Sparsify has 2 available APIs: 
```bash
- sparsify.package 
- sparsify.auto
```
- **sparsify.package** takes in a task *or* research dataset as parameters and returns a packaged ONNX model with configs; ready to plug in directly into DeepSparse or any inference engine for inferencing. 
- **sparsify.auto** takes a task *or* research dataset *and* your dataset that they wish to Sparse Transfer Learn the model onto as parameters and starts training locally on your training hardware. The Sparsify Auto API returns a packaged ONNX model with configs, ready to plug in directly into DeepSparse or any inference engine for inferencing. 

## Sparsify Package Usage and Parameters 


### Task/Dataset Selection:
To use the Sparsify Package API, you must choose a task or a dataset that you wish to get a deployable, packaged sparse model for.  You are required to select at least one of a task or a dataset, but not required to select both. 
    
   
   **Tasks**
   You can select from the following lists of supported list of tasks (--task) to create a performant model for: 
-   CV classification: [*ic, image-classification, image_classification, classification*]
-   CV detection: [*od, object-detection, object_detection, detection*]
-   CV segmentation: [*segmentation*]
-   NLP question answering: [*qa, question-answering, question_answering*]
-   NLP text classification: [*text-classification, text_classification, glue*]
-   Sentiment analysis: [*sentiment, sentiment_analysis, sentiment-analysis*]
-   NLP token classification: [*token-classification, token_classification*]
-   Named entity recognition: [*ner, named-entity-recognition, named_entity_recognition*]
    
   **Datasets**
You can also select a supported public dataset (--dataset) that they want their pre-packaged model trained on, including:
- TBD

### Model Optimization Metrics:
You can select optimization metrics that the selected model is optimized on. We will always return an optimized model. A dense baseline is not a possible option for the model returned, even if slightly more accurate, since we want to return the most balanced performant and accurate model for whichever optimization metric you select for your task. 
    

-   The Optimizing metric (--optimizing-metric) is the metric to optimize above everything else and has the following options:
	- Accuracy Style metrics: *accuracy (default), f1, recall, map*
	- Performance Style metrics: *latency (default), throughput* 
	- Model Size metrics: *file_size, memory_usage* 

Multiple optimization metrics can be passed in as a comma separated value. In this event, Sparsify Package will return a model that meets a balance between the designated optimization metrics. 

### Outputs:
The output of a Sparsify Package API call is a deployment folder, dockerfile, and documentation at the root of current directory. Final performance numbers are displayed in the STD output. 

### Sparsify Package Examples:
**CV** 
To get a model that was trained for object detection and that is optimized for latency, you can call the Sparsify Package API as follows:
```bash
- sparsify.package --task['object detection'] --optimizing-metric['latency']
```
**NLP** 
To get a model that was trained for question answering on the SQuAD Dataset and that is optimized for model size, you can call the Sparsify Package API as follows:
```bash
- sparsify.package --task['qa'] --dataset=['SQuAD'] --optimizing-metric['file_size']
```

## Sparsify Auto Usage and Parameters 

### Training Information: 
Sparsify Auto will kick off the creation of an initial model based on the optimizing and satisficing metrics on the your datasets and then will begin automatic hyperparameter tuning to optimize the given metric to its highest value.  

The Sparsify Auto Sparse Transfer Learning process will run locally on your training hardware and automatically adjust training commands to fit the available training hardware (adjusting gradient accumulation for that setup).  You are able to override the model selection, teacher and model creation, and hyperparameter tuning processes by providing their own configurations via a config file, if you wish. 

You also have the ability to control aspects of the model training like the number of trials (--num-trials) that auto will run through for hyperparameter tuning. 

To learn about the full available list of training parameters, use 
```bash
sparsify.auto -h
```

### Task/Dataset Selection:
To use the Sparsify Auto API, you must choose a task and supply a dataset that you wish to get sparse transfer learn onto to create a deployable, packaged sparse model. You are required to designate a task and provide a dataset. 
    
   **Tasks**
   You can select from the following lists of supported list of tasks (--task) to create a performant model for: 
-   CV classification: [*ic, image-classification, image_classification, classification*]
-   CV detection: [*od, object-detection, object_detection, detection*]
-   CV segmentation: [*segmentation*]
-   NLP question answering: [*qa, question-answering, question_answering*]
-   NLP text classification: [*text-classification, text_classification, glue*]
-   Sentiment analysis: [*sentiment, sentiment_analysis, sentiment-analysis*]
-   NLP token classification: [*token-classification, token_classification*]
-   Named entity recognition: [*ner, named-entity-recognition, named_entity_recognition*]
    
   **Datasets**
   You must provide a path to a dataset that you wish to transfer learn a model onto for your designated task.  The dataset must conform to standard documentation around dataset creation that is detailed [here] link to our dataset format docs. 
    

### Model Optimization Metrics:
You can select optimization metrics that the selected model is optimized on. We will always return an optimized model. A dense baseline is not a possible option for the model returned, even if slightly more accurate, since we want to return the most balanced performant and accurate model for whichever optimization metric you select for your task. 
    

-   The Optimizing metric (--optimizing-metric) is the metric to optimize above everything else and has the following options:
	- Accuracy Style metrics: *accuracy (default), f1, recall, map*
	- Performance Style metrics: *latency (default), throughput* 
	- Model Size metrics: *file_size, memory_usage* 

Multiple optimization metrics can be passed in as a comma separated value. In this event, Sparsify Package will return a model that meets a balance between the designated optimization metrics. 

### Outputs:
The outputs of a Sparsify Auto API call are stored in a working directory, with each sub folder equivalent to a configuration file run. 

All progress is tracked through TensorBoard logs and is reported in the high-level command to reflect on overall auto progress as well as individual stage progress.
    
The final output is a deployment folder and docker file with instructions for deployment and orchestration integrations.


### Hyperparameter Tuning and Config File Requirements 
*Advanced Usage* 

The Sparsify Auto API is mainly used to create a sparse model for your dataset from scratch. However, for advanced users, you can also create your own config files and run hyperparameter tuning for your model. 

A custom config file can be easily created from weights or taken from a SparseZoo stub to target hyperparameters and then be able to be fed in for tuning for a supplied model. 
  
To learn about the usage of a config file to use Sparsify Auto for hyperparameter tuning, see our tutorial [here] TBD. 



### Sparsify Auto Examples: TBD
**CV** 
To get a model that was trained for object detection, is optimized for latency and transfer learn it to your dataset, you can call the Sparsify Auto  API as follows:
```bash
- sparsify.auto --task['object detection'] --optimizing-metric['latency'] 
```
**NLP** 
To get a model that was trained for question answering, is optimized for model size, and transfer learn it to your dataset,  you can call the Sparsify Auto API as follows:
```bash
- sparsify.package --task['qa'] --dataset=['SQuAD'] --optimizing-metric['file_size']


## Highlights

- [User Guide](https://docs.neuralmagic.com/sparsify/source/userguide/01-intro.html)

## Tutorials

Coming soon!

## Installation

This repository is tested on Python 3.7-3.9, Linux/Debian systems, and Chrome 87+.
It is recommended to install in a [virtual environment](https://docs.python.org/3/library/venv.html) to keep your system in order.

Install with pip using:

```bash
pip install sparsify
```

Depending on your flow, PyTorch, Keras, or TensorFlow must be installed in the local environment along with Sparsify. 


## Resources

### Learning More

- Documentation: [SparseML,](https://docs.neuralmagic.com/sparseml/) [SparseZoo,](https://docs.neuralmagic.com/sparsezoo/) [Sparsify,](https://docs.neuralmagic.com/sparsify/) [DeepSparse](https://docs.neuralmagic.com/deepsparse/)
- Neural Magic: [Blog,](https://www.neuralmagic.com/blog/) [Resources](https://www.neuralmagic.com/resources/)

### Release History

Official builds are hosted on PyPI

- stable: [sparsify](https://pypi.org/project/sparsify/)
- nightly (dev): [sparsify-nightly](https://pypi.org/project/sparsify-nightly/)

Additionally, more information can be found via [GitHub Releases.](https://github.com/neuralmagic/sparsify/releases)

### License

The project is licensed under the [Apache License Version 2.0](https://github.com/neuralmagic/sparsify/blob/main/LICENSE).

## Community

### Contribute

We appreciate contributions to the code, examples, integrations, and documentation as well as bug reports and feature requests! [Learn how here.](https://github.com/neuralmagic/sparsify/blob/main/CONTRIBUTING.md)

### Join

For user help or questions about Sparsify, sign up or log in to our [**Deep Sparse Community Slack**](https://join.slack.com/t/discuss-neuralmagic/shared_invite/zt-q1a1cnvo-YBoICSIw3L1dmQpjBeDurQ). We are growing the community member by member and happy to see you there. Bugs, feature requests, or additional questions can also be posted to our [GitHub Issue Queue.](https://github.com/neuralmagic/sparsify/issues)

You can get the latest news, webinar and event invites, research papers, and other ML Performance tidbits by [subscribing](https://neuralmagic.com/subscribe/) to the Neural Magic community.

For more general questions about Neural Magic, please fill out this [form.](http://neuralmagic.com/contact/)

### Cite

Find this project useful in your research or other communications? Please consider citing:

```bibtex
@InProceedings{
    pmlr-v119-kurtz20a, 
    title = {Inducing and Exploiting Activation Sparsity for Fast Inference on Deep Neural Networks}, 
    author = {Kurtz, Mark and Kopinsky, Justin and Gelashvili, Rati and Matveev, Alexander and Carr, John and Goin, Michael and Leiserson, William and Moore, Sage and Nell, Bill and Shavit, Nir and Alistarh, Dan}, 
    booktitle = {Proceedings of the 37th International Conference on Machine Learning}, 
    pages = {5533--5543}, 
    year = {2020}, 
    editor = {Hal Daumé III and Aarti Singh}, 
    volume = {119}, 
    series = {Proceedings of Machine Learning Research}, 
    address = {Virtual}, 
    month = {13--18 Jul}, 
    publisher = {PMLR}, 
    pdf = {http://proceedings.mlr.press/v119/kurtz20a/kurtz20a.pdf},
    url = {http://proceedings.mlr.press/v119/kurtz20a.html}, 
    abstract = {Optimizing convolutional neural networks for fast inference has recently become an extremely active area of research. One of the go-to solutions in this context is weight pruning, which aims to reduce computational and memory footprint by removing large subsets of the connections in a neural network. Surprisingly, much less attention has been given to exploiting sparsity in the activation maps, which tend to be naturally sparse in many settings thanks to the structure of rectified linear (ReLU) activation functions. In this paper, we present an in-depth analysis of methods for maximizing the sparsity of the activations in a trained neural network, and show that, when coupled with an efficient sparse-input convolution algorithm, we can leverage this sparsity for significant performance gains. To induce highly sparse activation maps without accuracy loss, we introduce a new regularization technique, coupled with a new threshold-based sparsification method based on a parameterized activation function called Forced-Activation-Threshold Rectified Linear Unit (FATReLU). We examine the impact of our methods on popular image classification models, showing that most architectures can adapt to significantly sparser activation maps without any accuracy loss. Our second contribution is showing that these these compression gains can be translated into inference speedups: we provide a new algorithm to enable fast convolution operations over networks with sparse activations, and show that it can enable significant speedups for end-to-end inference on a range of popular models on the large-scale ImageNet image classification task on modern Intel CPUs, with little or no retraining cost.} 
}
```

```bibtex
@misc{
    singh2020woodfisher,
    title={WoodFisher: Efficient Second-Order Approximation for Neural Network Compression}, 
    author={Sidak Pal Singh and Dan Alistarh},
    year={2020},
    eprint={2004.14340},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```
