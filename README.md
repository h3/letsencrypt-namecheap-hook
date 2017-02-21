# /!\ ATTENTION: Letsencrypt.sh is now deprecated, it was replaced by dehydrated:

https://github.com/lukas2511/dehydrated

**This project is not compatible with dehydrated, it is therefor deprecated too.**

# NameCheap hook for `letsencrypt.sh`

This a hook for [letsencrypt.sh](https://github.com/lukas2511/letsencrypt.sh) (a [Let's Encrypt](https://letsencrypt.org/) ACME client) that allows you to use [NameCheap](https://www.namecheap.com/) DNS records to respond to `dns-01` challenges. Requires Python and your NameCheap account and API key being in the environment.

**Credits**: This hook is eavily based on [letsencrypt-cloudflare-hook](https://github.com/kappataumu/letsencrypt-cloudflare-hook) and [PyNamecheap](https://github.com/Bemmu/PyNamecheap).

## Installation

On Debian based OS, the following packages are required:

```bash
$ sudo apt-get install libffi-dev libssl-dev python3-dev python-virtualenv
```

```bash
$ git clone https://github.com/lukas2511/letsencrypt.sh
$ cd letsencrypt.sh
$ mkdir hooks
$ git clone https://github.com/h3/letsencrypt-namecheap-hook.git
$ cd hooks
$ virtualenv --python=python3 venv
$ ./venv/bin/pip install -r requirements.pip
```

## Configuration

Your NameCheap account's credentials and API key are expected to be in the environment, so make sure to:

```
$ export NC_USERNAME="YourUserName"
$ export NC_CLIENT_IP="ip.of.ser.ver"
$ export NC_API_KEY="API-KEY"
$ export NC_API_USER="$NC_USERNAME"
```

Optionally, you can specify the DNS servers to be used for propagation checking via the `CF_DNS_SERVERS` environment variable (props [bennettp123](https://github.com/bennettp123)):

```
$ export NC_NAMESERVERS="216.87.155.33 216.87.152.33"
```
**WARNING**: Always use ip addresses, **not hostnames!**

Alternatively, these statements can be placed in `letsencrypt.sh/config.sh`, which is automatically sourced by `letsencrypt.sh` on startup:

```
$ echo "export NC_USERNAME='YourUserName'" >> config.sh
$ echo "export NC_CLIENT_IP='ip.of.ser.ver'" >> config.sh
$ echo "export NC_API_KEY='API-KEY'" >> config.sh
$ echo "export NC_API_USER='$NC_USERNAME'" >> config.sh
$ echo "export NC_NAMESERVERS='216.87.155.33 216.87.152.33'" >> config.sh
```

## Usage

```
$ ./letsencrypt.sh -c -d example.com -t dns-01 -k 'hooks/letsencrypt-namecheap-hook/bin/letsencrypt-namecheap-hook'
#
# !! WARNING !! No main config file found, using default config!
#
Processing example.com
 + Signing domains...
 + Creating new directory /home/user/letsencrypt.sh/certs/example.com ...
 + Generating private key...
 + Generating signing request...
 + Requesting challenge for example.com...
 + NameCheap hook executing: deploy_challenge
 + DNS not propagated, waiting 30s...
 + DNS not propagated, waiting 30s...
 + Responding to challenge for example.com...
 + NameCheap hook executing: clean_challenge
 + Challenge is valid!
 + Requesting certificate...
 + Checking certificate...
 + Done!
 + Creating fullchain.pem...
 + NameCheap hook executing: deploy_cert
 + ssl_certificate: /home/user/letsencrypt.sh/certs/example.com/fullchain.pem
 + ssl_certificate_key: /home/user/letsencrypt.sh/certs/example.com/privkey.pem
 + Done!
```

## Contributions

This hook is offered as is, so reported issues are note guaranteed to be resolved, however pull requests are welcome.
