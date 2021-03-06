%bcond_with X11

Name:       gst-plugins-base

Summary:    GStreamer streaming media framework base plug-ins
Version:    0.10.36
Release:    1
Group:      Applications/Multimedia
License:    LGPLv2+
URL:        http://gstreamer.freedesktop.org/
Source0:    http://gstreamer.freedesktop.org/src/gst-plugins-base/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(orc-0.4) >= 0.4.5
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gstreamer-0.10) >= 0.10.36
BuildRequires:  pkgconfig(gstreamer-base-0.10)
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
%setup -q -n %{name}-%{version}/%{name}

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
%{_libdir}/libgstinterfaces-0.10.so.*
%{_libdir}/libgstaudio-0.10.so.*
%{_libdir}/libgstcdda-0.10.so.*
%{_libdir}/libgstfft-0.10.so.*
%{_libdir}/libgstriff-0.10.so.*
%{_libdir}/libgsttag-0.10.so.*
%{_libdir}/libgstnetbuffer-0.10.so.*
%{_libdir}/libgstrtp-0.10.so.*
%{_libdir}/libgstvideo-0.10.so.*
%{_libdir}/libgstpbutils-0.10.so.*
%{_libdir}/libgstrtsp-0.10.so.*
%{_libdir}/libgstsdp-0.10.so.*
%{_libdir}/libgstapp-0.10.so.*
# base plugins without external dependencies
%{_libdir}/gstreamer-0.10/libgstadder.so
%{_libdir}/gstreamer-0.10/libgstaudioconvert.so
%{_libdir}/gstreamer-0.10/libgstaudiotestsrc.so
%{_libdir}/gstreamer-0.10/libgstffmpegcolorspace.so
%{_libdir}/gstreamer-0.10/libgstdecodebin.so
%{_libdir}/gstreamer-0.10/libgstdecodebin2.so
%{_libdir}/gstreamer-0.10/libgstplaybin.so
%{_libdir}/gstreamer-0.10/libgsttypefindfunctions.so
%{_libdir}/gstreamer-0.10/libgstvideotestsrc.so
%{_libdir}/gstreamer-0.10/libgstaudiorate.so
%{_libdir}/gstreamer-0.10/libgstsubparse.so
%{_libdir}/gstreamer-0.10/libgstvolume.so
%{_libdir}/gstreamer-0.10/libgstvideorate.so
%{_libdir}/gstreamer-0.10/libgstvideoscale.so
%{_libdir}/gstreamer-0.10/libgsttcp.so
%{_libdir}/gstreamer-0.10/libgstaudioresample.so
%{_libdir}/gstreamer-0.10/libgstgdp.so
%{_libdir}/gstreamer-0.10/libgstapp.so
%{_libdir}/gstreamer-0.10/libgstencodebin.so
# base plugins with dependencies
%{_libdir}/gstreamer-0.10/libgstalsa.so
%{_libdir}/gstreamer-0.10/libgstogg.so
%if %{with X11}
%{_libdir}/gstreamer-0.10/libgstxvimagesink.so
%{_libdir}/gstreamer-0.10/libgstlibvisual.so
%{_libdir}/gstreamer-0.10/libgstpango.so
%{_libdir}/gstreamer-0.10/libgstximagesink.so
%endif
%{_libdir}/gstreamer-0.10/libgsttheora.so
%{_libdir}/gstreamer-0.10/libgstvorbis.so
#%{_libdir}/gstreamer-0.10/libgstgnomevfs.so
%{_libdir}/gstreamer-0.10/libgstgio.so

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/gstreamer-0.10/gst/app
%{_includedir}/gstreamer-0.10/gst/audio/gstaudiodecoder.h
%{_includedir}/gstreamer-0.10/gst/audio/gstaudioencoder.h
%{_includedir}/gstreamer-0.10/gst/audio/gstaudioiec61937.h
%{_includedir}/gstreamer-0.10/gst/tag/gsttagmux.h
%{_includedir}/gstreamer-0.10/gst/video/video-overlay-composition.h
%doc %{_datadir}/gst-plugins-base/license-translations.dict
%{_includedir}/gstreamer-0.10/gst/app/gstappbuffer.h
%{_includedir}/gstreamer-0.10/gst/app/gstappsink.h
%{_includedir}/gstreamer-0.10/gst/app/gstappsrc.h
%dir %{_includedir}/gstreamer-0.10/gst/audio
%{_includedir}/gstreamer-0.10/gst/audio/audio.h
%{_includedir}/gstreamer-0.10/gst/audio/audio-enumtypes.h
%{_includedir}/gstreamer-0.10/gst/audio/gstaudioclock.h
%{_includedir}/gstreamer-0.10/gst/audio/gstaudiofilter.h
%{_includedir}/gstreamer-0.10/gst/audio/gstaudiosink.h
%{_includedir}/gstreamer-0.10/gst/audio/gstaudiosrc.h
%{_includedir}/gstreamer-0.10/gst/audio/gstbaseaudiosink.h
%{_includedir}/gstreamer-0.10/gst/audio/gstbaseaudiosrc.h
%{_includedir}/gstreamer-0.10/gst/audio/gstringbuffer.h
%{_includedir}/gstreamer-0.10/gst/audio/mixerutils.h
%{_includedir}/gstreamer-0.10/gst/audio/multichannel.h
%dir %{_includedir}/gstreamer-0.10/gst/cdda
%{_includedir}/gstreamer-0.10/gst/cdda/gstcddabasesrc.h
%dir %{_includedir}/gstreamer-0.10/gst/floatcast
%{_includedir}/gstreamer-0.10/gst/floatcast/floatcast.h
%dir %{_includedir}/gstreamer-0.10/gst/fft
%{_includedir}/gstreamer-0.10/gst/fft/gstfft*.h
%dir %{_includedir}/gstreamer-0.10/gst/interfaces
%{_includedir}/gstreamer-0.10/gst/interfaces/colorbalance.h
%{_includedir}/gstreamer-0.10/gst/interfaces/colorbalancechannel.h
%{_includedir}/gstreamer-0.10/gst/interfaces/interfaces-enumtypes.h
%{_includedir}/gstreamer-0.10/gst/interfaces/mixer.h
%{_includedir}/gstreamer-0.10/gst/interfaces/mixeroptions.h
%{_includedir}/gstreamer-0.10/gst/interfaces/mixertrack.h
%{_includedir}/gstreamer-0.10/gst/interfaces/navigation.h
%{_includedir}/gstreamer-0.10/gst/interfaces/propertyprobe.h
%{_includedir}/gstreamer-0.10/gst/interfaces/tuner.h
%{_includedir}/gstreamer-0.10/gst/interfaces/tunerchannel.h
%{_includedir}/gstreamer-0.10/gst/interfaces/tunernorm.h
%{_includedir}/gstreamer-0.10/gst/interfaces/videoorientation.h
%{_includedir}/gstreamer-0.10/gst/interfaces/xoverlay.h
%{_includedir}/gstreamer-0.10/gst/interfaces/streamvolume.h
%dir %{_includedir}/gstreamer-0.10/gst/netbuffer
%{_includedir}/gstreamer-0.10/gst/netbuffer/gstnetbuffer.h
%dir %{_includedir}/gstreamer-0.10/gst/pbutils
%{_includedir}/gstreamer-0.10/gst/pbutils/codec-utils.h
%{_includedir}/gstreamer-0.10/gst/pbutils/descriptions.h
%{_includedir}/gstreamer-0.10/gst/pbutils/gstdiscoverer.h
%{_includedir}/gstreamer-0.10/gst/pbutils/gstpluginsbaseversion.h
%{_includedir}/gstreamer-0.10/gst/pbutils/install-plugins.h
%{_includedir}/gstreamer-0.10/gst/pbutils/missing-plugins.h
%{_includedir}/gstreamer-0.10/gst/pbutils/pbutils.h
%{_includedir}/gstreamer-0.10/gst/pbutils/pbutils-enumtypes.h
%{_includedir}/gstreamer-0.10/gst/pbutils/encoding-profile.h
%{_includedir}/gstreamer-0.10/gst/pbutils/encoding-target.h

%dir %{_includedir}/gstreamer-0.10/gst/riff
%{_includedir}/gstreamer-0.10/gst/riff/riff-ids.h
%{_includedir}/gstreamer-0.10/gst/riff/riff-media.h
%{_includedir}/gstreamer-0.10/gst/riff/riff-read.h
%dir %{_includedir}/gstreamer-0.10/gst/rtp
%{_includedir}/gstreamer-0.10/gst/rtp/gstbasertpaudiopayload.h
%{_includedir}/gstreamer-0.10/gst/rtp/gstbasertpdepayload.h
%{_includedir}/gstreamer-0.10/gst/rtp/gstbasertppayload.h
%{_includedir}/gstreamer-0.10/gst/rtp/gstrtcpbuffer.h
%{_includedir}/gstreamer-0.10/gst/rtp/gstrtpbuffer.h
%{_includedir}/gstreamer-0.10/gst/rtp/gstrtppayloads.h
%dir %{_includedir}/gstreamer-0.10/gst/rtsp
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtsp-enumtypes.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtspbase64.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtspconnection.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtspdefs.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtspextension.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtspmessage.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtsprange.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtsptransport.h
%{_includedir}/gstreamer-0.10/gst/rtsp/gstrtspurl.h
%dir %{_includedir}/gstreamer-0.10/gst/sdp/
%{_includedir}/gstreamer-0.10/gst/sdp/gstsdp.h
%{_includedir}/gstreamer-0.10/gst/sdp/gstsdpmessage.h
%dir %{_includedir}/gstreamer-0.10/gst/tag
%{_includedir}/gstreamer-0.10/gst/tag/tag.h
%{_includedir}/gstreamer-0.10/gst/tag/gsttagdemux.h
%{_includedir}/gstreamer-0.10/gst/tag/xmpwriter.h
%dir %{_includedir}/gstreamer-0.10/gst/video
%{_includedir}/gstreamer-0.10/gst/video/gstvideofilter.h
%{_includedir}/gstreamer-0.10/gst/video/gstvideosink.h
%{_includedir}/gstreamer-0.10/gst/video/video.h
%{_includedir}/gstreamer-0.10/gst/video/video-enumtypes.h
%{_libdir}/libgstaudio-0.10.so
%{_libdir}/libgstinterfaces-0.10.so
%{_libdir}/libgstnetbuffer-0.10.so
%{_libdir}/libgstriff-0.10.so
%{_libdir}/libgstrtp-0.10.so
%{_libdir}/libgsttag-0.10.so
%{_libdir}/libgstvideo-0.10.so
%{_libdir}/libgstcdda-0.10.so
%{_libdir}/libgstpbutils-0.10.so
%{_libdir}/libgstrtsp-0.10.so
%{_libdir}/libgstsdp-0.10.so
%{_libdir}/libgstfft-0.10.so
%{_libdir}/libgstapp-0.10.so
# pkg-config files
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root,-)
# helper programs
%{_bindir}/gst-visualise-0.10
%{_bindir}/gst-discoverer-0.10
%{_mandir}/man1/gst-visualise-0.10*

# %files doc
# %defattr(-,root,root,-)
# gtk-doc documentation
# %doc %{_datadir}/gtk-doc/html/gst-plugins-base-libs-0.10
# %doc %{_datadir}/gtk-doc/html/gst-plugins-base-plugins-0.10
