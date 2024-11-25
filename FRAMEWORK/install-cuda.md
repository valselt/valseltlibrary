<h3>
    <div style="display: flex; align-items: center;">
      <span>Install CUDA inside Ananconda</span>
          <a href="https://www.anaconda.com/">
              <img src="https://skillicons.dev/icons?i=anaconda" alt="Anaconda" style="height: 24px; margin-left: 8px;">
          </a>
    </div>
  </h3>

<ol>
  <li>CUDA installation needed Visual Studio to work properly. Install <a href ="https://visualstudio.microsoft.com/">Visual Studio Installer</a>, run it when it done downloading, and dont forget to checkmark <strong>Desktop development with C++ workload</strong> when you install Visual Studio</br></br></li>
    <li>Install <a href="https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html#:~:text=All%20Conda%20packages%20released%20under%20a%20specific%20CUDA%20version%20are%20labeled%20with%20that%20release%20version.%20To%20install%20a%20previous%20version%2C%20include%20that%20label%20in%20the%20install%20command%20such%20as%3A">CUDA</a> inside Conda and choose the CUDA version that matched with the CUDA you choose when installing PyTorch. If you use the command above, Install CUDA 12.4</br><pre><code>conda install nvidia/label/cuda-12.4.0::cuda-toolkit</code></pre></br></li>
      <li>Also, install <a href="https://developer.nvidia.com/rdp/cudnn-archive">cuDNN</a> that matched CUDA Version. For This, i'll install cuDNN v8.9.7</br><pre><code>conda install -c nvidia cudnn=8.9.7
</code></pre></br></li>
</ol>
