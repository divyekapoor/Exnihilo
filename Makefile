SRC_DIR=src
BIN_DIR=bin
DEBUG_DIR=debug
MEDIA_DIR=exnihilo/media

SRC_CSS=$(SRC_DIR)/css
SRC_IMAGES=$(SRC_DIR)/images
SRC_JS=$(SRC_DIR)/js

DEBUG_CSS=$(DEBUG_DIR)/css
DEBUG_JS=$(DEBUG_DIR)/js
DEBUG_IMAGES=$(DEBUG_DIR)/images

DIST_DIR=dist
DIST_CSS=$(DIST_DIR)/css
DIST_IMAGES=$(DIST_DIR)/images
DIST_JS=$(DIST_DIR)/js


.PHONY: dist debug media clean all

all: dist debug media zip

debug: 
	mkdir -p $(DEBUG_DIR)
	cp -r $(SRC_CSS) $(DEBUG_CSS)
	cp -r $(SRC_IMAGES) $(DEBUG_IMAGES)
	cp -r $(SRC_JS) $(DEBUG_JS)
	$(BIN_DIR)/preprocess.sh $(DEBUG_DIR) -DDEBUG

media: dist
	mkdir -p $(MEDIA_DIR)
	cp -r $(DIST_CSS) $(MEDIA_DIR)
	cp -r $(DIST_IMAGES) $(MEDIA_DIR)
	cp -r $(DIST_JS) $(MEDIA_DIR)

runserver: debug dist media
	xterm -e '/usr/bin/env node serve.js' &
	xterm -e '/usr/bin/env python exnihilo/manage.py runserver' &

dist: 
	@@echo Creating $(DIST_DIR) $(DIST_CSS) $(DIST_JS)
	@@mkdir -p $(DIST_DIR)
	@@mkdir -p $(DIST_CSS)
	@@mkdir -p $(DIST_JS)
	
	@@echo Copying Images from $(SRC_IMAGES) to $(DIST_IMAGES)
	@@cp -r $(SRC_IMAGES) $(DIST_IMAGES)
	
	@@echo Operating less.js on .less files
	@@$(BIN_DIR)/lessc $(SRC_CSS)/style.less > $(DIST_CSS)/style.less.css
	@@echo Creating unified and minified CSS in $(DIST_CSS)/style.min.css
	@@cat $(SRC_CSS)/reset.css $(SRC_CSS)/nivo-slider.css $(SRC_CSS)/slide.css $(SRC_CSS)/animation.css $(DIST_CSS)/style.less.css > $(DIST_CSS)/style.css
	@@yui-compressor --type css $(DIST_DIR)/css/style.css -o $(DIST_DIR)/css/style.min.css
	
	@echo Creating unified and minified JS in $(DIST_JS)/scripts.js
	@@cat $(SRC_JS)/jquery-1.4.3.min.js  $(SRC_JS)/jquery.nivo.slider.pack.js $(SRC_JS)/slide.js $(SRC_JS)/jquery.color.js  $(SRC_JS)/jquery.rating.pack.js > $(DIST_JS)/scripts.js
	@@yui-compressor --type js --nomunge $(DIST_DIR)/js/scripts.js -o $(DIST_DIR)/js/scripts.min.js
	
	@@echo Preprocessing and copying HTML files...
	@@$(BIN_DIR)/preprocess.sh $(DIST_DIR) -DRELEASE
	
	@@echo Done.


zip: dist
	zip -9 -r exnihilo.zip dist

clean:
	rm -rf $(MEDIA_DIR)
	rm -rf $(DIST_DIR)
	rm -rf $(DEBUG_DIR)
	rm -f exnihilo.zip

