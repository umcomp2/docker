# Receta automatizada para crear imagen
FROM alpine
#WORKDIR /code
RUN apk update
RUN apk add --no-cache apache2 nano
RUN apk add git
RUN rm -rf /var/www/localhost/
RUN git clone https://github.com/umcomp2/docker.git /tmp
RUN mv /tmp/server-web/*html /var/www/localhost/htdocs/
#COPY index.html /var/www/localhost/htdocs/index.html 
CMD ["/usr/sbin/httpd", "-D" , "FOREGROUND", "-f" , "/etc/apache2/httpd.conf"]
