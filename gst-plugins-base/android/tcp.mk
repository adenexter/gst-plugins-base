LOCAL_PATH:= $(call my-dir)

include $(CLEAR_VARS)

LOCAL_ARM_MODE := arm

tcp_LOCAL_SRC_FILES_BASE:= \
	gst/tcp/gsttcpplugin.c  	\
	gst/tcp/gsttcp.c 			\
	gst/tcp/gstmultifdsink.c 	\
	gst/tcp/gsttcpclientsrc.c 	\
	gst/tcp/gsttcpclientsink.c 	\
	gst/tcp/gsttcpserversrc.c 	\
	gst/tcp/gsttcpserversink.c 	\
	gst/tcp/gsttcp-enumtypes.c 	\
	gst/tcp/gsttcp-marshal.c

LOCAL_SRC_FILES:= $(addprefix ../,$(tcp_LOCAL_SRC_FILES_BASE))

LOCAL_SHARED_LIBRARIES := \
    libgstreamer-0.10       \
    libgstbase-0.10         \
    libglib-2.0             \
    libgthread-2.0          \
    libgmodule-2.0          \
    libgobject-2.0 			\
	libgstdataprotocol-0.10

LOCAL_MODULE:= libgsttcp

LOCAL_CFLAGS := -DHAVE_CONFIG_H  -DGSTREAMER_BUILT_FOR_ANDROID \
	$(GST_PLUGINS_BASE_CFLAGS)
#
# define LOCAL_PRELINK_MODULE to false to not use pre-link map
#
LOCAL_PRELINK_MODULE := false

#It's a gstreamer plugins, and it must be installed on ..../lib/gstreamer-0.10
LOCAL_MODULE_PATH := $(TARGET_OUT)/lib/gstreamer-0.10
LOCAL_MODULE_TAGS := optional

include $(BUILD_SHARED_LIBRARY)
