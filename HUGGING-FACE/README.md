<h1 align="center"> NLP With HuggingFace Transformers 🤖✨ </h1>
<p align="center"> This project contains various NLP pipelines using HuggingFace Transformers for different natural language processing tasks. </p>

<div align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
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
  <li><strong>Import TensorFlow Configuration</strong> - Import the <code>tensorflow.yaml</code> file into your new environment to set up the required packages and dependencies.</li>
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
  <li>Type <code>conda activate pytorch</code> and then hit enter.</li>
  <li>Once you are inside of the <code>(pytorch)</code>, open the <a href="https://pytorch.org/get-started/locally/">PyTorch Website</a> and select the one that you want to installed on the computer. For Example, I want to use CUDA 12.4 and installed it through conda installer.</li>
  <li>For that, I will type <code>conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia</code> in the ananconda prompt and hit enter.</li>
</ol>

<h3>Google Colab ☁️</h3>
<ol>
  <li><strong>Install Transformers Library</strong>
    <pre><code>!pip install transformers</code></pre>
    <p>This command installs the HuggingFace Transformers library, allowing you to utilize its powerful features for natural language processing tasks.</p>
  </li>
</ol>

<h2>Analysis</h2>
    <span>All of the analysis i made are inside of the <a href = "https://github.com/valselt/NLP_HuggingFace_Transformers/blob/main/NLP_HuggingFace_Transformers_Muhammad%20Ivan%20Aldorino.ipynb"><code>NLP_HuggingFace_Transformers_Muhammad Ivan Aldorino.ipynb</code></a>. Go Check it Out!</span>