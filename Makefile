setup:
	#you should source this: source ~/.myrepo/bin/activate
	#python3 -m venv ~/.myrepo

install:
	pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C s3hello.py face.py detect.py

all: install lint test