<h1 align="center"> Convolutional Neural Networks 🖼️✨ </h1>
<p align="center"> This folder contains various projects demonstrating of the implementation of Convolutional Neural Networks (CNNs) for image classification tasks using popular datasets. </p>

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
  <li><strong><a href="https://github.com/valselt/valseltlibrary/tree/main/CNN">CNN - MNIST</a> ✏️🖼️</strong> - A project that implements CNN to classify handwritten digits from the MNIST dataset, showcasing the effectiveness of deep learning in image recognition.</li>
  <li><strong><a href="https://github.com/valselt/valseltlibrary/tree/main/CNN/TACO%20Trash">CNN - TACO</a> 🥡🗑️🖼️</strong> - Using CNN to identify and classify images in the Trash Annotations in Context (TACO) dataset, useful for object detection tasks.</li>
</ol>

<h2>Pre-Setup ⚙️</h2>

<ol>
  <li><strong>Make a <a href="https://huggingface.co/login">Hugging Face</a> Account</strong> </li>
  <li>Once you Sign Up or Login, make sure to verified your email.</li>
  <li>Create a Hugging Face <strong><a href="https://huggingface.co/settings/tokens">Tokens</a></strong>. Check all the requirement you need for the tokens. If you are new to this, check all of it.</li>
  <li>Save your personal token somewhere safe. </br><strong>IMPORTANT! YOU CANNOT RETRIEVE IT ONCE YOU LOST THE TOKEN AND YOU SHOULD MAKE A NEW TOKEN</strong></li>
  <li>Import your token whenever you're running </br><code>from huggingface_hub import login</br>
  login()</code></li>
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
  <li><strong>Open Anaconda Navigator</strong> - Launch the Anaconda Navigator application.</li>
  <li><strong>Create a New Environment</strong>
    <ul>
      <li>Click on the "Environments" tab on the left sidebar.</li>
      <li>Click "Create" at the bottom left.</li>
      <li>Name the environment <code>tensorflow</code> and choose Python version <code>3.10.x</code>.</li>
    </ul>
  </li>
  <li><strong>Import TensorFlow Configuration</strong> - Import the <code>py31.yaml</code> file into your new environment to set up the required packages and dependencies.</li>
  <li><strong>Remember to use <code>tensorflow</code> kernel when you try to run the notebooks.</strong></li>
</ol>

<h3>
  <div style="display: flex; align-items: center;">
    <span>Locally (via Anaconda + PyTorch)</span>
        <a href="https://www.anaconda.com/">
            <img src="https://skillicons.dev/icons?i=anaconda" alt="Anaconda" style="height: 24px; margin-left: 8px;">
        </a>
        <a href="https://www.tensorflow.org/install/pip">
            <img src="https://skillicons.dev/icons?i=pytorch" alt="PyTorch" style="height: 24px; margin-left: 8px;">
        </a>
  </div>
</h3>

<ol>
  <li><strong>Install Anaconda</strong> - Download Anaconda from <a href="https://www.anaconda.com/download">Anaconda Download</a> and install it on your system.</li>
  <li><strong>Open Anaconda Navigator</strong> - Launch the Anaconda Navigator application.</li>
  <li><strong>Create a New Environment</strong>
    <ul>
      <li>Click on the "Environments" tab on the left sidebar.</li>
      <li>Click "Create" at the bottom left.</li>
      <li>Name the environment <code>pytorch</code> .</li>
    </ul>
  </li>
  <li><strong>Open Anaconda Prompt in your Computer</strong></li>
  <li>Once you are inside of the Anaconda Prompt, type this : <pre><code>conda activate pytorch</code></pre> and then hit enter.</li>
  <li>Once you are inside of the <code>(pytorch)</code>, open the <a href="https://pytorch.org/get-started/locally/">PyTorch Website</a> and select the one that you want to installed on the computer. For Example, I want to use CUDA 12.4 and installed it through conda installer.</li>
  <li>For that, I will type <pre><code>conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia</code></pre> in the ananconda prompt and hit enter.</li>
  <li>After PyTorch were successfully installed, run this code <pre><code>conda install conda-forge::huggingface_hub</code></pre>
  <pre><code>conda install conda-forge::transformers
</code></pre><pre><code>conda install jupyter
</code></pre>to install Hugging Face Hub and Transformers as well as Jupyter Notebook to your environment.
  </li>
  <li><strong>Remember to use <code>pytorch</code> kernel when you try to run the notebooks.</strong></li>
</ol>

<h3>Google Colab ☁️</h3>
<span>All of the requirements needed for this notebook are already installed inside Google Colab by Default (TensorFlow and Hugging Face). In order to speed up your process, change Google Colab runtime from <code>CPU</code> to <code>GPU</code> or <code>TPU</code>. For the tutorial on how to change the runtime click <a href="https://www.geeksforgeeks.org/how-to-use-google-colab/#:~:text=Change%20Runtime%20Environment%3A%20Click%20the%20%E2%80%9CRuntime%E2%80%9D%20dropdown%20menu.%20Select%20%E2%80%9CChange%20runtime%20type%E2%80%9D%20.%20Select%20python2%20or%203%20from%20the%20%E2%80%9CRuntime%20type%E2%80%9D%20dropdown%20menu.">here</a>

</br>
Note : If you want to use TPU, copy and run this code first <pre><code>!pip install tensorflow==2.11.0 protobuf==3.19.0
</code></pre>before you jump into another line.</span>
