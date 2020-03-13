all: dist/main.exe dist/configs



ui/main_ui.py: ui/main.ui
	python3 -m PyQt5.uic.pyuic -x $^ -o $@

dist/main.exe: main.py ui/main_ui.py  
	pyinstaller.exe main.py --onefile 

dist/configs:
	cp -r configs dist/

clean:
	$(RM) build __pycache__ dist ui/*.py 
