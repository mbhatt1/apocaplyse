
FROM gliderlabs/alpine:3.1
MAINTAINER Cory Altheide "coryaltheide@gmail.com"
ADD Dockerfile.run /Dockerfile
RUN apk --update add redis && chown redis /var/lib/redis && chmod +x /var/lib/redis
CMD tar -cf - /Dockerfile /etc/passwd /var/lib/redis /etc/group /usr/bin/redis-server /lib/ld-musl-x86_64.so.1 /lib/libc.musl-x86_64.so.1

