var fibGenerator = function(n) {
    var arr =[0,1]
    for(var i=2;i<=n;i++){
        arr.push(arr[i-1]+arr[i-2]);
    }
    return arr;
};
console.log(fibGenerator(10));

var fibGenerator1 = function(n){
    if (n <= 1){
        return n;
    }
    else{
       return fibGenerator1(n-1)+ fibGenerator1(n-2);
       
    }
}
console.log(fibGenerator1(10))