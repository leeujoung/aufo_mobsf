##암호화된 파일 clssess+넘버.dex 로 저장

import os
from Crypto.Cipher import AES


##매직넘버 사용하여 암호화 되어있는 dex 파일 구분 
def is_encrypted(target_file):
    with open(target_file, 'rb') as tf:
        magic_num = tf.read(8)
        if magic_num == b'\x64\x65\x78\x0A\x30\x33\x35\x00': 
            return False
        return True


#AES-128/ECB 모드를 사용하여 파일의 내용을 복호화
def decrypt_aes_ecb(file_path, key):
    key_bytes = key.encode()  # 키를 바이트로 변환

    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    cipher = AES.new(key_bytes, AES.MODE_ECB)  # AES ECB 모드로 암호화 객체 생성
    decrypted_data = cipher.decrypt(encrypted_data)  # 복호화 수행
    return decrypted_data


def get_next_available_filename(directory, base_name="classes", extension=".dex"):
    """
    디렉토리 내에서 사용할 수 있는 다음 파일 이름을 찾습니다.
    예를 들어 classes.dex, classes2.dex와 같은 형식으로 이름을 지정합니다.
    """
    index = 1
    while True:
        # classes.dex부터 시작하여 차례대로 파일 존재 여부를 확인합니다.
        new_filename = f"{base_name}{index if index > 1 else ''}{extension}"
        if not os.path.exists(os.path.join(directory, new_filename)):
            return new_filename  # 존재하지 않는 파일명을 찾으면 반환합니다.
        index += 1  # 다음 번호를 확인합니다.



def process_directory(directory_path, key):
    """
    주어진 디렉토리 내의 모든 DEX 파일을 검사하고, 암호화된 파일을 복호화합니다.
    복호화된 파일은 새로운 이름으로 저장하고 원본 파일은 삭제합니다.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith('.dex'):  # .dex 확장자를 가진 파일만 처리합니다.
            file_path = os.path.join(directory_path, filename)  # 파일의 전체 경로를 생성합니다.
            if is_encrypted(file_path):  # 파일이 암호화되었는지 확인합니다.
                print(f"{file_path} is encrypted. Attempting to decrypt...")
                try:
                    decrypted_data = decrypt_aes_ecb(file_path, key)  # 복호화를 시도합니다.
                    print("복호화 성공.")

                    # 새로운 파일 이름을 생성합니다.
                    new_filename = get_next_available_filename(directory_path)
                    new_file_path = os.path.join(directory_path, new_filename)

                    # 복호화된 데이터를 새로운 파일에 저장합니다.
                    with open(new_file_path, 'wb') as f:
                        f.write(decrypted_data)
                    print(f"Decrypted data written to {new_file_path}.")

                    # # 원본 암호화 파일을 삭제합니다.
                    # os.remove(file_path)
                    # print(f"Original encrypted file {file_path} deleted.")
                
                except Exception as e:
                    print(f"Decryption failed for {file_path}: {e}")
            else:
                print(f"{file_path} is not encrypted.")
