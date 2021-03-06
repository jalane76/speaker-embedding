FROM pytorch/pytorch

ENV DEBIAN_FRONTEND=noninteractive

COPY apt-requirements.txt /tmp/apt-tmp/
COPY requirements.txt /tmp/pip-tmp/

# Install packages
# Configure apt and install packages
RUN apt-get update \

    # Update Linux packages based on apt-requirements.txt
    && cat /tmp/apt-tmp/apt-requirements.txt | xargs apt-get -y install \
    && rm -rf /tmp/apt-tmp \

    # Install Python dependencies
    && pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp \

    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Clone git repository dependencies
RUN mkdir /repos \
    && cd /repos \
    && git clone https://github.com/pyannote/pyannote-audio.git \
    && cd pyannote-audio \
    && git checkout develop \
    && pip install . \
    && cd /repos \
    && git clone https://github.com/juanmc2005/SpeakerEmbeddingLossComparison.git

ENV DEBIAN_FRONTEND=dialog

ENV PYTHONPATH "${PYTHONPATH}:/workspace/:repos"