# Docker Commands

We build a Redis docker image with customized configuration
so that we can easily trigger eviction event.

```
docker build -f redis.dockerfile -t redis-server .
```

To run this docker image

```
docker run --name redis -p 6379:6379 -t redis-server
```

To run Pulsar in docker
```
docker run -it -p 6650:6650 -p 8080:8080 --mount source=pulsardata,target=/pulsardata --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:3.0.0 bin/pulsar standalone
```