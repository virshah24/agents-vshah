# Start from the devcontainers Python image for convenience
FROM mcr.microsoft.com/devcontainers/python:1-3.12

# Switch off interactive front-end
ENV DEBIAN_FRONTEND=noninteractive

# [Optional] Install Miniconda, or skip if you want only pip + venv
RUN apt-get update && apt-get install -y wget bzip2 \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    #
    # Download & Install Miniconda
    && wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -b -p /opt/conda \
    && rm /tmp/miniconda.sh

ENV CONDA_DIR=/opt/conda
ENV PATH="$CONDA_DIR/bin:$PATH"

# Initialize Conda for bash
RUN conda init bash

# Create and activate a new environment named "dev" with Python 3.12
RUN conda create -y -n dev python=3.12 && conda clean -ya
ENV CONDA_DEFAULT_ENV=dev
ENV PATH=$CONDA_DIR/envs/$CONDA_DEFAULT_ENV/bin:$PATH

# Copy in your requirements
WORKDIR /workspace
COPY requirements.txt .

# Install your Python packages in the "dev" conda environment
RUN conda run -n dev pip install -r requirements.txt --no-cache-dir

# Install a named kernel so Jupyter sees "Python (dev)" if you want
RUN conda run -n dev python -m ipykernel install --user --name dev --display-name "Python (dev)"

# Force conda activate for all newly launched shells
RUN echo "conda activate dev" >> ~/.bashrc

# Clean up
RUN apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Done!
