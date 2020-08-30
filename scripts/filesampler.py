from src.helper_functions import get_parser, samplefiles


def main():
    parser = get_parser()
    args = parser.parse_args()
    output_sampled_files = samplefiles(args.file_folder,
                                       args.output_folder,
                                       args.file_ext,
                                       args.how_many,
                                       args.set_seed,
                                       args.saveList)
    return output_sampled_files


if __name__ == '__main__':
    main()
