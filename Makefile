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
	
	@@echo Creating unified CSS in $(DIST_DIR)/css/style.css
	@@cat $(CSS_DIR)/reset.css $(CSS_DIR)/nivo-slider.css $(CSS_DIR)/slide.css $(CSS_DIR)/style.css > $(DIST_DIR)/css/style.css
	
	@echo Creating unified JS in $(DIST_DIR)/js/scripts.js
	@@cat $(JS_DIR)/jquery-1.4.3.min.js  $(JS_DIR)/jquery.nivo.slider.pack.js $(JS_DIR)/slide.js > $(DIST_DIR)/js/scripts.js

	@@echo Copying HTML files...
	@@cp $(SRC_DIR)/*.html $(DIST_DIR)/
	
	@@echo Done.

clean:
	@@rm -rf dist
