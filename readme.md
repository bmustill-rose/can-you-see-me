# Can You See Me

## What Is It

Can You See Me is a simple tool that offers guidance on webcam placement to people with limited amounts of useful vision. Based on simple verbal feedback given by the tool, blind people are able to independently position themselves appropriately in relation to their webcam before attending online meetings such that other sighted participants are able to see them.

The tool uses on-device computer vision, which in non-technical terms means that unlike some other services the images that your webcam captures (and by extension your face) is never sent to third parties.

If you just want to download the tool, I'd suggest you [visit its website](https://www.canyouseeme.app) instead of this page, which is primarily designed for people who have an interest in how the tool has been written.

## Running From Source

1. [Download Python 3.8.10](https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe). The tool should work on any 3x version but it's built using 3.8.10 for Windows 7 support.
2. Clone / download the repo.
3. Run `pip install -r requirements.txt` to install dependencies.
4. Run `python cysm.py`.