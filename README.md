
# description

Program identifies file types from raw byte headers and compares them to a database of extensions, flagging mismatches.

# install (clone)

`git clone https://github.com/ambeRAWR/Filetype-ID`

# permissions and file setup

Then add permissions, and move to binaries:

```bash
chmod +x filetypeID.py
sudo cp filetypeID.py /usr/local/bin/filetypeID
```

or if youre developing and want a symlink:
 
`sudo ln -s $(pwd)/filetypeID.py /usr/local/bin/filetypeID`

# running:

typical usage:

`filetypeID <file>`

