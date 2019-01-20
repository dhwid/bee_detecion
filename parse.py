import argparse


def parse(path_beginning, input_file_name):
    file = open(input_file_name, 'r')
    output_file = open("train.txt", 'w')
    input_files_data = file.readlines()
    for line in input_files_data:
        data = line.split()
        path = data[0].split("/")
        path = path_beginning + path[-1].replace("bmp", "jpg ")
        new_line = path
        for i in range(0, int(data[1])):
            new_line = new_line + str(data[4 * i + 2]) + "," + str(data[4 * i + 3]) + "," + str(int(data[4 * i + 2]) + int(data[4 * i + 4])) + "," + str(int(data[4 * i + 5]) + int(data[4 * i + 3])) + ",0 "
        output_file.write(new_line)
        output_file.write('\n')
    output_file.close()


if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, default="dataset/train/",
                    help="path to dataset")
parser.add_argument("--input_file", type=str, default="info.txt",
                    help="Name of txt input file.")
args = parser.parse_args()

parse(args.path, args.input_file)
