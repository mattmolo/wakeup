# Wakeup
Small Flask server that sends a magic packet on HTTP request.

## Why
Running [Home Assistant](https://www.home-assistant.io/) with the default docker-compose network blocks the magic packet. I don't want to put Home Assistant on the host docker network, but I am okay with this small server running on it.
