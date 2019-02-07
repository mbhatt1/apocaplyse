readonly DOCKER="/usr/bin/docker --"

${DOCKER} build -t redis-builder . && \
${DOCKER} run redis-builder | \
${DOCKER} build -t tiny-redis -
