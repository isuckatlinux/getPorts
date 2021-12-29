# getPorts

## Credits
First of all, I have to say this is not an original idea, I pulled it from [S4vitar](https://github.com/s4vitar). However I just took the idea, the reason why I didn't forked the repo, is because I didn't look the code, I just writed all by my own.
Anyway, I recommend his content if you want to learn cybersecurity.

## What is getPorts?
getPorts is a tool that extract the most relevant information about the nmap grepeable format and dump all the ports found on the clipboard
*You can generate a grepeable file with -oG flag*

## Installation
Very easy to install.

1.Clone the repo
```bash
git clone https://github.com/isuckatlinux/getPorts
```

2.Install it
```bash
sudo chmod +x install.sh
sudo ./install.sh
```

## Usage
```bash
getPorts *grepeable_file*
```

You will have an output with the most relevant information and all the ports copied on the clipboard with this format: *p1,p2,pn*


