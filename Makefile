build:
	python setup.py install
	
run:
	python firmware.py

tests:
	python tests/export_test

usb:
	python usb.py &

.PHONY: build run tests