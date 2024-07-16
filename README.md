## Random File Sampler

I wrote this program with the goal of automating the random sampling of images from databases. This is useful to anyone looking to  prevent any bias in file selection. 

This program randomly samples (without replacement) files of any given extension from a folder. The sampled files are then copied to a new folder together with a .txt file listing the sampled file names.

For reproducibility, the program uses a fixed pseudo-random generator seed number (seed=1234). Alternatively, you can set your own custom seed number.

### How to install Random File Sampler

#### Windows

Download the application installer in "Releases" section. Then, simply install the application as you normally do in Windows.

#### Mac OS

Clone/download repo. 
Run "filesampler_app.py" in your Python environment.
