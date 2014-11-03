DOCKISTRY=dockistry.quizup.com
SERVICE=quizup/flask-test-kata
GIT_CHANGE_EPOCH=$(shell git log -n1 --format='%at')
TOUCH_TIMESTAMP=$(shell perl -e 'use POSIX strftime; print(strftime("%Y%m%d%H%M", localtime($(GIT_CHANGE_EPOCH))));')

ifndef GITHASH
        GITHASH=$(shell git log -n1 --format='%H')
endif

all: build

build:
	cd .. && git archive --format=tgz $(GITHASH) > build/src.tgz
	echo $(GITHASH) > githash
	cp ../requirements.txt .
	touch -t $(TOUCH_TIMESTAMP) src.tgz  # set modification time to please cache
	touch -t $(TOUCH_TIMESTAMP) githash
	touch -r ../requirements.txt requirements.txt
	docker build --rm=true -t $(DOCKISTRY)/$(SERVICE) .
	docker tag $(DOCKISTRY)/$(SERVICE) $(DOCKISTRY)/$(SERVICE):$(GITHASH)
	rm -f src.tgz
	rm -f githash
	rm -f requirements.txt

run: build
	docker run -it -p 80:8000 $(DOCKISTRY)/$(SERVICE)

test: build
	docker run -v /tmp:/testoutput -it $(DOCKISTRY)/$(SERVICE) /app/build/runtests.sh
