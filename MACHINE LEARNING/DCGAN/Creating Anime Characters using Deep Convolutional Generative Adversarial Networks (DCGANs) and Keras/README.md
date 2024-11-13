<h1 align="center">Creating anime characters using Deep Convolutional Generative Adversarial Networks (DCGANs) and Keras 🌌✨</h1>
<p align="center">This repository demonstrates the creation of anime-style characters using Deep Convolutional Generative Adversarial Networks (DCGANs) with Keras. It covers GAN fundamentals, data handling, model building, and training, focusing on generating unique, game-ready characters.</p>

<h2>Content Overview 📚</h2>
<ol>
  <li><strong>Objectives 🎯</strong> - Learn to generate anime-style characters using DCGANs, useful in applications like creating unique avatars in games.</li>
  <li><strong>Basic Generative Adversarial Networks (GANs) 🧩</strong> - Introduction to GANs, including a toy dataset example to demonstrate the generator model, GAN loss function, and training steps.</li>
  <li><strong>Deep Convolutional GANs (DCGANs) 🖼️</strong> - Detailed steps for implementing DCGANs on anime character images, including loading the dataset, setting up the data generator, and defining the generator and discriminator models.</li>
  <li><strong>Training DCGANs 🔄</strong> - Walkthrough of the training process for DCGANs, covering loss functions, optimizers, and training steps required to generate anime images.</li>
  <li><strong>Exploring Latent Variables 🔍</strong> - Exercises to experiment with latent variables and observe their effects on generated images, which can help refine character generation.</li>
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
      <li>Before importing configuration, download the <code><a href = "https://github.com/valselt/valseltlibrary/blob/main/REQUIREMENTS/dcgan-anime.yaml">dcgan-anime.yaml</a></code> from REQUIREMENTS folder first.</li>
      <li>Click "Import" at the bottom left.</li>
      <li>Click "Import from Local Drive".</li>
      <li>Click on the folder icon, and choose <code>dcgan-anime.yaml</code> you download earlier.</li>
      <li>Name the environment <code>dcgan-anime</code>.</li>
    </ul>
  </li>
  
  <li><strong>(Option 2) Build it yourself!</strong>
    <ul>
      <li><strong>Create a New Environment</strong>
      <li>Click on the "Environments" tab on the left sidebar.</li>
      <li>Click "Create" at the bottom left.</li>
      <li>Name the environment <code>dcgan-anime</code> and choose Python version <code>3.9.x</code>.</li>
      <li>Open Anaconda Prompt</li>
      <li>Type this on your Anaconda Prompt<pre><code>conda activate dcgan-anime</code></pre></li>
      <li>Install Tensorflow first :</li>
        <ul>
           <li><pre><code>pip install "tensorflow<2.11"</pre></code></li>
        </ul>
        <li>Install other dependencies used in this project :</li>
        <ul>
          <li>
            <a href="https://github.com/tensorflow/tensorflow/issues/60216#:~:text=Numpy%20was%20pinned%20to%20%3C1.24%20since%20it%20affected%20few%20tests%20on%20Ragged%20Tensors.%20Agree%20that%20we%20should%20fix%20those%20tests%20and%20remove%20the%20upperbound%20in%20future%20releases.">NumPy</a></br>
            <pre><code>conda install numpy==1.21.4</pre></code>
          </li>
          <li>
            <a href="https://matplotlib.org/devdocs/devel/min_dep_policy.html#:~:text=of%20the%20dependencies.-,Matplotlib,1.23.0,-3.8">Matplotlib</a></br>
            <pre><code>conda install matplotlib==3.5.0</pre></code>
          </li>
          <li>
            <a href="https://pandas.pydata.org/pandas-docs/version/2.1.3/getting_started/install.html#:~:text=Required%20dependencies">Pandas</a></br>
            <pre><code>conda install pandas==1.3.4</pre></code>
          </li>
          <li>
            Scikit Learn</br>
            <pre><code>conda install scikit-learn</pre></code>
          </li>
          <li>
            seaborn</br>
            <pre><code>conda install seaborn=0.9.0</pre></code>
          </li>
          <li>
            IPyKernel</br>
            <pre><code>conda install ipykernel</pre></code>
          </li>
          <li>
            Skills Network</br>
            <pre><code>pip install skillsnetwork</pre></code>
          </li>
        </ul>
        <li>
            The following required libraries are not pre-installed in the Skills Network Labs environment. You will need to run the following cell to install them:</br>
            <pre><code>pip install tqdm skillsnetwork</pre></code>
          </li>
    </ul>
  </li>
</ol>
</br>
<span>Remember to use <code>dcgan-anime</code> kernel when you try to run the notebooks.</span>

<h3>Google Colab ☁️</h3>
<span>All of the requirements needed for this notebook are already installed inside Google Colab by Default (TensorFlow and Hugging Face). In order to speed up your process, change Google Colab runtime from <code>CPU</code> to <code>GPU</code> or <code>TPU</code>. For the tutorial on how to change the runtime click <a href="https://www.geeksforgeeks.org/how-to-use-google-colab/#:~:text=Change%20Runtime%20Environment%3A%20Click%20the%20%E2%80%9CRuntime%E2%80%9D%20dropdown%20menu.%20Select%20%E2%80%9CChange%20runtime%20type%E2%80%9D%20.%20Select%20python2%20or%203%20from%20the%20%E2%80%9CRuntime%20type%E2%80%9D%20dropdown%20menu.">here</a>

</br>
Note : If you want to use TPU, copy and run this code first <pre><code>!pip install tensorflow==2.11.0 protobuf==3.19.0
</code></pre>before you jump into another line.</span>

<h2>Documentation 📝</h2>
<p>This project is organized as follows:</p>
<ol>
  <li><strong>Data Preparation</strong>: Pre-processes and prepares the anime character images for training.</li>
  <li><strong>GAN Model Fundamentals</strong>: Introduces the components of a GAN, including the generator and discriminator networks, and outlines the GAN training loop.</li>
  <li><strong>DCGAN Architecture</strong>: Details the architecture for Deep Convolutional GANs, enhancing traditional GANs with CNN layers to improve image generation quality.</li>
  <li><strong>Training Process</strong>: Implements the training loop using the Keras framework, including batch updates, loss tracking, and generated image sampling for feedback during training.</li>
  <li><strong>Latent Space Exploration</strong>: Experiment with different latent space vectors to control and refine the character styles and expressions generated by the model.</li>
</ol>

<h2>Technologies Used 🛠️</h2>
<p>This project employs several key tools and libraries:</p>
<ul>
  <li><strong>Python</strong>: Core programming language for implementing the DCGAN model and training pipeline.</li>
  <li><strong>Keras with TensorFlow Backend</strong>: Used to construct and train the DCGAN model, leveraging TensorFlow’s GPU capabilities for efficient deep learning.</li>
  <li><strong>NumPy</strong>: Fundamental for handling array operations and managing dataset transformations.</li>
  <li><strong>Matplotlib</strong>: Used for visualizing generated images at different training stages to track progress and outcomes.</li>
  <li><strong>Anaconda</strong>: Provides an isolated environment to manage dependencies and versions, ensuring reproducibility across different systems.</li>
  <li><strong>Google Colab (optional)</strong>: Offers free GPU resources to accelerate model training, ideal for users without local GPU access.</li>
</ul>

<h2>Analysis of Technology Choices 🧩</h2>
<ol>
  <li><strong>Keras with TensorFlow</strong>: The choice of Keras for model building simplifies DCGAN architecture development, and TensorFlow enables optimized computations, particularly on GPUs.</li>
  <li><strong>DCGANs</strong>: This GAN variant leverages convolutional layers to enhance the generation of high-quality images, making it ideal for visual tasks like anime character creation.</li>
  <li><strong>NumPy and Matplotlib</strong>: These libraries facilitate data handling and visualization, which are essential for pre-processing datasets and monitoring the GAN’s training progress.</li>
  <li><strong>Anaconda and Google Colab</strong>: The use of Anaconda ensures a consistent environment, while Google Colab’s GPU support allows for faster experimentation without requiring a high-end local machine, making it accessible for educational purposes.</li>
</ol>

<h2>Conclusion 📈</h2>
<p>This project successfully demonstrates how Deep Convolutional Generative Adversarial Networks (DCGANs) can be used to generate high-quality, unique anime characters. By leveraging the convolutional network capabilities within GAN architecture, the model is able to learn the visual patterns and styles of the anime character dataset, producing images that are realistic and consistent with anime aesthetics.</p>

<p>Key takeaways from this project include:</p>
<ol>
  <li><strong>Effectiveness of DCGANs in Image Generation:</strong> DCGAN proved to be a powerful method for generating high-resolution, realistic images, especially in this project where the focus was on the anime visual style.</li>
  <li><strong>In-Depth Understanding of Latent Space:</strong> Exploring the model’s latent space provided insights into how different vector values affect generated images, allowing for adjustments to the style and features of the generated characters.</li>
  <li><strong>Flexibility and Scalability:</strong> By using Keras and TensorFlow, this project enabled both local development and easy migration to Google Colab for GPU access.</li>
  <li><strong>Opportunities for Further Development:</strong> This project opens up pathways for further exploration, such as implementing more advanced GAN architectures (e.g., StyleGAN) or experimenting with different model parameters to generate other visual styles.</li>
</ol>