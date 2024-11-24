<h3>
    <div style="display: flex; align-items: center;">
      <span>Install PyTorch with CUDA-Enabled</span>
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
        <li>Name the environment <code>pytorch</code> or whatever you want to name it.</li>
      </ul>
    </li>
    <li><strong>Open Anaconda Prompt in your Computer</strong></li>
<li>Once you are inside of the Anaconda Prompt, type this : <pre><code>conda activate [env_name]</code></pre> and then hit enter. For This Example, I'll Use <pre><code>conda activate pytorch</code></pre> </li>
    <li>Once you are inside of the <code>(pytorch)</code>, open the <a href="https://pytorch.org/get-started/locally/">PyTorch Website</a> and select the one that you want to installed on the computer. </br></br>For Example, I want to use CUDA 12.4 and installed it through conda installer.
    For that, I will type <pre><code>conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia</code></pre> in the ananconda prompt and hit enter.</br></br></li>
    <li>CUDA installation needed Visual Studio to work properly. Install <a href ="https://visualstudio.microsoft.com/">Visual Studio Installer</a>, run it when it done downloading, and dont forget to checkmark <strong>Desktop development with C++ workload</strong> when you install Visual Studio</br></br></li>
    <li>Install <a href="https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html#:~:text=All%20Conda%20packages%20released%20under%20a%20specific%20CUDA%20version%20are%20labeled%20with%20that%20release%20version.%20To%20install%20a%20previous%20version%2C%20include%20that%20label%20in%20the%20install%20command%20such%20as%3A">CUDA</a> inside Conda and choose the CUDA version that matched with the CUDA you choose when installing PyTorch. If you use the command above, Install CUDA 12.4</br><pre><code>conda install cuda -c nvidia/label/cuda-12.4</code></pre></br></li>
      <li>Also, install <a href="https://developer.nvidia.com/rdp/cudnn-archive">cuDNN</a> that matched CUDA Version. For This, i'll install cuDNN v8.9.7</br><pre><code>conda install -c nvidia cudnn=8.9.7
</code></pre></br></li>
    <li><strong>Remember to use <code>pytorch</code> kernel when you try to run the notebooks.</strong></li>
  </ol>
