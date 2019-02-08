docker build -t redis-builder . && \
docker run redis-builder | \
docker build -t tiny-redis -
