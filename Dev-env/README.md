# Dev-Env container

*This is Docker contianer use for creating the dev enviroment to launch the Jupyter-Lab*

Add the packages name that need to pre-install in `requirement.txt` file.

To build the contianer 
```shell
cd Dev-Env
docker build -t dev_env .
```

To run the container
```shell
docker run --name project_name -p 8888:8888 dev_env
```
Optionaly you can volumn mount the data folder
```shell
docker run --name project_name_data -v <local_path>/data:/home/data -p 8888:8888 dev_env
```

Container follow this file structure. 
```
home/
    |
    |- data/
    |- notebooks/
    |- requirement.txt
    |- README.md
```


