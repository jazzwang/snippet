all:	.installed
		@python spelling_bee.py -h
		@python spelling_bee.py -s 7 spelling-bee-2b1.txt
		@python spelling_bee.py spelling-bee-2b1.txt
setup: 
		@pip install google-cloud-texttospeech soundfile pydub
		@sudo apt-get -y install ffmpeg
		@touch .installed

