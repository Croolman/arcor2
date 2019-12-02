FROM python:3

RUN cd \
	&& git clone https://github.com/s-knibbs/dataclasses-jsonschema.git \
	&& cd dataclasses-jsonschema \
	&& pip install -e .

RUN cd \
	&& git clone https://github.com/capripot/wait-for.git \
	&& cd wait-for \
	&& git checkout http-tests \
	&& cp wait-for /wait-for

RUN pip install --upgrade setuptools PyYAML

COPY . /root/arcor2


RUN cd ~/arcor2 \
	&& pip install -e .

RUN ln -s /root/arcor2/docker/start.sh /start.sh

RUN mkdir -p ~/project
ENV PYTHONPATH ~
ENV ARCOR2_PROJECT_PATH /root/project

expose 6789
