<h1 align="center"> NLP With HuggingFace Transformers 🤖✨ </h1>
<p align="center"> This project contains various NLP pipelines using HuggingFace Transformers for different natural language processing tasks. </p>

<div align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
  <img src="https://img.shields.io/badge/Hugging%20Face-%23FFD21E?style=for-the-badge&logo=huggingface&logoColor=black
  ">
</div>

<h2>Content Overview 📚</h2>
<ol>
  <li><strong>Zero-Shot Classification 🎯</strong> - Classifies text into categories without the need for specific training data for those categories.</li>
  <li><strong>Text Generation ✍️</strong> - Generates coherent and relevant text based on a given prompt.</li>
  <li><strong>Fill-Mask 📝</strong> - Predicts missing words in a sentence, which is useful for text correction and completion.</li>
  <li><strong>Named Entity Recognition (NER) 🔍</strong> - Identifies and classifies entities in the text, such as names, organizations, and locations.</li>
  <li><strong>Question Answering ❓</strong> - Answers questions based on provided context, enabling information retrieval.</li>
  <li><strong>Sentiment Analysis ❤️</strong> - Analyzes text to determine the sentiment expressed, whether positive, negative, or neutral.</li>
  <li><strong>Summarization 📄</strong> - Creates a concise summary of longer texts while retaining key information.</li>
</ol>

<h2>Pre-Setup ⚙️</h2>

<ol>
  <li><strong>Make a <a href="https://huggingface.co/login">Hugging Face</a> Account</strong> </li>
  <li>Once you Sign Up or Login, make sure to verified your email.</li>
  <li>Create a Hugging Face <strong><a href="https://huggingface.co/settings/tokens">Tokens</a></strong>. Check all the requirement you need for the tokens. If you are new to this, check all of it.</li>
  <li>Save your personal token somewhere safe. </br><strong>IMPORTANT! YOU CANNOT RETRIEVE IT ONCE YOU LOST THE TOKEN AND YOU SHOULD MAKE A NEW TOKEN</strong><</li>
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
</ol>

<h3>Google Colab ☁️</h3>
<span>All of the requirements needed for this notebook are already installed inside Google Colab by Default (TensorFlow and Hugging Face). In order to speed up your process, change Google Colab runtime from <code>CPU</code> to <code>GPU</code> or <code>TPU</code>. For the tutorial on how to change the runtime click <a href="https://www.geeksforgeeks.org/how-to-use-google-colab/#:~:text=Change%20Runtime%20Environment%3A%20Click%20the%20%E2%80%9CRuntime%E2%80%9D%20dropdown%20menu.%20Select%20%E2%80%9CChange%20runtime%20type%E2%80%9D%20.%20Select%20python2%20or%203%20from%20the%20%E2%80%9CRuntime%20type%E2%80%9D%20dropdown%20menu.">here</a> </span>
