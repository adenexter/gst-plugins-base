%bcond_with X11

Name:       gst-plugins-base1.0

Summary:    GStreamer streaming media framework base plug-ins
Version:    1.4.0
Release:    1
Group:      Applications/Multimedia
License:    LGPLv2+
URL:        http://gstreamer.freedesktop.org/
Source0:    http://gstreamer.freedesktop.org/src/gst-plugins-base/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(orc-0.4) >= 0.4.18
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.4.0
%if %{with X11}
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(libvisual-0.4)
%endif
BuildRequires:  gettext
BuildRequires:  cvs
BuildRequires:  python

%description
A well-groomed and well-maintained collection of GStreamer plug-ins and elements, 
spanning the range of possible types of elements one would want to write for GStreamer.


%package devel
Summary:    Development tools for GStreamer base plugins
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Separate sub-package for development based on gstreamer base plugins. 


%package tools
Summary:    Gstreamer base plugins utilities
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description tools
Separate sub-package contaning helper applications of gstreamer base plugins.


#%package doc
#Summary:    API reference for Gstreamer base plugins
#Group:      Documentation
#Requires:   %{name} = %{version}-%{release}
#
#%description doc
#Separate documentation sub-package for gstreamer base plugins.



%prep
%setup -q -n %{name}-%{version}/gst-plugins-base

%build
export NOCONFIGURE=1

%autogen --disable-static
%configure --disable-static \
    --with-package-name='Mer GStreamer Base Plugins package' \
    --with-package-origin='http://www.merproject.org/' \
    --enable-experimental \
    --enable-gtk-doc=no \
    --disable-freetypetest \
    --disable-nls \
    --enable-orc \
%if %{without X11}
    --disable-x \
    --disable-xvideo \
    --disable-libvisual \
    --disable-pango \
%endif
%ifarch %{ix86}
    --with-audioresample-format=float \
%endif
%ifarch armv7el armv7tel armv7l armv7hl armv7nhl
    --with-audioresample-format=float \
%endif
%ifarch armv6l armv6hl
    --with-audioresample-format=float \
%endif
%ifarch armv5el armv5tel armv5tejl
    --with-audioresample-format=int \
%endif
    --enable-introspection=no

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README REQUIREMENTS
%{_libdir}/libgstaudio-1.0.so.*
%{_libdir}/libgstfft-1.0.so.*
%{_libdir}/libgstriff-1.0.so.*
%{_libdir}/libgsttag-1.0.so.*
%{_libdir}/libgstrtp-1.0.so.*
%{_libdir}/libgstvideo-1.0.so.*
%{_libdir}/libgstpbutils-1.0.so.*
%{_libdir}/libgstrtsp-1.0.so.*
%{_libdir}/libgstsdp-1.0.so.*
%{_libdir}/libgstapp-1.0.so.*
%{_libdir}/libgstallocators-1.0.so.*
# base plugins without external dependencies
%{_libdir}/gstreamer-1.0/libgstadder.so
%{_libdir}/gstreamer-1.0/libgstaudioconvert.so
%{_libdir}/gstreamer-1.0/libgstaudiotestsrc.so
%{_libdir}/gstreamer-1.0/libgsttypefindfunctions.so
%{_libdir}/gstreamer-1.0/libgstvideotestsrc.so
%{_libdir}/gstreamer-1.0/libgstaudiorate.so
%{_libdir}/gstreamer-1.0/libgstsubparse.so
%{_libdir}/gstreamer-1.0/libgstvolume.so
%{_libdir}/gstreamer-1.0/libgstvideoconvert.so
%{_libdir}/gstreamer-1.0/libgstvideorate.so
%{_libdir}/gstreamer-1.0/libgstvideoscale.so
%{_libdir}/gstreamer-1.0/libgsttcp.so
%{_libdir}/gstreamer-1.0/libgstaudioresample.so
%{_libdir}/gstreamer-1.0/libgstapp.so
%{_libdir}/gstreamer-1.0/libgstencodebin.so
%{_libdir}/gstreamer-1.0/libgstplayback.so
# base plugins with dependencies
%{_libdir}/gstreamer-1.0/libgstalsa.so
%{_libdir}/gstreamer-1.0/libgstogg.so
%if %{with X11}
%{_libdir}/gstreamer-1.0/libgstxvimagesink.so
%{_libdir}/gstreamer-1.0/libgstlibvisual.so
%{_libdir}/gstreamer-1.0/libgstpango.so
%{_libdir}/gstreamer-1.0/libgstximagesink.so
%endif
%{_libdir}/gstreamer-1.0/libgsttheora.so
%{_libdir}/gstreamer-1.0/libgstvorbis.so
#%{_libdir}/gstreamer-1.0/libgstgnomevfs.so
%{_libdir}/gstreamer-1.0/libgstgio.so

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/gstreamer-1.0/gst/app
%dir %{_includedir}/gstreamer-1.0/gst/allocators
%{_includedir}/gstreamer-1.0/gst/allocators/allocators.h
%{_includedir}/gstreamer-1.0/gst/allocators/gstdmabuf.h
%{_includedir}/gstreamer-1.0/gst/audio/audio-channels.h
%{_includedir}/gstreamer-1.0/gst/audio/audio-format.h
%{_includedir}/gstreamer-1.0/gst/audio/audio-info.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiodecoder.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudioencoder.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudioiec61937.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiobasesink.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiobasesrc.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiocdsrc.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiometa.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudioringbuffer.h
%{_includedir}/gstreamer-1.0/gst/audio/streamvolume.h
%{_includedir}/gstreamer-1.0/gst/tag/gsttagmux.h
%{_includedir}/gstreamer-1.0/gst/video/video-overlay-composition.h
%doc %{_datadir}/gst-plugins-base/1.0/license-translations.dict
%{_includedir}/gstreamer-1.0/gst/app/app.h
%{_includedir}/gstreamer-1.0/gst/app/gstappsink.h
%{_includedir}/gstreamer-1.0/gst/app/gstappsrc.h
%dir %{_includedir}/gstreamer-1.0/gst/audio
%{_includedir}/gstreamer-1.0/gst/audio/audio.h
%{_includedir}/gstreamer-1.0/gst/audio/audio-enumtypes.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudioclock.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiofilter.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiosink.h
%{_includedir}/gstreamer-1.0/gst/audio/gstaudiosrc.h
%dir %{_includedir}/gstreamer-1.0/gst/fft
%{_includedir}/gstreamer-1.0/gst/fft/fft.h
%{_includedir}/gstreamer-1.0/gst/fft/gstfft*.h
%dir %{_includedir}/gstreamer-1.0/gst/pbutils
%{_includedir}/gstreamer-1.0/gst/pbutils/codec-utils.h
%{_includedir}/gstreamer-1.0/gst/pbutils/descriptions.h
%{_includedir}/gstreamer-1.0/gst/pbutils/gstdiscoverer.h
%{_includedir}/gstreamer-1.0/gst/pbutils/gstpluginsbaseversion.h
%{_includedir}/gstreamer-1.0/gst/pbutils/install-plugins.h
%{_includedir}/gstreamer-1.0/gst/pbutils/missing-plugins.h
%{_includedir}/gstreamer-1.0/gst/pbutils/pbutils.h
%{_includedir}/gstreamer-1.0/gst/pbutils/pbutils-enumtypes.h
%{_includedir}/gstreamer-1.0/gst/pbutils/encoding-profile.h
%{_includedir}/gstreamer-1.0/gst/pbutils/encoding-target.h

%dir %{_includedir}/gstreamer-1.0/gst/riff
%{_includedir}/gstreamer-1.0/gst/riff/riff.h
%{_includedir}/gstreamer-1.0/gst/riff/riff-ids.h
%{_includedir}/gstreamer-1.0/gst/riff/riff-media.h
%{_includedir}/gstreamer-1.0/gst/riff/riff-read.h
%dir %{_includedir}/gstreamer-1.0/gst/rtp
%{_includedir}/gstreamer-1.0/gst/rtp/gstrtpbaseaudiopayload.h
%{_includedir}/gstreamer-1.0/gst/rtp/gstrtpbasedepayload.h
%{_includedir}/gstreamer-1.0/gst/rtp/gstrtpbasepayload.h
%{_includedir}/gstreamer-1.0/gst/rtp/gstrtphdrext.h
%{_includedir}/gstreamer-1.0/gst/rtp/gstrtcpbuffer.h
%{_includedir}/gstreamer-1.0/gst/rtp/gstrtpbuffer.h
%{_includedir}/gstreamer-1.0/gst/rtp/gstrtppayloads.h
%{_includedir}/gstreamer-1.0/gst/rtp/rtp.h
%dir %{_includedir}/gstreamer-1.0/gst/rtsp
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtsp.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtsp-enumtypes.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtspconnection.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtspdefs.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtspextension.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtspmessage.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtsprange.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtsptransport.h
%{_includedir}/gstreamer-1.0/gst/rtsp/gstrtspurl.h
%{_includedir}/gstreamer-1.0/gst/rtsp/rtsp.h
%dir %{_includedir}/gstreamer-1.0/gst/sdp/
%{_includedir}/gstreamer-1.0/gst/sdp/gstsdp.h
%{_includedir}/gstreamer-1.0/gst/sdp/gstsdpmessage.h
%{_includedir}/gstreamer-1.0/gst/sdp/gstmikey.h
%{_includedir}/gstreamer-1.0/gst/sdp/sdp.h
%dir %{_includedir}/gstreamer-1.0/gst/tag
%{_includedir}/gstreamer-1.0/gst/tag/tag.h
%{_includedir}/gstreamer-1.0/gst/tag/gsttagdemux.h
%{_includedir}/gstreamer-1.0/gst/tag/xmpwriter.h
%dir %{_includedir}/gstreamer-1.0/gst/video
%{_includedir}/gstreamer-1.0/gst/video/colorbalance.h
%{_includedir}/gstreamer-1.0/gst/video/colorbalancechannel.h
%{_includedir}/gstreamer-1.0/gst/video/gstvideodecoder.h
%{_includedir}/gstreamer-1.0/gst/video/gstvideoencoder.h
%{_includedir}/gstreamer-1.0/gst/video/gstvideofilter.h
%{_includedir}/gstreamer-1.0/gst/video/gstvideometa.h
%{_includedir}/gstreamer-1.0/gst/video/gstvideopool.h
%{_includedir}/gstreamer-1.0/gst/video/gstvideosink.h
%{_includedir}/gstreamer-1.0/gst/video/gstvideoutils.h
%{_includedir}/gstreamer-1.0/gst/video/navigation.h
%{_includedir}/gstreamer-1.0/gst/video/video.h
%{_includedir}/gstreamer-1.0/gst/video/video-blend.h
%{_includedir}/gstreamer-1.0/gst/video/video-chroma.h
%{_includedir}/gstreamer-1.0/gst/video/video-color.h
%{_includedir}/gstreamer-1.0/gst/video/video-event.h
%{_includedir}/gstreamer-1.0/gst/video/video-format.h
%{_includedir}/gstreamer-1.0/gst/video/video-frame.h
%{_includedir}/gstreamer-1.0/gst/video/video-info.h
%{_includedir}/gstreamer-1.0/gst/video/video-enumtypes.h
%{_includedir}/gstreamer-1.0/gst/video/video-tile.h
%{_includedir}/gstreamer-1.0/gst/video/videoorientation.h
%{_includedir}/gstreamer-1.0/gst/video/videooverlay.h
%{_libdir}/libgstaudio-1.0.so
%{_libdir}/libgstriff-1.0.so
%{_libdir}/libgstrtp-1.0.so
%{_libdir}/libgsttag-1.0.so
%{_libdir}/libgstvideo-1.0.so
%{_libdir}/libgstpbutils-1.0.so
%{_libdir}/libgstrtsp-1.0.so
%{_libdir}/libgstsdp-1.0.so
%{_libdir}/libgstfft-1.0.so
%{_libdir}/libgstapp-1.0.so
%{_libdir}/libgstallocators-1.0.so
# pkg-config files
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root,-)
# helper programs
%{_bindir}/gst-play-1.0
%{_bindir}/gst-discoverer-1.0
%{_bindir}/gst-device-monitor-1.0
%{_datadir}/man/man1/gst-discoverer-1.*.gz
%{_datadir}/man/man1/gst-device-monitor-1.*.gz
%{_datadir}/man/man1/gst-play-1.*.gz

# %files doc
# %defattr(-,root,root,-)
# gtk-doc documentation
# %doc %{_datadir}/gtk-doc/html/gst-plugins-base-libs-1.0
# %doc %{_datadir}/gtk-doc/html/gst-plugins-base-plugins-1.0
