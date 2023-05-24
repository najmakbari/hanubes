FROM ubuntu
RUN apt update
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt clean

COPY ./ /var/www/html/

RUN ls -al /var/www/html
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 755 /var/www/html


EXPOSE 80
CMD [“apache2ctl”, “-D”, “FOREGROUND”]

