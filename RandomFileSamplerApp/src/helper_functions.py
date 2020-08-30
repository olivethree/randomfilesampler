import argparse
import glob
import os
import random
import shutil
from datetime import datetime


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_folder', default=None, required=True, type=str,
                        help='String specifying the target folder.')
    parser.add_argument('--output_folder', default=None, required=True, type=str,
                        help='String specifying the output folder where the sampled files are copied to.')
    parser.add_argument('--file_ext', default=None, required=True, type=str,
                        help="""String specifying the target file extension.\n
                        String should contain only the file extension, 
                        without the '.' (correct: 'jpg'; incorrect: '.jpg').""")
    parser.add_argument('--how_many', default=None, required=True, type=int,
                        help="""Integer specifying the number of file names to be sampled.\n
                        Must be lower or equal to total number of files in target directory.""")
    parser.add_argument('--set_seed', default=1234, required=False, type=int,
                        help="""Integer specifying the pseudo-random number generator.
                        Allows reproducibility.\nDefault is set to '1234', but seed can be set to any number, not necessarily with four digits.""")
    parser.add_argument('--saveList', default=True, required=False, type=bool,
                        help="""Takes a boolean value as input.\n
                        If TRUE, saves a .txt file containing a list of the sampled file names. Also returns list object.\n
                        If FALSE, only returns the output list object with sampled file names is returned.""")
    return parser


def samplefiles(file_folder, output_folder, file_ext, how_many, set_seed=1234, saveList=True):
    """Function to randomly sample file with a specified extension from a specified folder
     and copy the sampled files to an output folder. Random sampling is without replacement.
     A list with the file names of the sampled files is saved in a .txt file by default"""
    try:

        if os.path.isdir(os.path.join(os.getcwd(), file_folder)) == False:
            print(
                "Warning:\nSpecified folder was not found in the current working directory. Please check for typos in your specified folder name")
            return None

        pathtofiles = file_folder + "/*." + str(file_ext)

        # Get list of file names in specified folder
        filelist = [os.path.basename(f) for f in glob.glob(pathtofiles, recursive=True)]

        total_files = len(filelist)

        if total_files == 0:
            print("No files with '{}' extension were found in the '{}' folder.".format(file_ext, file_folder))
            return None

        if how_many <= 0:
            print("Number of files must be higher than zero.")
            return None

        if how_many > total_files:
            print(
                "Number of files cannot be higher than the total number of {} files in the folder (total files = {})".format(
                    file_ext, total_files))
            return None

        # Set seed for random sampling
        random.seed(int(set_seed))

        # Randomly sample entries from file list without replacement
        sampled_files = random.sample(filelist, how_many)

        # Move randomly sampled files to output folder

        # Create sub-directory to store output files
        if output_folder == "":
            print("Output folder name cannot be an empty string. Using 'output' as output folder name.")
            output_folder_name ='output'
        else:
            output_folder_name = str(output_folder)

        outputpath = os.path.join(os.getcwd(), output_folder_name)

        if not os.path.isdir(outputpath):
            os.makedirs(outputpath)

        for f in sampled_files:
            shutil.copy(os.path.join(os.getcwd(), file_folder, f), outputpath)

        print("\nList of randomly sampled files copied to:\n",
              outputpath)

        if saveList == True:

            # Create sampled file names list and save it
            outputfilename = 'sampling_info.txt'

            # Add timestamp and save it together with sampled file names list
            samplingtimestamp = datetime.now()
            samplingtimestamp_str = samplingtimestamp.strftime("%d/%b/%Y (%H:%M:%S)")
            finaltimestamp = 'Timestamp: ' + samplingtimestamp_str

            # Add seed number info
            seed_info = 'Seed number used: ' + str(set_seed)

            # Merge all sampling information in a list
            sampling_log = [finaltimestamp, seed_info, sampled_files]

            # Save list
            with open(os.path.join(outputpath, outputfilename), 'w') as output:
                output.write(str(sampling_log))

            print("\nList of randomly sampled file names and sampling timestamp saved to:\n",
                  os.path.join(outputpath, outputfilename))

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
            "Something went wrong. Please make sure all the names and values you enter are valid.")


def samplefiles_input():
    """Randomly samples files with a specified extension from a specified folder
     and copies the sampled files to an output folder.
     Function parameters are requested via the terminal interactively. Random sampling is without replacement.
     A list with the file names of the sampled files is saved in a .txt file by default"""
    try:

        file_folder = str(input(
            "Please enter name of the folder you want to sample files from (must be in same directory as this script): "))

        if os.path.isdir(os.path.join(os.getcwd(), file_folder)) == False:
            print("Specified folder was not found in the current working directory. Try again with valid folder name.")
            return None

        file_ext = str(input(
            "Please enter the extension of the files you want to sample (without the '.'): "
        ))

        pathtofiles = file_folder + "/*." + str(file_ext)

        # Get list of file names in specified folder
        filelist = [os.path.basename(f) for f in glob.glob(pathtofiles, recursive=True)]

        total_files = len(filelist)

        if total_files == 0:
            print("No files with '{}' extension were found in the '{}' folder.".format(file_ext, file_folder))
            return None

        how_many = int(input(
            "Please enter the number of files you want to sample: "
        ))

        if how_many <= 0:
            how_many = int(input(
                "Number must be higher than zero.\nPlease re-enter the number of files you want to sample: "
            ))

        if how_many > total_files:
            how_many = int(input(
                "Number of files cannot be higher than the total number of {} files in the folder (total files = {}).\nPlease re-enter the number of files you want to sample: ".format(
                    file_ext, total_files)
            ))

        save_user_input = str(input(
            "Save a file with a list of sampled file names?\nYes: press 'y'\nNo: press 'n'\n"))

        if save_user_input in ['y', 'Y']:
            saveList = True
        elif save_user_input in ['n', 'N']:
            saveList = False

        # Set seed for random sampling
        seed_input = str(input(
            "Set your own seed number for the random sampling? If No, seed = 1234 will be used by default.\nYes: press 'y'\nNo: press 'n'\n"
        ))

        if seed_input in ['y', 'Y']:
            set_seed = input(
                "Please enter your custom seed number: "
            )
        elif seed_input in ['n', 'N']:
            set_seed = 1234

        # Set seed
        random.seed(int(set_seed))

        # Randomly sample entries from file list without replacement
        sampled_files = random.sample(filelist, how_many)

        # Move randomly sampled files to output folder

        # Create sub-directory to store output files
        output_folder = str(input(
            "Please enter a name for the output folder where the sampled files will be copied to:"
        ))

        if output_folder == "":
            print("Output folder name cannot be an empty string. Using 'output' as output folder name.")
            output_folder_name = 'output'

        else:
            output_folder_name = str(output_folder)

        outputpath = os.path.join(os.getcwd(), output_folder_name)

        if not os.path.isdir(outputpath):
            os.makedirs(outputpath)

        for f in sampled_files:
            shutil.copy(os.path.join(os.getcwd(), file_folder, f), outputpath)

        print("\nList of randomly sampled files copied to:\n",
              outputpath)

        if saveList == True:

            # Create sampled file names list and save it
            outputfilename = 'sampling_info.txt'

            # Add timestamp and save it together with sampled file names list
            samplingtimestamp = datetime.now()
            samplingtimestamp_str = samplingtimestamp.strftime("%d/%b/%Y (%H:%M:%S)")
            finaltimestamp = 'Timestamp: ' + samplingtimestamp_str

            # Add seed number info
            seed_info = 'Seed number used: ' + str(set_seed)

            # Merge all sampling information in a list
            sampling_log = [finaltimestamp, seed_info, sampled_files]

            # Save list
            with open(os.path.join(outputpath, outputfilename), 'w') as output:
                output.write(str(sampling_log))

            print("\nList of randomly sampled file names and sampling timestamp saved to:\n",
                  os.path.join(outputpath, outputfilename))

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
            "Something went wrong. Please make sure all the names and values you enter are valid.")
