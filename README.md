# mobile-vapt-scripts

## Apk Extractor

> Tool for extracting apks directly from devices.

**Requirements**

- App downloaded on device
- Device connected through adb
```bash
adb device
```
- `adb` in `PATH`
- ```pip3 install -r requirements.txt```

**Usage**

```bash
./apk-extractor  <output_dir> <package_name>
```