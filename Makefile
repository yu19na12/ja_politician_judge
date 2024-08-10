.PHONY: collect
collect:
	python collection/main.py

.PHONY: train
train:
	python train/main.py

.PHONY: run
run:
	python main/main.py
