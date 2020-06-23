## Random File Sampler

I wrote this program with the goal of automating the random sampling of face images from databases. This is useful to anyone looking to  prevent any bias in image file selection. 

This program randomly samples (without replacement) files of any given extension from a folder. The sampled files are then copied to a new folder together with a .txt file listing the sampled file names.

For reproducibility, the program uses a fixed pseudo-random generator seed number (seed=1234). Alternatively, you can set your own custom seed number.

Lastest news:
- Created a user-friendly application to use the program, to make it accessible to a wider audience. 
- To run the application download the "dist" folder and run "filesampler_app.exe"

New features:
- Timestamp of sampling added to output list of sampled file names
- Reproducibility: Option to enter custom seed to make sampling process reproducible. Default seed set to 1234.
- Option to enter a name for the output folder
- Seed number information added to output list of sampled file names
- GUI


Program written by:

Manuel Oliveira (manueljbo@gmail.com)
