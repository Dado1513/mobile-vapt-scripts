#!/usr/bin/env python3
import os
import sys
import rich
from loguru import logger
import subprocess
from pathlib import Path




if __name__=="__main__":
    if len(sys.argv) > 2:
        package_name = sys.argv[2]
        output_dir = sys.argv[1]
        os.makedirs(output_dir, exist_ok=True)
        output = subprocess.check_output(["adb", "shell", "pm","path", package_name]).decode('utf-8').strip()
        list_apk = output.split("\n")
        for apk in list_apk:
            path = apk.split("package:")[1]
            output_downloaded_app = os.system(f"adb pull {path} {output_dir}")
            logger.info(f"Downloading app {apk}")
    else:
        logger.error("Error. Usage:")
        logger.error("./apk-extractor.py  <output_dir> <package_name>")
    

