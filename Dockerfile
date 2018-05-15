FROM python:2-alpine3.7

ENV MOCK_SMTP_ADDRESS=0.0.0.0
ENV MOCK_SMTP_PORT=25
ENV MOCK_SMTP_PATH=/var/lib/mock-smtp

RUN apk add tzdata --no-cache

COPY mock-smtp.py /usr/sbin/mock-smtp

EXPOSE $MOCK_SMTP_PORT

VOLUME $MOCK_SMTP_PATH

CMD ["/usr/sbin/mock-smtp"]
