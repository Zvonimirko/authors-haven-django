ARG PYTHON_VERSION=3.10-bullseye

FROM python:${PYTHON_VERSION} as python


FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

# By setting PYTHONDONTWRITEBYTECODE to 1, you prevent Python from generating .pyc files, which can be helpful in environments where minimizing disk I/O, reducing container size, or improving startup performance is a concern.
ENV PYTHONDONTWRITEBYTECODE 1

# ENV PYTHONUNBUFFERED 1 is used to ensure that Python doesn't buffer the output, allowing logs and messages to be immediately visible in the container's output, which is useful for debugging and monitoring applications.
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
  libpq-dev \
  gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# for optimization of space
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
# to insure taht the slash entry point file has unique style line endings instead of windows style line endings.
# important because Linux expects unique style endings and win style endings can cause problems when executing scripts or reading
# configuration files
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . ${APP_HOME}

# defines primary command that is executed when container is launched
ENTRYPOINT ["/entrypoint"]