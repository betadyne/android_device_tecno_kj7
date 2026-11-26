#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/tecno/kj7',
    'hardware/google/interfaces',
    'hardware/google/pixel',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/transsion',
    'vendor/mediatek/ims',
]


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('libc++_shared',): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/factory': blob_fixup()
        .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
    'vendor/bin/hw/android.hardware.memtrack-service.mediatek': blob_fixup()
        .replace_needed('android.hardware.memtrack-V1-ndk_platform.so', 'android.hardware.memtrack-V1-ndk.so'),
    'vendor/bin/hw/android.hardware.security.keymint-service.trustonic': blob_fixup()
        .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so', 'android.hardware.security.keymint-V1-ndk.so')
        .replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
        .replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so'),
    (
        'vendor/bin/hw/android.hardware.gnss-service.mediatek',
        'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so',
    ): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    (
        'vendor/lib/hw/face.default.so',
        'vendor/lib64/hw/face.default.so',
    ): blob_fixup()
        .replace_needed('android.hardware.power-V1-ndk_platform.so', 'android.hardware.power-V1-ndk.so'),
    'vendor/lib64/libkeystore-engine-wifi-hidl.so': blob_fixup()
        .replace_needed('android.system.keystore2-V1-ndk_platform.so', 'android.system.keystore2-V1-ndk.so'),
    'vendor/lib64/mt6789/libeffect_hal.so': blob_fixup()
        .remove_needed('libc++_shared.so')
        .add_needed('libc++.so'),
    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v32.so'),
    'vendor/lib64/libnvram.so': blob_fixup()
        .add_needed('libbase-v33.so'),
    (
        'vendor/bin/mnld',
        'vendor/lib/librgbwlightsensor.so',
        'vendor/lib64/librgbwlightsensor.so',
        'vendor/lib/mt6789/libaalservice.so',
        'vendor/lib64/mt6789/libaalservice.so',
        'vendor/lib64/mt6789/libcam.utils.sensorprovider.so',
        'vendor/lib64/mt6789/libmtkcam_3rdparty.customer.so',
    ): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    (
        'vendor/lib/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so',
        'vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so',
    ): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    (
        'vendor/lib64/mt6789/libmtkcam_stdutils.so',
        'vendor/lib64/hw/mt6789/android.hardware.camera.provider@2.6-impl-mediatek.so',
    ): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    (
        'vendor/lib64/hw/hwcomposer.mtk_common.so',
        'vendor/lib64/hw/hwcomposer.mtk_fold.so',
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'kj7',
    'tecno',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
