# Use a more specific base image with pre-installed conda
FROM mcr.microsoft.com/devcontainers/python:1-3.12

# Install system dependencies in one layer
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y wget bzip2 && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Install Azure Developer CLI
RUN curl -fsSL https://aka.ms/install-azd.sh | bash

# Install Mambaforge for faster conda operations
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh -O /tmp/mambaforge.sh && \
    bash /tmp/mambaforge.sh -b -p ${CONDA_DIR} && \
    rm /tmp/mambaforge.sh && \
    ${CONDA_DIR}/bin/conda clean -ya

# Set up conda environment and install packages
COPY environment.yml /tmp/environment.yml
RUN ${CONDA_DIR}/bin/mamba env create -f /tmp/environment.yml && \
    ${CONDA_DIR}/bin/mamba clean -ya && \
    rm /tmp/environment.yml

# Register Jupyter kernel and set permissions
RUN ${CONDA_DIR}/envs/dev/bin/python -m ipykernel install --user --name dev --display-name "Python (dev)" && \
    chown -R vscode:${CONDA_DIR} ${CONDA_DIR} && \
    chmod -R 775 ${CONDA_DIR}

# Activate environment in shell
ENV PATH="${CONDA_DIR}/envs/dev/bin:${PATH}"
RUN echo "conda activate dev" >> /home/vscode/.bashrc

# Ensure proper permissions
USER vscode
WORKDIR /workspace