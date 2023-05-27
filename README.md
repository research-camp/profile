# HAProxy

![](https://img.shields.io/badge/lang-python-blue)
![](https://img.shields.io/badge/tool-haproxy-orange)

```HAProxy``` (High Availability Proxy) is open source proxy and load balancing server software.
It provides high availability at the network (TCP) and application (HTTP/S) layers,
improving speed and performance by distributing workload across multiple servers.

## HAProxy vs NginX

```Haproxy``` is typically used for load balancing, while ```Nginx``` is often used as a web server or reverse proxy.
```Haproxy``` can be more suitable in cases where you need to distribute traffic across multiple servers and/or services,
whereas ```Nginx``` may be better suited for serving static content from a single server.

```Haproxy``` is an open source software TCP/HTTP load balancer and proxying solution.
In general, ```Nginx``` should be chosen over ```Haproxy``` when you need to serve large
amounts of static content (e.g., images) or if you require advanced features such as URL rewriting or caching capabilities.

## Install

You can install ```HAProxy``` using this [link](https://haproxy.debian.net/).

```shell
sudo apt-get update
sudo apt-get install haproxy=2.4.\*
```

### Config

Now that you have HAProxy installed, let’s see how to configure it.
All settings are defined in the file ```/etc/haproxy/haproxy.cfg``` (or /etc/hapee-{version}/hapee-lb.cfg for HAProxy Enterprise).
If you are using Docker, then this file is mounted as a volume into the container
at the path ```/usr/local/etc/haproxy/haproxy.cfg```.

## Example

To define the IP address and port at which HAProxy should receive traffic, add a frontend section to your haproxy.cfg file.
Inside this section, add a bind line. A bind line sets the IP address and port to listen on.

```cfg
defaults
  mode http
  timeout client 10s
  timeout connect 5s
  timeout server 10s 
  timeout http-request 10s

frontend myfrontend
  bind 127.0.0.1:80
```

## Resources

- [haproxy.com](https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/)
