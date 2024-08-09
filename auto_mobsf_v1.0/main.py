#API 자동화 코드
#복호화 연결
# PDF 리포트 다운로드

import json
import os
import requests
import apktool  # apktool 모듈 임포트
from requests_toolbelt.multipart.encoder import MultipartEncoder
from datetime import datetime
# import subprocess
# from datetime import datetime

SERVER = "http://127.0.0.1:8000"
APIKEY = 'b79304d47697bd2981edc5d98a95516c268582493d71b864057c04d637dbe12a'




#업로드 API_Static Analysis
def upload(path):
    """Upload File"""
    print("Uploading file")
    multipart_data = MultipartEncoder(fields={'file': (path, open(path, 'rb'), 'application/octet-stream')})
    headers = {'Content-Type': multipart_data.content_type, 'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/upload', data=multipart_data, headers=headers)
    # print(f"Upload Reponse:{response.json()}")
    print("업로드완료")
    return response.json()



#mobsf 인증서 설치 
def install_root_ca():
    """MobSF Root CA 설치"""
    print("MobSF Root CA를 설치합니다.")
    
    headers = {'Authorization': APIKEY}
    data = {'action': 'install'}
    response = requests.post(f'{SERVER}/api/v1/android/root_ca', data=data, headers=headers)
    


#for Static Analysis
def scan(data):
    """Scan the file"""
    print("파일 스캔중")
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/scan', data=data, headers=headers)
    # print(f"Scan Reponse:{response.json()}")
    return data["hash"]



# PDF 리포트 다운로드
def pdf(hash):
    headers = {'Authorization': APIKEY}
    data = {"hash": hash}

    response = requests.post(SERVER + '/api/v1/download_pdf', data=data, headers=headers, stream=True)

    save_dir = 'reports'  # 디렉토리로 변경
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # "YYYYMMDD_HHMMSS" 형식
    filename = f"report_{timestamp}.pdf"
    file_path = os.path.join(save_dir, filename)

    with open(file_path, 'wb') as flip:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                flip.write(chunk)

    print(f"리포트 저장됨: {file_path}")



#JSON API
def json_resp(hash):
    """Generate JSON Report"""
    print("Generate JSON report")
    headers = {'Authorization': APIKEY}
    data = {"hash": hash}
    response = requests.post(SERVER + '/api/v1/report_json', data=data, headers=headers)
    # print(f"Static Analysis JSON Report:{response.json()}")



########동적검사#############


#get app
def get():
    """get app"""
    print("Getting apps")
    headers = {'Authorization': APIKEY}
    response = requests.get(SERVER + '/api/v1/dynamic/get_apps', headers=headers)
    apps = response.json()
    
    if apps and 'apps' in apps and len(apps['apps']) > 0:
        print(f"app list")
    else:
        print("No apps found to start dynamic analysis.")



#start Activity
def start_activity(hash, activity):
    """Start Activity or Exported Activity"""
    print(f"Starting activity: {activity}")

    headers = {'Authorization': APIKEY}
    data = {
        "hash": hash,
        "activity": activity
    }
    response = requests.post(SERVER + '/api/v1/android/start_activity', data=data, headers=headers)
    



#start Activity_tester
def activity_tester(hash, test_type):
    """Test Activity or Exported Activity"""
    print(f"Testing {test_type} activities")

    headers = {'Authorization': APIKEY}
    data = {
        "hash": hash,
        "test": test_type
    }
    response = requests.post(SERVER + '/api/v1/android/activity', data=data, headers=headers)
    
    if response.status_code == 200:
        print("활동 테스트 성공")
        print("Response:", response.json())
    else:
        print("활동 테스트 중 오류 발생")
        print("Error:", response.json())
    
    return response



## 동적검사 
def start_dynamic(hash):
    """start dynamic Analysis"""
    print("Starting Dynamic Analysis")

    try:
        data = {"hash": hash}
        headers = {'Authorization': APIKEY}
        response = requests.post(SERVER + '/api/v1/dynamic/start_analysis', data=data, headers=headers)
        # response = frida_instrument(hash)
    except requests.exceptions.RequestException as err:
        print(f"start dynamic analysis error: {err}\nStarting Frida Hooking")
        response = frida_instrument(hash)
        start_dynamic(response)

   # stop_dynamic(hash)


def tls_ssl(hash):
    """TLS/SSl Security"""
    print("Testing TLS/SSL Security")
    data = {"hash": hash}
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/android/tls_tests', data=data, headers=headers)
    # print(f"TLS/SSL Security Test Response:{response.json()}")
    print("Testing TLS/SSL Security 완료")


def mobsfy(hash):
    """MobSFy Android Runtime Environment"""
    print("Preparing MobSF Android Runtime")
    data = {"hash": hash}
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/android/mobsfy', data=data, headers=headers)
    print(f"MobSFy Android Runtime Environment 완료")



# Frida Get Runtime Dependencies
def get_dependencies(hash):
    """Get Runtime Dependencies using Frida API"""
    print("프리다 종속성검사")
    data = {"hash": hash}
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/frida/get_dependencies', data=data, headers=headers)

    if response.status_code == 200:
        print("Runtime dependencies collected successfully.")
        return response.json()
    else:
        print(f"Failed to get runtime dependencies: {response.status_code}")
        print(f"Error message: {response.json().get('error')}")
        return None



def frida_instrument(hash):
    """Frida Script Execution"""
    print("프리다 스크립트 실행")

    bypass_script = """
        Java.perform(function () {
       
            var RootCheckClass = Java.use("com.ldjSxw.heBbQd.a.b");
            RootCheckClass.k.implementation = function () {
                console.log("Bypassing root check");
                return false;  
            };
            
        });
        """
    headers = {'Authorization': APIKEY}
    data = {
        "hash": hash,
        "default_hooks": " ",  # 기본 훅 추가
        "auxiliary_hooks": " ",
        "frida_code": bypass_script
    }

    response = requests.post(SERVER + '/api/v1/frida/instrument', data=data, headers=headers)
    return response


def frida_instrument2(hash):
    """Frida Script Execution"""
    print("프리다 스크립트 실행")

    bypass_script = """
        Java.perform(function () {

            var dexClass = Java.use('com.ldjSxw.heBbQd.pupsPVlBod');

            // m1781k 메서드의 구현을 수정
            dexClass.k.implementation = function (xZip, mDir, mLister) {
                // 원래 구현을 호출하여 ZIP 파일을 처리합니다.
                this.k(xZip, mDir, mLister);

                // m1780j 메서드를 후킹하여 조건을 수정합니다.
                var originalj = this.j;
                this.j.implementation = function (zipFile, zipEntry, file, mLister) {
                    var fileName = file.getName();
                    // 모든 .dex 파일을 특별한 처리하지 않고 일반적으로 처리하게 함
                    if (!fileName.equals("classes.dex") && fileName.endsWith(".dex")) {
                        // do nothing, skip special processing for non-classes.dex .dex files
                    } else {
                        // classes.dex 또는 .dex가 아닌 파일들에 대해 원래 메서드를 호출
                        originalj.call(this, zipFile, zipEntry, file, mLister);
                    }
                };
            };
        });
        """
    headers = {'Authorization': APIKEY}
    data = {
        "hash": hash,
        "default_hooks": " ",  # 기본 훅 추가
        "auxiliary_hooks": " ",
        "frida_code": bypass_script
    }

    response = requests.post(SERVER + '/api/v1/frida/instrument', data=data, headers=headers)
    return response



def stop_dynamic(hash):
    """Stop dynamic Analysis"""
    print("stop dynamic Analysis")
    data = {"hash": hash}
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/dynamic/stop_analysis', data=data, headers=headers)
    # print(f"Stop dynamic Analysis Response: {response.json()}")
    print(f"동적분석 종료")
    joson_rep_dyn(hash)




# 동적 분석 JSON 보고서 생성 및 저장
def joson_rep_dyn(hash):
    print("Dynamic Analysis JSON Report")
    data = {"hash": hash}
    headers = {'Authorization': APIKEY}
    response = requests.post(SERVER + '/api/v1/dynamic/report_json', data=data, headers=headers)

    if response.status_code == 200:
        # JSON 데이터를 파일로 저장
        json_data = response.json()
        save_dir = 'reports'  # 저장할 디렉토리

        # 디렉토리 존재 여부 확인 및 생성
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        # 파일 이름 생성 ('dynamic' + timestamp + '.json')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dynamic_{timestamp}.json"
        file_path = os.path.join(save_dir, filename)

        # JSON 데이터 저장
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Dynamic Analysis JSON Report saved at: {file_path}")
    else:
        print(f"Failed to get JSON report: {response.status_code}")
        


#delete API
def delete(hash):
    """Delete Scan Result"""
    print("Deleting Scan")
    headers = {'Authorization': APIKEY}
    data = {"hash": hash}
    response = requests.post(SERVER + '/api/v1/delete_scan', data=data, headers=headers)
    # print(f"Delete File Reponse:{response.json()}")




def main():
    repackaged_apk_path = apktool.main()
    path = repackaged_apk_path

    
 # 첫 번째 APK 파일의 고정된 경로
    path_static_only = r'C:\Users\82106\Downloads\testAPK\sample_export\pgsHZz.apk'

    # MobSF Root CA 설치 (공통)
    install_root_ca()

    # 첫 번째 APK 파일에 대해 정적 분석과 PDF 리포트 생성 수행
    try:
        # 첫 번째 APK 파일에 대해 정적 분석 수행
        RES_static = upload(path_static_only)
        print("pgsHZz.apk 업로드 완료")
        HASH_static = scan(RES_static)
        json_resp(HASH_static)
        pdf(HASH_static)

    except FileNotFoundError:
        print("첫 번째 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"첫 번째 파일에 대해 오류가 발생했습니다: {str(e)}")
    
    # 두 번째 APK 파일 경로 설정 및 처리
    try:
        # MobSF Root CA 설치
        install_root_ca()
        
        #정적 검사
        RES = upload(path)
        HASH = scan(RES)
        json_resp(HASH)
        pdf(HASH)

    
        #동적 검사
        get()     
        start_dynamic(HASH)
        mobsfy(HASH)

        # tls_ssl(HASH)
        frida_instrument(HASH)
        
        # 활동 테스트
        activity_tester(HASH, "exported")
        activity_tester(HASH, "exported")
        
        # frida_instrument(HASH)

        stop_dynamic(HASH)
        delete(HASH)

    except FileNotFoundError:
        print("두 번째 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"두 번째 파일에 대해 오류가 발생했습니다: {str(e)}")

if __name__== "__main__":
    main()
