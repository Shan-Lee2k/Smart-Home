import h5py

with h5py.File('face_recognition_model.h5', 'r') as file:
    # Define a function to print information about each object in the file
    def print_object_info(name, obj):
        print(name)
        print('-' * len(name))
        print(obj)
        print('\n')


    # Visit all objects in the file and call the print_object_info function
    file.visititems(print_object_info)
print("========================================================================")

