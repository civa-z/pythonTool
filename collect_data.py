
import os,sys

def read_data(file_name):
    data_buf = []
    with open(file_name) as f:
        for line in f.readlines():
            if -1 == line.find("IND"):
                data_buf.append(line)
    return data_buf

if __name__ == "__main__":
    arg_size = len(sys.argv)
    if arg_size < 3:
        print "Parameter error"
        exit()
    data_buf = []
    name_out_file = sys.argv[arg_size - 1]
    for i in range(1, arg_size - 1):
        data_buf = data_buf + read_data(sys.argv[i])

    if os.path.exists(name_out_file):
        print "Delete output file first"
        exit()
    with open(name_out_file, "w") as f:
        f.writelines(data_buf)




