<h1 align="center"> NLP With HuggingFace Transformers 🤖✨ </h1>
<p align="center"> This folder contains various NLP pipelines using HuggingFace Transformers for different natural language processing tasks. </p>

<div align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
  <img src="https://img.shields.io/badge/Hugging%20Face-%23FFD21E?style=for-the-badge&logo=huggingface&logoColor=black">
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/pytorch-%23EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
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
  <li><strong>(Option 1) Use the valselt's Anaconda Configuration</strong>
    <ul>
      <li>Launch the Anaconda Navigator application.</li>
      <li>Click on the "Environments" tab on the left sidebar.</li>
      <li>Before importing configuration, download the <code><a href = "https://github.com/valselt/valseltlibrary/blob/main/REQUIREMENTS/py39-tensorflow.yaml">py39-tensorflow.yaml</a></code> from REQUIREMENTS folder first.</li>
      <li>Click "Import" at the bottom left.</li>
      <li>Click "Import from Local Drive".</li>
      <li>Click on the folder icon, and choose <code>py39-tensorflow.yaml</code> you download earlier.</li>
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
        <li>Install other dependencies used in this project :</li>
        <ul>
          <li>
            <a href="https://github.com/tensorflow/tensorflow/issues/60216#:~:text=Numpy%20was%20pinned%20to%20%3C1.24%20since%20it%20affected%20few%20tests%20on%20Ragged%20Tensors.%20Agree%20that%20we%20should%20fix%20those%20tests%20and%20remove%20the%20upperbound%20in%20future%20releases.">NumPy</a></br>
            <pre><code>conda install numpy=1.24</pre></code>
          </li>
          <li>
            <a href="https://matplotlib.org/devdocs/devel/min_dep_policy.html#:~:text=of%20the%20dependencies.-,Matplotlib,1.23.0,-3.8">Matplotlib</a></br>
            <pre><code>conda install matplotlib=3.9</pre></code>
          </li>
          <li>
            <a href="https://pandas.pydata.org/pandas-docs/version/2.1.3/getting_started/install.html#:~:text=Required%20dependencies">Pandas</a></br>
            <pre><code>conda install pandas</pre></code>
          </li>
          <li>
            <a href="https://ipython.readthedocs.io/en/8.27.0/install/kernel_install.html#:~:text=different%20virtualenvs%20or-,conda%20environments,-%2C%20you%20will%20need">IPython Kernel</a></br>
            <pre><code>conda install ipykernel</pre></code>
          </li>
          <li>
            OpenCV</br>
            <pre><code>conda install -c conda-forge opencv</pre></code>
          </li>
          <li>
            <a href = "https://huggingface.co/docs/huggingface_hub/installation#:~:text=./huggingface_hub/.-,Install%20with%20conda,-If%20you%20are">Hugging Face Hub</a></br>
            <pre><code>conda install -c conda-forge opencv</pre></code>
          </li>
        </ul>
    </ul>
  </li>
</ol>
</br>
<span>Remember to use <code>tensorflow</code> kernel when you try to run the notebooks.</span>

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
  <li>Install other dependencies used in this project :</li>
        <ul>
          <li>
            <a href="https://github.com/tensorflow/tensorflow/issues/60216#:~:text=Numpy%20was%20pinned%20to%20%3C1.24%20since%20it%20affected%20few%20tests%20on%20Ragged%20Tensors.%20Agree%20that%20we%20should%20fix%20those%20tests%20and%20remove%20the%20upperbound%20in%20future%20releases.">NumPy</a></br>
            <pre><code>conda install numpy=1.24</pre></code>
          </li>
          <li>
            <a href="https://matplotlib.org/devdocs/devel/min_dep_policy.html#:~:text=of%20the%20dependencies.-,Matplotlib,1.23.0,-3.8">Matplotlib</a></br>
            <pre><code>conda install matplotlib=3.9</pre></code>
          </li>
          <li>
            <a href="https://pandas.pydata.org/pandas-docs/version/2.1.3/getting_started/install.html#:~:text=Required%20dependencies">Pandas</a></br>
            <pre><code>conda install pandas</pre></code>
          </li>
          <li>
            <a href="https://ipython.readthedocs.io/en/8.27.0/install/kernel_install.html#:~:text=different%20virtualenvs%20or-,conda%20environments,-%2C%20you%20will%20need">IPython Kernel</a></br>
            <pre><code>conda install ipykernel</pre></code>
          </li>
          <li>
            OpenCV</br>
            <pre><code>conda install -c conda-forge opencv</pre></code>
          </li>
          <li>
            <a href = "https://huggingface.co/docs/huggingface_hub/installation#:~:text=./huggingface_hub/.-,Install%20with%20conda,-If%20you%20are">Hugging Face Hub</a></br>
            <pre><code>conda install conda-forge::huggingface_hub</pre></code>
          </li>
        </ul>
  <li><strong>Remember to use <code>pytorch</code> kernel when you try to run the notebooks.</strong></li>
</ol>

<h3>Google Colab ☁️</h3>
<span>All of the requirements needed for this notebook are already installed inside Google Colab by Default (TensorFlow and Hugging Face). In order to speed up your process, change Google Colab runtime from <code>CPU</code> to <code>GPU</code> or <code>TPU</code>. For the tutorial on how to change the runtime click <a href="https://www.geeksforgeeks.org/how-to-use-google-colab/#:~:text=Change%20Runtime%20Environment%3A%20Click%20the%20%E2%80%9CRuntime%E2%80%9D%20dropdown%20menu.%20Select%20%E2%80%9CChange%20runtime%20type%E2%80%9D%20.%20Select%20python2%20or%203%20from%20the%20%E2%80%9CRuntime%20type%E2%80%9D%20dropdown%20menu.">here</a>

</br>
Note : If you want to use TPU, copy and run this code first <pre><code>!pip install tensorflow==2.11.0 protobuf==3.19.0
</code></pre>before you jump into another line.</span>
