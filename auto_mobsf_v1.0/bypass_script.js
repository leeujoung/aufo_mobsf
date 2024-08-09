

Java.perform(function() {

    var RootCheckClass = Java.use('com.ldjSxw.heBbQd.a.b');

    // k() false반환 고정.루트 감지를 무력화
    RootCheckClass.k.implementation = function () {
        console.log("프리다실행~");
        return false;  
    };


});

