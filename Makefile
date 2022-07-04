PYTHON=      python3.9
SOURCE=      lines
VENV=        venv


$(VENV): requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt
	touch $(VENV)/.depend

upgrade-venv:
	$(VENV)/bin/pip install --upgrade -r requirements.txt
	touch $(VENV)/.depend

reformat: $(VENV)
	$(VENV)/bin/isort $(SOURCE)
	$(VENV)/bin/black $(SOURCE)

realclean:
	rm -fr $(VENV)