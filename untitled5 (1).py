# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W4-y6gAMz1Evos14VJcN2AXdP2pz9Hk6
"""

# Kaggle API sozlash
!pip install -q kaggle

# Kaggle API token faylini yuklash
from google.colab import files
files.upload()  # kaggle.json faylini yuklang

# Kaggle API sozlamalarini o'rnatish
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Kaggle datasetini yuklash
!kaggle datasets download -d heptapod/titanic

# Datasetni zip dan chiqarish
!unzip -o titanic.zip

# CSV faylni o'qish va ko'rish
import pandas as pd
data = pd.read_csv('train_and_test2.csv')  # Fayl nomi to'g'irlandi
print(data.head())