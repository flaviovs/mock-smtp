VERSION = 0.0.1

all: build

build: build-stamp

build-stamp: Dockerfile mock-smtp.py
	docker build -t flaviovs/mock-smtp:$(VERSION) .
	docker tag flaviovs/mock-smtp:$(VERSION) flaviovs/mock-smtp:latest
	: > $@

push: build push-stamp

push-stamp: build-stamp
	docker push flaviovs/mock-smtp:$(VERSION)
	docker push flaviovs/mock-smtp:latest
	: > $@

clean:
	rm -f *~ *-stamp

.PHONY: all build push clean

