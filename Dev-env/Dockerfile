# Take the Python Base image
FROM python:3

# Update the OS and install pip package manager
RUN apt-get update && apt-get install -y python3-pip

# Set the working directory
WORKDIR /home

# Copy the requirement.txt, README files
COPY requirement.txt .
COPY README.md .

# Install all requirement.txt
RUN pip install -r requirement.txt

# Install jupyter-lab
RUN pip install jupyterlab

# Create the two folders 
RUN mkdir notebook data

# Run the jupyter-lab
ENTRYPOINT [ "jupyter-lab","--ip=0.0.0.0", "--allow-root"]