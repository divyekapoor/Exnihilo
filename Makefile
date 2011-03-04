SRC_DIR=src
BIN_DIR=bin
CSS_DIR=$(SRC_DIR)/css
IMAGES_DIR=$(SRC_DIR)/images
JS_DIR=$(SRC_DIR)/js

DIST_DIR=dist
DIST_CSS=$(DIST_DIR)/css
DIST_IMAGES=$(DIST_DIR)/images
DIST_JS=$(DIST_DIR)/js


.PHONY: dist

dist: 
	@@echo Creating $(DIST_DIR)
	@@mkdir -p $(DIST_DIR)
	@@mkdir -p $(DIST_CSS)
	@@mkdir -p $(DIST_JS)
	
	@@echo Copying Images from $(IMAGES_DIR) to $(DIST_IMAGES)
	@@cp -r $(IMAGES_DIR) $(DIST_IMAGES)
	
	@@echo Operating less.js on .less files
	@@$(BIN_DIR)/lessc $(CSS_DIR)/style.less > $(DIST_CSS)/style.less.css
	@@echo Creating unified and minified CSS in $(DIST_DIR)/css/style.css
	@@cat $(CSS_DIR)/reset.css $(CSS_DIR)/nivo-slider.css $(CSS_DIR)/slide.css $(DIST_CSS)/style.less.css > $(DIST_CSS)/style.css
	@@yui-compressor --type css $(DIST_DIR)/css/style.css -o $(DIST_DIR)/css/style.min.css
	
	@echo Creating unified and minified JS in $(DIST_DIR)/js/scripts.js
	@@cat $(JS_DIR)/jquery-1.4.3.min.js  $(JS_DIR)/jquery.nivo.slider.pack.js $(JS_DIR)/slide.js > $(DIST_DIR)/js/scripts.js
	@@yui-compressor --type js --nomunge $(DIST_DIR)/js/scripts.js -o $(DIST_DIR)/js/scripts.min.js
	
	@@echo Preprocessing and copying HTML files...
	@@./preprocess.sh
	
	@@echo Done.

clean:
	rm -rf dist
