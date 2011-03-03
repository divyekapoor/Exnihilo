SRC_DIR=src
CSS_DIR=$(SRC_DIR)/css
IMAGES_DIR=$(SRC_DIR)/images
JS_DIR=$(SRC_DIR)/js

DIST_DIR=dist

.PHONY: dist

dist: 
	@@echo Creating $(DIST_DIR)
	@@mkdir -p $(DIST_DIR)
	@@mkdir -p $(DIST_DIR)/css
	@@mkdir -p $(DIST_DIR)/js
	
	@@echo Copying Images from $(IMAGES_DIR)
	@@cp -r $(IMAGES_DIR) $(DIST_DIR)/images
	
	@@echo Creating unified and minified CSS in $(DIST_DIR)/css/style.css
	@@cat $(CSS_DIR)/reset.css $(CSS_DIR)/nivo-slider.css $(CSS_DIR)/slide.css $(CSS_DIR)/style.css > $(DIST_DIR)/css/style.css
	@@yui-compressor --type css $(DIST_DIR)/css/style.css -o $(DIST_DIR)/css/style.min.css
	
	@echo Creating unified and minified JS in $(DIST_DIR)/js/scripts.js
	@@cat $(JS_DIR)/jquery-1.4.3.min.js  $(JS_DIR)/jquery.nivo.slider.pack.js $(JS_DIR)/slide.js > $(DIST_DIR)/js/scripts.js
	@@yui-compressor --type js --nomunge $(DIST_DIR)/js/scripts.js -o $(DIST_DIR)/js/scripts.min.js
	
	@@echo Copying HTML files...
	@@./preprocess.sh
	
	@@echo Done.

clean:
	rm -rf dist
