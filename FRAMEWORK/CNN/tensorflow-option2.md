<h3>
  <div style="display: flex; align-items: center;">
    <span>Built TensorFlow yourself</span>
        <a href="https://www.anaconda.com/">
            <img src="https://skillicons.dev/icons?i=anaconda" alt="Anaconda" style="height: 24px; margin-left: 8px;">
        </a>
        <a href="https://www.tensorflow.org/install/pip">
            <img src="https://skillicons.dev/icons?i=tensorflow" alt="Tensorflow" style="height: 24px; margin-left: 8px;">
        </a>
  </div>
</h3>

<ol>
    <li>Follow the instruction in this <a href="https://github.com/valselt/valseltlibrary/blob/main/FRAMEWORK/tensorflow-cuda.md">link</a></li>
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
            OpenCV</br>
            <pre><code>conda install -c conda-forge opencv</pre></code>
          </li>
          <li>
            <a href="https://ipython.readthedocs.io/en/8.27.0/install/kernel_install.html#:~:text=different%20virtualenvs%20or-,conda%20environments,-%2C%20you%20will%20need">IPython Kernel</a></br>
            <pre><code>conda install ipykernel</pre></code>
          </li>
          <li>
            Kaggle</br>
            <pre><code>conda install conda-forge::kaggle</pre></code>
          </li>
          <li>
            <a href="https://scikit-learn.org/stable/install.html">Scikit Learn</a></br>
            <pre><code>conda install scikit-learn</pre></code>
          </li>
        </ul>
</ol>