
def es_palindromo(str1): 
    i = 0
    j = len(str1)-1
    while i<=j:
        if str1[i]!=str1[j]:
            return False
        i = i + 1
        j = j - 1
        

    return True


def test_es_palindromo():
    assert es_palindromo('pasta') == False
    assert es_palindromo('arroz') == False
    assert es_palindromo('salas') == True
    assert es_palindromo('amor a roma') == True
