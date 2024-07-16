const ispalindrome = (num) => {
    return num === +num.toString().split("").reverse().join("");
}
console.log(ispalindrome(1421));