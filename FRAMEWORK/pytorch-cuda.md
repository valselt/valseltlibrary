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
    </br></br>For that, I will type <pre><code>conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia</code></pre> in the ananconda prompt and hit enter.</li>
    <li>Install <a href="https://developer.nvidia.com/cuda-toolkit-archive">CUDA</a> and choose the CUDA version that matched with the CUDA you choose when installing PyTorch. If you use the command above, Install <a href="https://developer.nvidia.com/cuda-12-4-1-download-archive">CUDA 12.4</a></br></br>Note : CUDA installation needed <a href ="https://visualstudio.microsoft.com/">Visual Studio</a> to work properly.</li>
    <li>Install <a href="https://developer.nvidia.com/rdp/cudnn-archive">cuDNN</a> and choose the cuDNN version that matched with the CUDA you installed. If you use CUDA 12.4, Install cuDNN v8.9.7</li>
    <li><strong>Remember to use <code>pytorch</code> kernel when you try to run the notebooks.</strong></li>
  </ol>