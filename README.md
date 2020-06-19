## Random File Sampler

I wrote this program with the goal of automating the random sampling of face images from databases, mostly to prevent bias in image selection. 

This program randomly samples files from a folder, based on a specified file extension (image extensions: 'png', 'jpg'; but also works for any other file types: 'csv', 'txt', etc.). The sampled files are copied to a new folder, together with a .txt file listing the file names of all the sampled files.

The sampling is without replacement.

Latest updates:

- Created Windows executable file to run program interactively via pop-up window.
- New function samplefiles_input() allows to run the program in the terminal

Coming soon:
- option to set seed
- output log file with sampling timestamp


Program written by:

Manuel Oliveira (manueljbo@gmail.com)
