var log = function () {
    console.log.apply(console, arguments)
}

var a = [1, 3, 5, 6] //数组
log('数组长度', a.length)

for(var i = 0; i < a.length; i++){
    log(a[i])
}
