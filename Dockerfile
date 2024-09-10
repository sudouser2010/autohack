# Kali Linux latest with useful tools by tsumarios
FROM kalilinux/kali-rolling

# Set working directory to /root
WORKDIR /root

# Update
RUN apt -y update && apt -y dist-upgrade && apt -y autoremove && apt clean

# Install common and useful tools
RUN apt -y install curl wget vim git net-tools whois netcat-traditional pciutils usbutils

# Install useful languages
RUN apt -y install python3-pip golang nodejs npm

## Install useful cybersecurity tools
RUN apt -y install kali-tools-top10 exploitdb man-db dirb nikto wpscan uniscan lsof apktool dex2jar ltrace strace binwalk \
    seclists snmp smbmap smbclient smtp-user-enum nbtscan enum4linux medusa sipvicious patator \
    oscanner tnscmd10g rpcbind nfs-common sqsh dirsearch whatweb wkhtmltopdf unicornscan


# Install Conda for AutoHack
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

# Install conda
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh \
RUN conda --version
RUN conda init

# Setup AutoHack Python Package
RUN conda create --name autohack python=3.10 --yes
RUN /root/miniconda3/envs/autohack/bin/pip install autohack==0.1 --root-user-action=ignore

# Activate AutoHack Conda On Container Start
RUN echo "source activate autohack" > ~/.bashrc
