
// program to check if the string is palindrome or not

function checkPalindrome(str) {

    // find the length of a string
    let len = string.length;

    // loop through half of the string
    for (let i = 0; i < len / 2; i++) {

        // check if first and last string are same
        if (string[i] !== string[len - 1 - i]) {
            return alert('It is not a palindrome');
        }
    }
    return alert('It is a palindrome');
}

// take input
let string = prompt('Enter a string: ');

// call the function
let value = checkPalindrome(string);
