.PHONY: collect
collect:
	python collection/collect_image.py

.PHONY: train
train:
	python train/main.py

.PHONY: run
run:
	python main/main.py
