//date ： 2018/6/3 15：35



var log = function () {
    console.log.apply(console, arguments);
}


// 测试套路
var ensure = function (condition, message) {
    if(!condition){
        console.log(message);
    }
}

var sum = 0
var n = 0
while (n <= 100) {
    if (n % 2 ==1){
        sum += n
    }
    n++
}

log('sum = ', sum);

ensure(sum == 2500, '报错')
