## Installing DNS message receiver server

### Description

This component receives the parsed/filtered events from the filter tool, stores them, and charts them.

### Requirements

- A [RethinkDB](http://www.rethinkdb.com) instance.
- Python 2.7 and PIP (sudo apt-get install python-pip)

### Installation

1. Downloaded release archive.
2. Installed:

    ```
    $ sudo pip install dmr-0.1.9.tar.gz
    ```

3. Configured Nginx.
   1. Installed:

       ```
       $ sudo apt-get install -y nginx
       ```

   2. Copied *dmr/resources/nginx/dmr.conf* to */etc/nginx/sites-enabled*. You can also copy it directly from the project directory, after installed:

    ```
    $ sudo cp /usr/local/lib/python2.7/dist-packages/dmr/resources/nginx/dmr.conf /etc/nginx/sites-enabled
    ```

   3. If Apache2 is installed, Nginx's default sample site will conflict on port 80. Either disable Apache and turn it off or remove the default site from Nginx (this won't affect our project):

    ```
    $ sudo rm /etc/nginx/sites-enabled/default
    ```

   4. Our project runs on port 8080. If you prefer something else, make the change to *dmr.conf*.
   5. Restart Nginx:

    ```
    $ sudo service nginx restart
    ```

### Usage

1. If your database isn't hosted locally, set the database host in the environment (if nothing else, you can use */etc/environment*). For example:

    ```
    export DMR_DB_HOSTNAME=dustinhub
    ```

2. Provision the DB. This is idempotent and will not do anything that's already been done:

    ```
    $ dmr_db_provision
    ```

3. Start the server. It must be root, and note that, if you've defined the database in the environment, *sudo* will largely ignore any environment variables. So, you'd best run this *while actually being* root:

    ```
    $ dmr_server_prod
    ```

4. Open the webpage in the browser on port 8080 (unless you've changed the default). e.g., http://dustinberry2:8080
5. The chart will be shown on the homepage.
6. For good measure, there is also a command-line tool to dump the last day's worth of data, grouped by hour and type:

    ```
    dustin@dustinberry2:~$ dmr_db_model_dns_message_print_by_hour 
    [(2015, 7, 7, 4)] [query[AAAA]]: (66)
    [(2015, 7, 7, 4)] [query[A]]: (644)
    [(2015, 7, 7, 4)] [query[PTR]]: (582)
    [(2015, 7, 7, 4)] [query[TXT]]: (1)
    [(2015, 7, 7, 5)] [query[AAAA]]: (75)
    [(2015, 7, 7, 5)] [query[A]]: (720)
    [(2015, 7, 7, 5)] [query[PTR]]: (765)
    [(2015, 7, 7, 6)] [query[AAAA]]: (80)
    [(2015, 7, 7, 6)] [query[A]]: (735)
    [(2015, 7, 7, 6)] [query[PTR]]: (146)
    [(2015, 7, 7, 6)] [query[TXT]]: (2)
    ...
    ```
