<h1 align="center"> Support Vector Machine (SVM) Projects 📊✨ </h1>
<p align="center"> This folder showcases various projects that implement Support Vector Machine (SVM) algorithms for classification tasks on popular datasets. </p>

<div align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/scikit%20learn-%23F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/pandas-%23150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/numpy-5aaacd?style=for-the-badge&logo=numpy&logoColor=5575cc">
  <img src="https://img.shields.io/badge/matplotlib-1f5379?style=for-the-badge&logoColor=5575cc">
</div>

<h2>Content Overview 📚</h2>
<ol>
  <li><strong><a href="https://github.com/valselt/valseltlibrary/tree/main/MACHINE%20LEARNING/CNN">CNN - MNIST</a> ✏️🖼️</strong> - A project that implements CNN to classify handwritten digits from the MNIST dataset, showcasing the effectiveness of deep learning in image recognition.</li>
  <li><strong><a href="https://github.com/valselt/valseltlibrary/tree/main/MACHINE%20LEARNING/CNN">CNN - TACO</a> 🥡🗑️🖼️</strong> - Using CNN to identify and classify images in the Trash Annotations in Context (TACO) dataset, useful for object detection tasks.</li>
</ol>

<h2>Setup ⚙️</h2>

<h3>
  <div style="display: flex; align-items: center;">
    <span>Locally (via Anaconda + Tensorflow)</span>
        <a href="https://www.anaconda.com/">
            <img src="https://skillicons.dev/icons?i=anaconda" alt="Anaconda" style="height: 24px; margin-left: 8px;">
        </a>
        <a href="https://www.tensorflow.org/install/pip">
            <img src="https://skillicons.dev/icons?i=tensorflow" alt="Tensorflow" style="height: 24px; margin-left: 8px;">
        </a>
  </div>
</h3>

<ol>
  <li><strong>Install Anaconda</strong> - Download Anaconda from <a href="https://www.anaconda.com/download">Anaconda Download</a> and install it on your system.</li>
  <li><strong>(Option 1) Use the valselt's Anaconda Configuration</strong>
    <ul>
      <li>Launch the Anaconda Navigator application.</li>
      <li>Click on the "Environments" tab on the left sidebar.</li>
      <li>Before importing configuration, download the <code><a href = "https://github.com/valselt/valseltlibrary/blob/main/REQUIREMENTS/py39.yaml">py31.yaml</a></code> from REQUIREMENTS folder first.</li>
      <li>Click "Import" at the bottom left.</li>
      <li>Click "Import from Local Drive".</li>
      <li>Click on the folder icon, and choose <code>py31.yaml</code> you download earlier.</li>
      <li>Name the environment <code>tensorflow</code>.</li>
    </ul>
  </li>
  
  <li><strong>(Option 2) Build it yourself!</strong>
    <ul>
      <li><strong>Create a New Environment</strong>
      <li>Click on the "Environments" tab on the left sidebar.</li>
      <li>Click "Create" at the bottom left.</li>
      <li>Name the environment <code>tensorflow</code> and choose Python version <code>3.9.x</code>.</li>
      <li>Open Anaconda Prompt</li>
      <li>Type this on your Anaconda Prompt<pre><code>conda activate tensorflow</code></pre></li>
      <li>Open <a href = "https://www.tensorflow.org/install/pip#windows-native:~:text=Then%20install%20the%20CUDA%2C%20cuDNN%20with%20conda.">Tensorflow with pip</a> and follow the instruction inside those documentation. The code below is the same as stated inside the documentation :</li>
        <ul>
           <li><pre><code>conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0</pre></code></li>
           <li><pre><code>pip install "tensorflow<2.11"</pre></code></li>
        </ul>
    </ul>
  </li>
</ol>
</br>
<span>Remember to use <code>tensorflow</code> kernel when you try to run the notebooks.</span>

<h3>Google Colab ☁️</h3>
<span>All of the requirements needed for this notebook are already installed inside Google Colab by Default (TensorFlow). In order to speed up your process, change Google Colab runtime from <code>CPU</code> to <code>GPU</code> or <code>TPU</code>. For the tutorial on how to change the runtime click <a href="https://www.geeksforgeeks.org/how-to-use-google-colab/#:~:text=Change%20Runtime%20Environment%3A%20Click%20the%20%E2%80%9CRuntime%E2%80%9D%20dropdown%20menu.%20Select%20%E2%80%9CChange%20runtime%20type%E2%80%9D%20.%20Select%20python2%20or%203%20from%20the%20%E2%80%9CRuntime%20type%E2%80%9D%20dropdown%20menu.">here</a>
