EXE         = asysc
BIN_DIR     = $(shell mkdir -p bin) bin
LIB_DIR     = src
APP_DIR     = app
RULES_DIR   = rules
OBJ_DIR     = $(shell mkdir -p objs/nostd objs/std objs/asysc) objs
LIB         = lib$(EXE).a
EXE_OBJ     = $(APP_SRC:%.cpp=$(OBJ_DIR)/%.o) $(OBJ_DIR)/asysc/help.o
LIB_OBJS    = $(LIB_SRC:%.cpp=$(OBJ_DIR)/%.o)
INCDIR      = -I$(LIB_DIR)
RULE_FILES  = $(addprefix $(RULES_DIR)/, $(shell awk -F '<|>' '$$1~/`include/ {print $$2}' $(RULES_DIR)/includes.rule))
CPP_FILES   = $(addprefix $(LIB_DIR)/, $(LIB_SRC)) $(addprefix $(APP_DIR)/, $(APP_SRC))
LDFLAGS     =

USE_CLANG   ?= 0
USE_STD     ?= 1
DEBUG       ?= 0
TEST        ?= 0
GPROF       ?= 0

ifeq ($(USE_CLANG),1)
	CXX = $(CROSS_COMPILE)clang++
	LD  = $(CROSS_COMPILE)ld
	AR  = $(CROSS_COMPILE)ar
else
	CXX = $(CROSS_COMPILE)g++
	LD  = $(CROSS_COMPILE)ld
	AR  = $(CROSS_COMPILE)ar
endif

ifeq ($(USE_STD),1)
	INCDIR += -I$(LIB_DIR)/std
else
	INCDIR += -I$(LIB_DIR)/nostd
endif

CPPFLAGS = -MMD -Wall -fno-rtti -fno-exceptions $(INCDIR)

APP_SRC = \
	asysc/asysc.cpp \
	asysc/mathexpressionex.cpp

LIB_SRC = \
	display.cpp \
	parser.cpp \
	element.cpp \
	elementdatabase.cpp \
	function.cpp \
	mathexpression_core.cpp \
	mathexpression_display.cpp \
	mathexpression_parser.cpp \
	mathexpression_simplify.cpp \
	value.cpp \
	evaluator.cpp \
	test.cpp

ifeq ($(USE_STD),1)
	LIB_SRC += std/lcstring.cpp
else
	LIB_SRC += nostd/lcstring.cpp
endif

ifeq ($(DEBUG),1)
	CPPFLAGS += -g -D_DEBUG
else ifeq ($(GPROF),1)
	CPPFLAGS += -pg
	LDFLAGS  += -pg
else
	CPPFLAGS += -O3
	LDFLAGS  += -s
endif

ifeq ($(TEST),1)
	CPPFLAGS += -D_TEST
endif

all: build
	echo "\nTo run the examples, type \"make run\"\n"

build: $(BIN_DIR)/$(EXE) rules
	$(MAKE) -C examples --no-print-directory

-include $(LIB_OBJS:.o=.d)
-include $(EXE_OBJ:.o=.d)

$(OBJ_DIR)/%.o: $(APP_DIR)/%.cpp
	echo 'Compiling  $(notdir $< )'
	$(CXX) $(CPPFLAGS) -c $< -o $@

$(OBJ_DIR)/%.o: $(LIB_DIR)/%.cpp
	echo 'Compiling  $(notdir $< )'
	$(CXX) $(CPPFLAGS) -c $< -o $@

$(APP_DIR)/Rules_concat.txt: $(RULE_FILES)
	cat $^ > $@

$(OBJ_DIR)/%.ztxt: $(APP_DIR)/%.txt
	cp $< $@
	echo -e '\0' >> $@

$(OBJ_DIR)/%.o: $(OBJ_DIR)/%.ztxt
	echo 'Packaging  $(notdir $< )'
	$(LD) -r -b binary $< -o $@

$(LIB): $(LIB_OBJS)
	echo 'Archiving  $(notdir $@)'
	$(AR) rcs $@ $^

$(BIN_DIR)/$(EXE): $(EXE_OBJ) $(LIB)
	echo 'Linking    $(notdir $@)'
	$(CXX) -o $@ $(LDFLAGS) $(EXE_OBJ) $(LIB)

rules: $(RULE_FILES)
	echo 'Copying    $(notdir $^)'
	cp -r $(RULES_DIR) $(BIN_DIR)

clean:
	@echo 'Cleaning  ...'
	rm -rf $(LIB) $(BIN_DIR) $(OBJ_DIR) $(APP_DIR)/Rules_concat.txt
	$(MAKE) -C examples --no-print-directory clean

run: build
	$(MAKE) -C examples --no-print-directory run

archive:
	mkdir -p archive
	git ls-files -z | xargs -0 zip -q archive/lightcas_`date +%y%m%d`.zip

cppcheck:
	cppcheck --enable=all --suppress=missingIncludeSystem --suppress=noExplicitConstructor $(INCDIR) $(CPP_FILES)

clang-tidy:
	clang-tidy $(CPP_FILES) -- $(INCDIR)

header:
	python3 tools/add_license_headers.py --license LICENSE --style hash examples tools
	python3 tools/add_license_headers.py --license LICENSE --style c app src

pdf:
	asciidoctor-pdf -D doc/build -r asciidoctor-kroki -r asciidoctor-mathematical -a allow-uri-read -a mathematical-format=svg -a pdf-theme=pdf -a pdf-themesdir=doc doc/index.adoc

html:
	asciidoctor -D doc/build -r asciidoctor-kroki -a allow-uri-read doc/index.adoc

.PHONY: all build clean run rules archive cppcheck clang-tidy header pdf html
.SILENT:
