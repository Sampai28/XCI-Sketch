# Photo-ColorSketching: Extraction of Color from Images

This project aims to convert photographic pictures into colored sketches. 
 
We use the [Contour Drawing Dataset presented in the Photo-Sketching paper](http://www.cs.cmu.edu/~mengtial/proj/sketch/) and propose two ways to extract color information from the images and amalgamate it with the corresponding sketches: 
1. We formulate a process to transfer color onto the existing black and white sketches in the dataset to produce colored outline sketches. 
2. We propose another method to produce color-filled sketches by performing colorspace manipulation. We go a step further to use these sketches as the training dataset for a Generative Adversarial Network and develop a model which can generate colored sketches from unseen images.
