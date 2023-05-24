FROM najmastudent/naububase23
RUN apt update -y
RUN apt upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt install -y apache2
RUN DEBIAN_FRONTEND=noninteractive apt install -y php
RUN echo "<h1>dit is een HTMLtest</h1>"> /var/www/html/test.html
RUN echo "<?php echo '<h1>dit is een PHPtest </h1>'; ?>"> /var/www/html/test.php