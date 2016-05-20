######################################################################
# Automatically generated by qmake (2.01a) ?? ?? 23 19:29:15 2014
######################################################################

TEMPLATE = lib
TARGET = utilities
INCLUDEPATH += .
INCLUDEPATH += ./include

dir = ..
include($$dir/common.pri)

!LIB_ALL:!LIB_CORE{
	DEFINES += UTILITIES_EXPORTS
	RC_FILE += utilities.rc
}
else{
    CONFIG += staticlib
}

PRECOMPILED_HEADER = stdafx.h


# Input
HEADERS += include/gdialpha.h \
           include/souicoll.h \
           include/trace.h \
           include/snew.h \
           include/utilities-def.h \
           include/utilities.h \
           include/soui_mem_wrapper.h \
           include/atl.mini/atldef.h \
           include/atl.mini/SComCli.h \
           include/atl.mini/SComHelper.h \
           include/pugixml/pugiconfig.hpp \
           include/pugixml/pugixml.hpp \
           include/string/strcpcvt.h \
           include/string/tstring.h \
           include/unknown/obj-ref-i.h \
           include/unknown/obj-ref-impl.hpp \
           include/com-loader.hpp \
           include/wtl.mini/msgcrack.h \
           include/wtl.mini/souimisc.h
           
SOURCES += src/gdialpha.cpp \
           src/trace.cpp \
           src/utilities.cpp \
           src/soui_mem_wrapper.cpp\
           src/pugixml/pugixml.cpp \
           src/string/strcpcvt.cpp \
           src/string/tstring.cpp \
