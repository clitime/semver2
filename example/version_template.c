#include "version.h"


static const char firmware_version[] = "{{SEMVER}}";
static const char full_version[] = "{{SEMVER}} ({{HASH_DATA}})";
static const char device_name[]  = "test_device";


char *getFirmVersion() {
    return firmware_version;
}

char *getDeviceName() {
    return device_name;
}
