
# Description

Program identifies file types from raw byte headers and compares them to a database of extensions, flagging mismatches.

# Clone Repo

`git clone https://github.com/ambeRAWR/Filetype-ID`

# Permissions and file setup

Then add permissions, and move to binaries:

```bash
chmod +x filetypeID.py
sudo cp filetypeID.py /usr/local/bin/filetypeID
```

or if youre developing and want a symlink:
 
`sudo ln -s $(pwd)/filetypeID.py /usr/local/bin/filetypeID`

# Running:

typical usage:

`filetypeID <file>`

