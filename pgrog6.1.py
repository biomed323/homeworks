import os


def sort_directory_info(directory_info, ascending=True):

    directory_info['filenames'] = sorted(directory_info['filenames'], reverse=not ascending)
    directory_info['dirnames'] = sorted(directory_info['dirnames'], reverse=not ascending)

    return directory_info

directory_path = '/homeworks'
original_directory_info = get_directory_info(directory_path)

sorted_directory_info = sort_directory_info(original_directory_info)
print(sorted_directory_info)

reverse_sorted_directory_info = sort_directory_info(original_directory_info, ascending=False)
print(reverse_sorted_directory_info)
