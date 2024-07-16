const ispalindrome = (number) => {
    return number<0 ? false:number === +number.toString().split("").reverse().join("");}

console.log(ispalindrome(121));