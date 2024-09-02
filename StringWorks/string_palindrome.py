
#create a function is_palindrome(word) return True if word is palindrome string
#else return false

def is_palindrome(str):

    reverse=str[::-1]

    return True if str==reverse else False
    
print(is_palindrome("madam"))

def reverse(word):

    reverse=word[::-1]
    return reverse
print(reverse("hello"))