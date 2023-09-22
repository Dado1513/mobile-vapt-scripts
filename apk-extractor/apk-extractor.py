#!/usr/bin/env python3
import os
import sys
import rich
from loguru import logger
import subprocess


if __name__=="__main__":
    if len(sys.argv) > 2:
        pacakge_name = sys.argv[2]
        output_dir = sys.argv[1]
        os.makedirs(output_dir, exist_ok=True)
        output = subprocess.check_output(["adb", "shell", "pm","path", pacakge_name]).decode('utf-8').strip()
        list_apk = output.split("\n")
        for apk in list_apk:
            path = apk.split("package:")[1]
            output_downloaded_app = subprocess.call(["adb","pull",path, output_dir], stdout=os.devnull, stderr=os.devnull)
            logger.info(f"Downloading app {apk}")
    else:
        logger.error("Error. Usage:")
        logger.error("./apk-extractor.py <package_name> <output_dir>")
    