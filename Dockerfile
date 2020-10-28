# Receta automatizada para crear imagen
#FROM alpine .. .conviene poner la version
FROM alpine:3.12.1
EXPOSE 80
#Variable de entorno para el DocumentRoot
ENV PATH_WEB=/var/www/localhost/htdocs
#WORKDIR /code
#RUN apk update
#RUN apk add --no-cache apache2 nano
#conviene juntar update && install ... por si está cacheado 
RUN apk update && apk add --no-cache apache2 nano
RUN rm /var/www/localhost/htdocs/index.html
RUN apk add git
#poner al ultimo mi codigo ... que es el que cambia siempre .. caso contrario hay que reconstruir toooodo
RUN git clone https://github.com/umcomp2/docker.git /tmp
#copio solo el "codigo" que uso .. no readme .. no versiones ...etc
RUN mv /tmp/server-web/*html /var/www/localhost/htdocs/
RUN rm -rf /tmp/server-web
#para usar la variable de entorno
COPY httpd.conf /etc/apache2/httpd.conf
#en ADD se puede poner url en COPY solo archivos locales
#ADD httpd.conf /etc/apache2//httpd.conf 
#CMD ["/usr/sbin/httpd", "-D" , "FOREGROUND", "-f" , "/etc/apache2/httpd.conf"]
#ENTRYPOINT no permite overwrite del cmd a ejecutar como punto de entrada
ENTRYPOINT ["/usr/sbin/httpd", "-D" , "FOREGROUND", "-f" , "/etc/apache2/httpd.conf"]
