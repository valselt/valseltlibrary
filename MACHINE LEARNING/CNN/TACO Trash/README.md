<h1 align="center"> TACO Dataset 🖼️✨ </h1>
<p align="center"> This repository contains projects that utilize Convolutional Neural Networks (CNN) and Support Vector Machines (SVM) to classify images within the Trash Annotations in Context (TACO) dataset, focusing on waste management and object detection.</p>

<div align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
  <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/scikit%20learn-%23F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/pandas-%23150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/numpy-5aaacd?style=for-the-badge&logo=numpy&logoColor=5575cc">
  <img src="https://img.shields.io/badge/matplotlib-1f5379?style=for-the-badge&logoColor=5575cc">
</div>

<h2>Setup ⚙️</h2>
<ol>
  <li>Do all the steps for Setup given earlier in the <a href="https://github.com/valselt/valseltlibrary/blob/main/MACHINE%20LEARNING/CNN/README.md">README.md for CNN</a></li>
  <li>Open <a href="https://www.kaggle.com/settings#:~:text=THEME-,API,-Using%20Kaggle%27s%20beta">Kaggle -> Settings -> API</a> to Create New Token</li>
  <li>Save kaggle.json to <code>C:\Users\[your Username]\.kaggle</code>. If there is no such folder, create one.</li>
  
</ol>
</br>

<h2>Before you jump into CNN, its important to do these! 🤔</h2>
<ol>
  <li><strong>Import Dataset</strong> </br> Run <a href="https://github.com/valselt/valseltlibrary/blob/main/MACHINE%20LEARNING/CNN/TACO%20Trash/import-dataset-from-kaggle.ipynb">import-dataset-from-kaggle.ipynb</a> to download the dataset straight from kaggle to <code>dataset/</code> directory</li></br>
  <li><strong>Update "img_file" Path</strong> </br> Run <a href="https://github.com/valselt/valseltlibrary/blob/main/MACHINE%20LEARNING/CNN/TACO%20Trash/update-path-csv.ipynb">update-path-csv.ipynb</a> to update the "img_file" path inside meta_df.csv</li></br>
  <li><strong>Split Train and Test</strong> </br> Run <a href="https://github.com/valselt/valseltlibrary/blob/main/MACHINE%20LEARNING/CNN/TACO%20Trash/split-dataset.ipynb">split-dataset.ipynb</a> to splitting dataset to 80% train and 20% test</li></br>
  
</ol>
