import os


def get_directory_info(directory_path):

    filenames = []
    dirnames = []


    if os.path.exists(directory_path) and os.path.isdir(directory_path):

        for entry in os.listdir(directory_path):
            entry_path = os.path.join(directory_path, entry)


            if os.path.isfile(entry_path):
                filenames.append(entry)


            elif os.path.isdir(entry_path):
                dirnames.append(entry)


    result_dict = {'filenames': filenames, 'dirnames': dirnames}
    return result_dict



directory_path = '/homeworks'
directory_info = get_directory_info(directory_path)
print(directory_info)
