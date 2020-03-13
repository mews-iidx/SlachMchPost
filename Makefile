ui/main_ui.py: ui/main.ui
	python3 -m PyQt5.uic.pyuic -x $^ -o $@
