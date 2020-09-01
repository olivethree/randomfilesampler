## Random File Sampler

I wrote this program with the goal of automating the random sampling of face images from databases. This is useful to anyone looking to  prevent any bias in image file selection. 

This program randomly samples (without replacement) files of any given extension from a folder. The sampled files are then copied to a new folder together with a .txt file listing the sampled file names.

For reproducibility, the program uses a fixed pseudo-random generator seed number (seed=1234). Alternatively, you can set your own custom seed number.

### How to install Random File Sampler

#### Windows

Download the application installer in "Releases" section. Then, simply install the application as you normally do in Windows.

#### Mac OS

Unfortunately, the only way to run the app in Mac OS is via Python. Download the source code (see "Releases" section) and run "filesampler_app.py" in your Python environment.
Installer coming soon, as soon as I am able to compile it on a Mac machine.


### Lastest updates:
- Created installer for Random File Sampler GUI application (for Windows only).  

New features:
- Timestamp of sampling added to output list of sampled file names
- Reproducibility: Option to enter custom seed to make sampling process reproducible. Default seed set to 1234.
- Option to enter a name for the output folder
- Seed number information added to output list of sampled file names
- GUI
- Windows installer



Manuel Oliveira
(manueljbo@gmail.com)
