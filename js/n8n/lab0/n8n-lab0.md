# Lab 0 - Run n8n on a Linux server using Docker Compose

- https://docs.n8n.io/hosting/installation/server-setups/docker-compose/#3-dns-setup

## 2025-12-17

- test on Github CodeSpace
- Create an `.env` file
```bash
@jazzwang ➜ .../snippet/js/n8n/lab0 (master) $ cat > .env << EOF
> # DOMAIN_NAME and SUBDOMAIN together determine where n8n will be reachable from
> # The top level domain to serve from
> DOMAIN_NAME=example.com
>
> # The subdomain to serve from
> SUBDOMAIN=n8n
>
> # The above example serve n8n at: https://n8n.example.com
>
> # Optional timezone to set which gets used by Cron and other scheduling nodes
> # New York is the default value if not set
> GENERIC_TIMEZONE=Europe/Berlin
>
> # The email address to use for the TLS/SSL certificate creation
> SSL_EMAIL=user@example.com
> EOF
```
- Create an `docker-compose.yml` file
