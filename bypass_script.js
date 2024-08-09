
// // / Frida 스크립트를 사용하여 Java 코드를 훅킹합니다.
Java.perform(function() {

    // 'com.ldjSxw.heBbQd.a.b' 클래스에서 루트,감지를 수행 메서드 우회
    var RootCheckClass = Java.use('com.ldjSxw.heBbQd.a.b');

    // k() false반환 고정.루트 감지를 무력화
    RootCheckClass.k.implementation = function () {
        console.log("프리다 실행 com.ldjSxw.heBbQd.a.b");
        return false;  
    };


});


