FROM python:3.9-alpine

WORKDIR /tmp
# RUN pip install pipenv
COPY . /action
# RUN pipenv install --system --deploy

# RUN apk update && apk upgrade && apk add git
# RUN git submodule update --init --recursive

# RUN cp -a ./hugo/. /action/

ENTRYPOINT [ "echo", "Files copied" ]
