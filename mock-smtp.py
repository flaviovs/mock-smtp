#!/usr/local/bin/python

import sys
import os
import smtpd
import asyncore
import logging
import datetime
import email.utils
import signal

logging.basicConfig(stream=sys.stderr,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.DEBUG)

os.chdir(os.getenv('MOCK_SMTP_PATH', '.'))

class MockSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

        today = datetime.datetime.today();

        file = '%s.eml' % today.strftime('%Y-%d-%mT%T.%f')

        mail = open(file, "w")
        mail.write('Return-Path: <%s>\n' % mailfrom)
        for to in rcpttos:
            mail.write('Envelope-To: <%s>\n' % to)
        mail.write('Delivery-Date: %s\n' % email.utils.format_datetime(today))
        mail.write(data)
        mail.close()

        logging.info('%s => %s: %s', mailfrom, rcpttos, file)


def handle_signal(signalnum, frame):
    if signalnum == signal.SIGTERM:
        #asyncore.socket_map.clear()
        raise asyncore.ExitNow('SIGTERM')


logging.info('Starting up Mock SMTP server')

smtp_server = MockSMTPServer((os.getenv('MOCK_SMTP_ADDRESS', '127.0.0.1'),
                              int(os.getenv('MOCK_SMTP_PORT', '25'))),
                             None)

if os.getuid() == 0:
    # Switch to UID/GID of owner of current path.
    stat = os.stat('.')
    os.setgroups([])

    os.setgid(stat.st_uid)
    os.setuid(stat.st_gid)
    os.umask(0o77)

# Install signal handler, for handling SIGTERM.
signal.signal(signal.SIGTERM, handle_signal)

# Start the server
try:
    asyncore.loop()
except (KeyboardInterrupt, asyncore.ExitNow):
    pass
except Exception as ex:
    logging.exception(ex)

smtp_server.close()
