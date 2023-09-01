# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device ginkgo
%define vendor xiaomi

%define vendor_pretty XIAOMI
%define device_pretty REDMI NOTE 8

%define installable_zip 1
%define droid_target_aarch64 1
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}
%define straggler_files \
/acct \
/apex \
/boot \
/bt_firmware \
/bugreports \
/cache \
/config \
/d \
/data \
/data_mirror \
/debug_ramdisk \
/default.prop \
/etc \
/firmware \
/img \
/init-debug \
/init.environ.rc \
/init.recovery.qcom.rc \
/lib \
/linkerconfig \
/metadata \
/mnt \
/odm \
/oem \
/postinstall \
/product \
/sbin \
/sdcard \
/storage \
/system \
/system_ext \
/usr \
/vendor \
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

