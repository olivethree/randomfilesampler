import glob
import os
import random
import shutil
import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# Initiate app window
window = tk.Tk()
# Configure app window
window.geometry("500x400")
window.title("Random File Sampler")


# Define class for folder selection object
class selectFolder(Frame):
    def __init__(self, parent=None, folderDescription="", **kw):
        Frame.__init__(self, master=parent, **kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0, column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0, column=1)
        self.btnFind = ttk.Button(self, text="Browse Folder", command=self.setFolderPath)
        self.btnFind.grid(row=0, column=2)

    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)

    @property
    def folder_path(self):
        return self.folderPath.get()


# File sampler function
def filesampler():
    file_folder = input_folder.folder_path
    file_ext = str(file_extEntry.get())

    how_many = how_manyEntry.get()
    if how_many.isdigit():
        how_many = int(how_many)
    else:
        messagebox.showwarning("Warning",
                               "Number of files to be sampled: Not a valid entry! Only number digits accepted as input.")

    set_seed = set_seedEntry.get()
    if not set_seed.isdigit():
        set_seed = 1234
    elif set_seed.isdigit():
        set_seed = int(set_seed)

    output_folder = str(output_folderEntry.get())

    pathtofiles = file_folder + "/*." + file_ext

    # Get list of file names in specified folder
    filelist = [os.path.basename(f) for f in glob.glob(pathtofiles, recursive=True)]

    total_files = len(filelist)

    if total_files == 0:
        messagebox.showwarning("Warning",
                               "No files with '{}' extension were found in the '{}' folder.".format(file_ext,
                                                                                                    file_folder))
        return None

    if how_many <= 0:
        messagebox.showwarning("Warning", "Number of files must be higher than zero.")
        return None

    if how_many > total_files:
        messagebox.showwarning("Warning",
                               "Number of files cannot be higher than the total number of {} files in the folder (total files = {})".format(
                                   file_ext, total_files))
        return None

    # Set seed for random sampling
    random.seed(set_seed)

    # Randomly sample entries from file list without replacement
    sampled_files = random.sample(filelist, how_many)

    # Move randomly sampled files to output folder

    # Create sub-directory to store output files
    if output_folder == "":
        messagebox.showwarning("Warning",
                               "Output folder name cannot be an empty string. Using 'output' as output folder name.")
        # print("Output folder name cannot be an empty string. Using 'output' as output folder name.")
        output_folder_name = 'output'
    else:
        output_folder_name = output_folder

    outputpath = os.path.join(file_folder, output_folder_name)

    if not os.path.isdir(outputpath):
        os.makedirs(outputpath)

    for f in sampled_files:
        shutil.copy(os.path.join(file_folder, f), outputpath)

    # Get info from save log check button
    savelog_option = savelogValue.get()

    if savelog_option == 1:
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

    # Finished message box
    messagebox.showinfo("Done",
                        f"Files sampling complete!\n\nList of randomly sampled files copied to:\n\n{outputpath}\n\n"
                        f"Application by Manuel Oliveira\n"
                        f"(manueljbo@gmail.com)")

    openpath = os.path.realpath(os.path.join(file_folder, output_folder_name))
    os.startfile(openpath)


# Define function to show Help info on menu
def showHelp():
    messagebox.showinfo("Help", """\n\n
    TUTORIAL\n\n
    Step 1 - Input folder:\n\n
    Select the folder containing the files you want to sample from, 
    by clicking the "Browse Folder" button in the first entry field.\n\n
    Step 2 - File extension:\n\n
    Insert the extension of the files you want to sample.
    The file extension must be entered without any '.' (correct: jpg; incorrect: .jpg)\n\n
    Step 3 - Sample size:\n\n
    Indicate how many files you want to randomly sample from the folder.\n
    You must enter a number higher than zero and lower than the total number of files (with the specified extension) in the input folder.\n\n
    Step 4 - Seed number:\n\n
    To allow for reproducibility, you can define your custom seed number, or leave the entry field blank to use the default seed number instead. 
    The default seed number = 1234. The seed number you decide to use will be saved to the sampling log file (if you activate the button in Step 5).\n\n
    Step 5 - Save sampling log file?:\n\n
    Check the box if you want to save a file including information about the sampling. This file includes:\n
    - timestamp informing about the date and time at which the sampling took place
    - seed number used
    - a list with all the names of the sampled files""")


# Define function to show App info on menu
def showAbout():
    messagebox.showinfo("Application Information", "\nRandom File Sampler\n\n"
                                                   "Version 0.1\n\n"
                                                   "Application written in Python 3.7 by:\n\n"
                                                   "Manuel J. Barbosa de Oliveira\n\n"
                                                   "Github: olivethree\n\n"
                                                   "Created on June 2020\n"
                                                   "Last update: 23/06/2020")


# Add menu and About information
menu_bar = Menu(window)

# Adding menus and commands

# Help menu
help_info = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_info)
help_info.add_command(label='How to use', command=showHelp)

# About menu
about_info = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_info)
about_info.add_command(label='App Info', command=showAbout)

# Get folder path input by user
folderPath = StringVar()
input_folder = selectFolder(window, "Select folder containing your files:")
input_folder.grid(rowspan=2, columnspan=4, pady=30, sticky=W + E)

# Define necessary variables and entries
Label(text="Files extension (without .):\n", justify=RIGHT).grid(row=3, column=0)
Label(text="Number of files to sample:\n", justify=RIGHT).grid(row=4, column=0)
Label(text="Custom seed number\n(leave blank for default seed):", justify=RIGHT).grid(row=5, column=0)
Label(text="Enter name for\noutput folder with sampled files:", justify=RIGHT).grid(row=6, column=0)

file_extValue = StringVar()
how_manyValue = StringVar()
set_seedValue = StringVar()
output_folderValue = StringVar()

file_extEntry = Entry(window, textvariable=file_extValue)
how_manyEntry = Entry(window, textvariable=how_manyValue)
set_seedEntry = Entry(window, textvariable=set_seedValue)
output_folderEntry = Entry(window, textvariable=output_folderValue)

file_extEntry.grid(row=3, column=1)
how_manyEntry.grid(row=4, column=1)
set_seedEntry.grid(row=5, column=1)
output_folderEntry.grid(row=6, column=1)

# Create option to save file with sampling info
savelogValue = IntVar()
savelogButton = Checkbutton(window, text='Save sampling info?', variable=savelogValue).grid(row=7, column=1,
                                                                                            columnspan=2)

# Create button to execute sampling process
executeButton = ttk.Button(window, text="Start random sampling", command=filesampler)
executeButton.grid(row=8, column=1, columnspan=2, sticky=W + E)

window.resizable(True, True)  # make app window resizeable
window.config(menu=menu_bar)  # display menu items
window.mainloop()
