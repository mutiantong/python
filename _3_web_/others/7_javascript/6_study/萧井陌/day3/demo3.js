var log = function () {
    console.log.apply(console, arguments);
}

var grade = 10
if (grade < 7) {
    log('小学生')
}
else{
    log('初中以上')
}


var add = function (a, b) {
    return a + b
}
