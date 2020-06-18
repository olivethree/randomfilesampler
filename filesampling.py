import glob
import os
import random


def samplefiles(file_folder, file_ext, how_many, save=True):
    try:

        pathtofiles = file_folder + "/*." + str(file_ext)

        # Get list of file names in specified folder
        filelist = [os.path.basename(f) for f in glob.glob(pathtofiles, recursive=True)]

        # Randomly sample entries from file list without replacement
        sampled_files = random.sample(filelist, int(how_many))

        if save == True:

            outputfilename = 'sampled_files_list.txt'

            with open(os.path.join(os.getcwd(), outputfilename), 'w') as output:
                output.write(str(sampled_files))

            print("\nList of randomly sampled file names saved to:\n",
                  os.path.join(os.getcwd(), outputfilename))

            print("\nThe following files were sampled:\n",
                  sampled_files)

            print("\nWritten by Manuel Oliveira (manueljbo@gmail.com)")

            return sampled_files

        else:

            print("\nThe following files were sampled:\n",
                  sampled_files)

            print("\nWritten by Manuel Oliveira (manueljbo@gmail.com)")

            return sampled_files

    except:

        print(
            "Something went wrong.\nPotential causes:\nany typos in specified folder name\nfile extension does not include '.' (example: insert 'csv' for .csv file extension, not '.csv' which will result in an error\n'how_many' takes integers as input")
