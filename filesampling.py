import glob
import os
import random


def samplefiles(file_folder, file_ext, how_many, save=True):
    """Function to randomly sample file names with a specified extension from a specified folder.
    Random sampling is without replacement.

    Function args:

    file_folder:    string specifying the target folder (located in same directory as the .py script)

    file_ext:   string specifying the target file extension.
                String should contain only the file extension, without the '.' (correct: 'jpg'; incorrect: '.jpg').

    how_many:   integer specifying the number of file names to be sampled.
                Must be lower or equal to total number of files in target directory.

    save:   takes a boolean value as input.
            If TRUE, saves a .txt file containing a list of the sampled file names. Also returns list object.
            If FALSE, only returns the output list object with sampled file names is returned.
    """
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
            "Something went wrong. Please make sure all the names and values you enter are valid.")


def samplefiles_input():
    """Function to randomly sample file names with a specified extension from a specified folder.
    Random sampling is without replacement.

    Function args:

    file_folder:    string specifying the target folder (located in same directory as the .py script)

    file_ext:   string specifying the target file extension.
                String should contain only the file extension, without the '.' (correct: 'jpg'; incorrect: '.jpg').

    how_many:   integer specifying the number of file names to be sampled.
                Must be lower or equal to total number of files in target directory.

    save:   takes a boolean value as input.
            If TRUE, saves a .txt file containing a list of the sampled file names. Also returns list object.
            If FALSE, only returns the output list object with sampled file names is returned.
    """
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

        save_user_input = str(input(""
                                    "Save a file with a list of sampled file names?\nYes: press 'y'\nNo: press 'n'"))

        if save_user_input in ['y', 'Y']:
            save = True
        elif save_user_input in ['n', 'N']:
            save = False

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
            "Something went wrong. Please make sure all the names and values you enter are valid.")
