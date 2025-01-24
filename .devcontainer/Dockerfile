# Base image
ARG VARIANT=bullseye
FROM --platform=amd64 mcr.microsoft.com/devcontainers/python:3.12-${VARIANT}

# Install additional dependencies do I need xdg-utils?
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y xdg-utils wget bzip2 \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install Azure Developer CLI (AZD)
RUN curl -fsSL https://aka.ms/install-azd.sh | bash

# Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p $CONDA_DIR \
    && rm /tmp/miniconda.sh \
    && $CONDA_DIR/bin/conda init bash \
    && $CONDA_DIR/bin/conda clean -ya
ENV PATH="$CONDA_DIR/bin:$PATH"

# Set up Conda environment
RUN conda create -y -n dev python=3.12 \
    && conda clean -ya

# Set Conda default environment
ENV CONDA_DEFAULT_ENV=dev
ENV PATH=$CONDA_DIR/envs/$CONDA_DEFAULT_ENV/bin:$PATH

# Install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN conda run -n dev pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt
    
# Activate Conda in every shell
RUN echo "conda init" >> ~/.bashrc
RUN echo "conda activate dev" >> ~/.bashrc

# --------------------
# ** Install Docker ** 
# --------------------
# RUN apt-get update -y \
#     && apt-get install -y \
#        ca-certificates \
#        curl \
#        gnupg \
#        lsb-release

# Add Docker’s official GPG key + repository
# RUN mkdir -p /etc/apt/keyrings \
#     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
#     && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bullseye stable" \
#        | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine & Compose
# RUN apt-get update -y \
#     && apt-get install -y \
#        docker-ce \
#        docker-ce-cli \
#        containerd.io \
#        docker-buildx-plugin \
#        docker-compose-plugin

# Create 'docker' group (force, ignore if exists) and add 'vscode' user
# RUN groupadd --force docker \
#     && usermod -aG docker vscode

# (Optional) Clean up
RUN apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Done!
