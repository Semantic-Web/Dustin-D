## Using the event filter tool

### Description

This component audits the dnsmasq event-log, parsing the lines, discards irrelevant entries, queues batches of events/messages, and ushes them to the DNS message receiver server.

### Requirements

- dnsmasq DNS server to produce logs. Sample logs are provided (in the event that you don't want to install this).
- Install the packages listed under "requirements" at the top of the script: "sudo pip install XYZ"

### Usage

1. Configure *dnsmasq* to write events to a log-file by modifying the /etc/init.d/dnsmasq service definition and adding the following parameters to the `start-stop-daemon` command in the `start` section (around line 120):

    ```
    --log-async
    --log-facility=/var/log/dnsmasq.log
    ```

2. Restart *dnsmasq*.
3. Download the *[dnsmasq_filter](dnsmasq_filter)* tool from the Assignment 3 root under my project.
4. Pipe the log-file into the *dnsmsq_filter* tool, whereever you installed it. The following is an example of the command, though the URL will not be available until you install/configure the server below. Note that the "-ru" parameter (which specifies the "receiver URL" can be omitted and the parsed entries will just be printed to the screen). There is command-line help for this tool. Just pass "-h":

    ```
    $ cat /var/log/dnsmasq.log | /home/dustin/dnsmasq_filter -ru http://localhost:81/dns/message
    ```
