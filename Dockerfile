FROM andrewosh/binder-base

USER root
RUN apt-get update

USER main
RUN conda install scikit-learn seaborn bokeh jupyter
RUN conda install -c jjhelmus tensorflow=0.8.0rc0
