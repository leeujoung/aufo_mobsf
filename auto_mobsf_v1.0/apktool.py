##암호화된 파일 clssess+넘버.dex 로 저장
##서명기능 추가  , 복호화 파일 경로 동적경로로 변경
##디컴파일 파일명 동적경로로 변경

import os
import subprocess
import decrypt_dex


APKTOOL_PATH = 'apktool'
DEX_MAGIC_NUMBER = b'dex\n035\0'

def run_command(command):
    """시스템 명령어를 실행하고 출력을 실시간으로 처리합니다."""
    print(f"Executing: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        for line in process.stdout:
            print(line, end='')  # 실시간 출력
        process.wait()  # 명령어가 완료될 때까지 대기

        if process.returncode != 0:
            print(f"Error: {process.stderr.read()}")
            raise Exception(f"Command failed: {command}\nError: {process.stderr.read()}")
    except KeyboardInterrupt:
        process.kill()
        print("\nExecution was interrupted by the user.")

def decompile_apk(apk_path):
    """APK 파일을 디컴파일합니다."""

    
     # APK 파일이 위치한 디렉토리 경로를 가져와 출력 디렉토리 설정
    base_name = os.path.basename(apk_path).replace('.apk', '')
    output_dir = os.path.join(os.path.dirname(apk_path), f'{base_name}_decompiled')  # 디컴파일 폴더 이름 동적 설정
    

    if os.path.exists(output_dir):
        print(f"Output directory '{output_dir}' already exists. Removing it...")
        subprocess.run(f"rmdir /s /q \"{output_dir}\"", shell=True)

    print("APK 디컴파일 중...")
    run_command(f"{APKTOOL_PATH} d \"{apk_path}\" -o \"{output_dir}\" -f -s")
    return output_dir

def repackage_apk(decompiled_dir, apk_path):
    """디컴파일된 파일을 리패키징합니다."""
    # APK 파일 이름에 "_repack"을 추가하여 새로운 APK 경로 설정
    repackaged_apk_path = os.path.join(os.path.dirname(apk_path), os.path.basename(apk_path).replace('.apk', '_repack.apk'))
    
    print("APK 리패키징 중...")
    run_command(f"{APKTOOL_PATH} b \"{decompiled_dir}\" -o \"{repackaged_apk_path}\"")
    print(f"Repackaged APK created at: {repackaged_apk_path}")

    return repackaged_apk_path

def sign_apk(apk_path, keystore_path, alias, keystore_password):
    """APK 파일에 서명합니다."""
    print("APK 서명 중...")
    run_command(
        f"jarsigner -keystore \"{keystore_path}\" -storepass {keystore_password} "
        f"\"{apk_path}\" {alias}"
    )
    print(f"APK signed: {apk_path}")
          

def main():
    apk_path = input("디컴파일할 APK 파일의 경로를 입력하세요: ")  # 사용자로부터 APK 경로 입력 받기

    # APK 디컴파일
    decompiled_dir = decompile_apk(apk_path)
    
    # 복호화 경로
    directory_path = decompiled_dir  
    # DEX 파일들이 있는 디렉토리 경로
    key = 'dbcdcfghijklmaop'  # AES 키
    decrypt_dex.process_directory(directory_path, key)
    
    
    
    # 디컴파일된 파일을 리패키징
    repackaged_apk_path = repackage_apk(decompiled_dir, apk_path)

    # APK 파일 서명
    keystore_path = 'my-release-key.jks'  # 서명 키 경로
    alias = 'my-alias'  # 키스토어 별칭
    keystore_password = '000000'  # 키스토어 비밀번호
    sign_apk(repackaged_apk_path, keystore_path, alias, keystore_password)

    return repackaged_apk_path

if __name__ == '__main__':
    repackaged_apk_path = main()
    print("디컴파일, 리패키징 및 서명 완료!")
    print(f"리패키징된 파일 경로: {repackaged_apk_path}")

