<h3>
  <div style="display: flex; align-items: center;">
    <span>Install Tensorflow with CUDA-Enabled (Without Using WSL2)</span>
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

</ol>