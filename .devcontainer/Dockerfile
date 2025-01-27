# Start from the official Dev Containers Python base 
FROM mcr.microsoft.com/devcontainers/python:1-3.12

# Avoid interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# 1. Install apt dependencies, Azure Dev CLI (azd), and Miniconda in one shot
RUN apt-get update && apt-get install -y xdg-utils wget bzip2 curl \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    #
    # Install Azure Developer CLI (AZD)
    && curl -fsSL https://aka.ms/install-azd.sh | bash \
    #
    # Download & install Miniconda
    && wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p /opt/conda \
    && rm /tmp/miniconda.sh

# Initialize Conda for bash
ENV CONDA_DIR=/opt/conda
ENV PATH="$CONDA_DIR/bin:$PATH"
RUN $CONDA_DIR/bin/conda init bash

# 2. Create your 'dev' conda environment and install dependencies
RUN conda create -y -n dev python=3.12 && conda clean -ya
ENV CONDA_DEFAULT_ENV=dev
ENV PATH="$CONDA_DIR/envs/$CONDA_DEFAULT_ENV/bin:$PATH"

# 3. Copy and install Python packages
WORKDIR /workspace
COPY requirements.txt .
RUN conda run -n dev pip install --no-cache-dir -r requirements.txt

# 4. (Optional) Add a named kernel for Jupyter
RUN conda run -n dev python -m ipykernel install --user --name dev --display-name "Python (dev)"

# 5. Clean up apt cache again (optional)
RUN apt-get clean -y && rm -rf /var/lib/apt/lists/*

# By default, when you 'exec' into this container, you'll have the environment available
RUN echo "conda activate dev" >> ~/.bashrc

