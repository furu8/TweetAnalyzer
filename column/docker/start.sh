#!bin/bash

JUPYTER_CONFIG=/root/.jupyter/jupyter_notebook_config.py

PASSWORD=`python -c 'from notebook.auth import passwd;print(passwd())'`

mkdir -p /root/.jupyter

echo "c.NotebookApp.password = '$PASSWORD'" > JUPYTER_CONFIG

jupyter notebook --no-browser --allow-root --ip 0.0.0.0 --notebook-dir $NOTEBOOK_DIR
