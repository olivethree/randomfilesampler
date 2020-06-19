#! /usr/local/bin/python
from filesampling import *

def main():

    parser = get_parser()
    args = parser.parse_args()
    output_sampled_files = samplefiles(args.file_folder,
                                       args.file_ext,
                                       args.how_many,
                                       args.save)
    return output_sampled_files


if __name__ == '__main__':
    main()