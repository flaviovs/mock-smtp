Mock SMTP
=========

_Mock SMTP_ is a SMTP server that does not deliver message, instead it save
the messages to files in your file system.

This is a development tool, used to test email sending from apps.


How to Run via Command Line
===========================

    # python mock-smtp.py

By default the server will listen on port 25, and bind to 127.0.0.1, plus
e-mails will be saved to startup directory. This behaviour can be changes by
using the following environment variables, respectively:

 - `MOCK_SMTP_ADDRESS`
 - `MOCK_SMTP_PORT`
 - `MOCK_SMTP_PATH`

**Note**: _Mock SMTP_ must be run as root for binding to ports below 1024,
otherwise you will get a _PermissionError_ exception. When run as root, the
daemon will drop privileges, and assume the same identify of the owner/group
of current directory or (the one specified in `MOCK_SMTP_PATH`), after the
SMTP socket is open.


How to Run via Docker
=====================

    $ mkdir emails
    $ docker run --rm -p 25:25 -v $(pwd)/emails:/var/lib/mock-smtp -d flaviovs/mock-smtp
    $ telnet localhost 25
    220 97e09283eb3f Python SMTP proxy version 0.2


Issues?
=======
Visit https://github.com/flaviovs/mock-smtp
