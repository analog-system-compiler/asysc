

MAKEFLAGS = --jobs 4

SRC_DIR     = ./
LIGHTCAS_DIR = lightcas
RULES_DIR   = $(LIGHTCAS_DIR)/rules
BUILD_DIR      = $(shell mkdir -p ./build) ./build
LIB         = $(LIGHTCAS_DIR)/libLightCAS.a
EXE_OBJ     = $(EXE_SRC:%.cpp=$(BUILD_DIR)/%.o)
INCDIR      = -I$(LIGHTCAS_DIR)/src
EXE         = cirsol

#Compiler settings
CXX         = $(CROSS_COMPILE)g++
#CXX         = $(CROSS_COMPILE)clang++
AR          = $(CROSS_COMPILE)ar
LD          = $(CROSS_COMPILE)ld

#options
USE_STD     = 0
DEBUG       = 0
TEST        = 0
EMBED_RULES = 0

CPPFLAGS  = -MMD -Wall -fno-rtti -fno-exceptions $(INCDIR)
LDFLAGS   = -Wl,-Map=$(EXE).map

EXE_SRC = CirSol.cpp \
	CMathExpressionEx.cpp

ifeq ($(GPROF),1)
	CPPFLAGS += -pg
endif

ifeq ($(USE_STD),0)
	CPPFLAGS += -Ilightcas/src/nostd 
	OBJ_SRC  += nostd/LCString.cpp  
else
	CPPFLAGS += -Ilightcas/src/std
endif

ifeq ($(DEBUG),1)
	CPPFLAGS += -g -D_DEBUG
else
	CPPFLAGS += -Os
	LDFLAGS  += -s
endif

ifeq ($(TEST),1)
	CPPFLAGS += -D_TEST
endif

all: $(BUILD_DIR)/$(EXE) rules

rules: $(RULES_DIR)/*.txt
	echo 'Copying    $(notdir $^)'
	cp $^ $(BUILD_DIR)

-include $(EXE_OBJ:.o=.d)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	echo 'Compiling  $(notdir $< )'
	$(CXX) $(CPPFLAGS) -c $< -o $@

$(LIB): force
	$(MAKE) -C $(LIGHTCAS_DIR) --no-print-directory DEBUG=$(DEBUG) TEST=$(TEST)

$(BUILD_DIR)/$(EXE): $(LIB) $(EXE_OBJ)
	echo 'Linking    $(notdir $@)'
	$(CXX) -o $@ $(LDFLAGS) $(EXE_OBJ) $(LIB)

clean:
	@echo 'Cleaning  ...'
	rm -rf $(EXE) $(BUILD_DIR)
	$(MAKE) -C $(LIGHTCAS_DIR) --no-print-directory clean

.PHONY: all clean force
.SILENT:
#.SECONDARY:
