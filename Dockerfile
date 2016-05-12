FROM andrewosh/binder-base

USER root
RUN apt-get update

USER main
RUN conda install scikit-learn seaborn bokeh jupyter
# RUN conda install -n python3 scikit-learn seaborn bokeh jupyter
RUN /home/main/anaconda/envs/python3/bin/pip install seaborn

RUN conda install -c jjhelmus tensorflow=0.8.0rc0
# RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp34-cp34m-linux_x86_64.whl
