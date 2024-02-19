#!/bin/bash

# pip 버전 출력
echo "pip version:"
pip --version

# local_lib 폴더 생성 (이미 존재한다면 아무 일도 하지 않음)
mkdir -p local_lib

# path 라이브러리 설치 (이미 존재하는 경우 제거 후 재설치)
python3 -m pip3 install --target=./local_lib --force-reinstall git+https://github.com/jaraco/path.git > install.log 2>&1

# 설치 로그 확인
echo "Installation log saved to install.log"

# 설치된 라이브러리 검사
if pip list --path ./local_lib | grep -q 'path'; then
    echo "path library installed successfully."
    # 파이썬 프로그램 실행
    python my_program.py
else
    echo "path library installation failed. Check install.log for errors."
    exit 1
fi
