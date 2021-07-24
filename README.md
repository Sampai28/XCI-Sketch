# Photo-ColorSketching: Extraction of Color from Images

This project aims to convert photographic pictures into colored sketches. 
 
We use the [Contour Drawing Dataset presented in the Photo-Sketching paper](http://www.cs.cmu.edu/~mengtial/proj/sketch/) and propose two ways to extract color information from the images and amalgamate it with the corresponding sketches: 
- **Rendering Colored Outlines in Sketches**: 
  - We formulate a process to transfer color onto the existing black and white sketches in the dataset to produce colored outline sketches. 
  - We first select an optimal threshold value (TryingDifferentThresholdValues.ipynb) based on which we perform preprocessing and K-Means Color Clustering (GeneratingImagesBasedOnKVals.ipynb) on the images. 
  - Using the post-processing image and grayscale sketches we generate colored outlines (GeneratingOutlines.ipynb).
- **Generating Colored Sketches**: 
  - We propose another method to produce color-filled sketches by performing colorspace manipulation (data_preprocessing.ipynb). 
  - We go a step further to use these sketches as the training dataset for a Generative Adversarial Network and develop a model which can generate colored sketches from unseen images (Sketch_gan.ipynb).
  
View our results on [StreamLit app](https://share.streamlit.io/sampai28/generatedsketches/main)
Download the data [here](https://drive.google.com/drive/folders/11Eg4DZDWptyRdel3UH_5wsAMmGy0zzU2?usp=sharing)


