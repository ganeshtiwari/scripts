from pathlib import Path

files = Path(str(Path.home()) + '/Pictures' + '/anime').glob('*')

for p in sorted(files):
    new_file_name = p.stem + '.jpg'
    p.rename(Path(p.parent, new_file_name))