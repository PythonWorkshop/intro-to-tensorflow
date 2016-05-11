FROM andrewosh/binder-base

# USER root
# RUN apt-get update

# USER main

conda install scikit-learn seaborn bokeh jupyter
#conda install -c jjhelmus tensorflow=0.8.0rc0
