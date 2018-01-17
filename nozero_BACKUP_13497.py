<<<<<<< HEAD
#!/usr/bin/env python3
=======
#! python3
>>>>>>> cc1e0fc1916cb6d3f59dbde70a61c61d2614d12e

import os
import re
import shutil

file_pat = re.compile(r"""^(.*?) # all before the zero
    (0*)                        # the zero part
    (.*?)                       # after the zero part
    """, re.VERBOSE
)

for old_file in os.listdir():
    f = file_pat.search(old_file)

    prev_part = f.group(1)
    zero_part = f.group(2)
    next_part = f.group(3)

    if not zero_part:
        continue
    else:
        new_file = prev_part + next_part
        abspath = os.path.abspath('.')
        old_file = os.path.join(abspath, old_path)
        new_file = os.path.join(abspath, new_file)

        print('Renaming %s to %s ...' % (old_file, new_file))
        shutil.move(old_file, new_file)

