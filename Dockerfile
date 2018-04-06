FROM python:2-alpine3.7

ENV MOCK_SMTP_ADDRESS=0.0.0.0

COPY mock-smtp.py /usr/sbin/mock-smtp

EXPOSE 25

VOLUME /var/lib/mock-smtp

CMD ["/usr/sbin/mock-smtp"]

