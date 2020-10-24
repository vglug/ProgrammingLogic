# ProgrammingLogic

Various programming logic in various programming languages.

This repo helps to everyone understand the programming logic, syntax and how works in diffrent languages.

## Contribution Guidelines

 Please follow the contribution guidelines. We consider following items in your program.

 1. Write your own program by own way.

 2. We expect new and intresting logic and program.

 3. Should have Well documentations

 4. Before raising pull request check alreay exisit or not in https://github.com/ViluppuramGLUG/ProgrammingLogic repo.
    
    
## Steps to Start 

 1. Login with [Github](https://github.com/login). (If you don't have account then [register](https://github.com/join) and [login](https://github.com/login))

 2. Login to [Hacktoberfest](https://hacktoberfest.digitalocean.com) using [Github](https://github.com).

 3. Fork this [https://github.com/ViluppuramGLUG/ProgrammingLogic](https://github.com/ViluppuramGLUG/ProgrammingLogic) repository to your repository (username/ProgrammingLogic).
    
    
## Steps to Contribute

 1. Choose your prefered langues in this repo.

 2. Write any programming logic/interview questions program in any language or your prefered language. That should be useful and intresting. 

 3. program filename should be valid, human readable and snake case format like (fibonacci_number.py) not like camel case (FibonacciNumber.py) except Java and Kotlin.

 4. Program should be well document. [ref link](#program-with-documentations)

 5. Commit and push it to your repo.
    
## Steps to pull request

 1. Click pull request in your repo after commit and push.

 2. Ensure base repository:(ViluppuramGLUG/ProgrammingLogic) <- head repository: (username/ProgrammingLogic). then click create pull request button.

 3. After that, Give valid title and message.

 4. Click Create Pull Request button.


 Ref more explanation : [link](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
    
    
## Example
 filename : ProgrammingLogic/python/palindrome_or_not.py [link](/python/palindrome_or_not.py)

### Program with documentations

``` python
    """ Palindrom or not given string """
    
    # function which return reverse of a string
    def isPalindrome(s):
        return s == s[::-1]
 
 
    # Getting string from user
    s = input("Enter word: ")
    ans = isPalindrome(s)

    # Checking the given string same as reversed string then print "Yes". otherwise print "No"
    if ans:
        print("Yes")
    else:
        print("No")
```
