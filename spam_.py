<<<<<<< HEAD
#!/usr/bin/env python3
=======
#! python3
>>>>>>> cc1e0fc1916cb6d3f59dbde70a61c61d2614d12e

import os
import shutil


# Loop over the files in the current working dir
for file_name in os.listdir():

    # Exclude the files not ending with .txt extension
    if not file_name.endswith('.txt'):
        continue
    else:
        new_file_name = 'spam_' + file_name

        # Get the full absolute file paths
        absolute_path = os.path.abspath('.')
        new_file_name = os.path.join(absolute_path, new_file_name)
        file_name = os.path.join(absolute_path, file_name)

        # Rename the files.
<<<<<<< HEAD
        print('Renaming %s to %s ....' % (file_name, new_file_name))
        shutil.move(file_name, new_file_name)
=======
        print('Renaming %s to %s ....'  %(file_name, new_file_name))
        shutil.move(file_name, new_file_name)

>>>>>>> cc1e0fc1916cb6d3f59dbde70a61c61d2614d12e