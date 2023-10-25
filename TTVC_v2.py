def transposition(text, key, is_encrypt=True):
    lenght = len(text)
    if is_encrypt == True:
        teks_without_space = text.replace(" ", "1")
        if (lenght % key) != 0:
            for i in range(key):
                lenght+=1
                if (lenght % key) == 0:
                    break
        if len(teks_without_space) < lenght:
            # Hitung berapa karakter yang perlu ditambahkan
            characters_to_add = lenght - len(teks_without_space)
    
            # Gabungkan string dengan karakter yang diinginkan
            teks_without_space = teks_without_space + str(key) * characters_to_add
        rows = ['' for _ in range(key)]
        for i in range(lenght):
            rows[i%key] += teks_without_space[i]
        result = ''.join(rows)
    else:
        row_length = len(text) // key  # Hitung panjang baris berdasarkan panjang teks dan kunci
        rows = ['' for _ in range(row_length)]
        for i, char in enumerate(text):
            row_index = i % row_length  # Menggunakan modulus dari panjang baris
            rows[row_index] += char
        text_test = ''.join(rows)
        result = text_test.replace(str(key),"")

    return result



def vigenere(text, key, is_encrypt=True):
    result = []
    key = key.upper()  # Konversi kunci ke huruf besar
    key_length = len(key)
    
    for i in range(len(text)):
        if text[i].isalpha():
            text_char = text[i]
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')  # Hitung pergeseran berdasarkan huruf kunci
            
            if is_encrypt:
                # Enkripsi: c(p) = (p + k) mod 26
                encrypted_char = chr((ord(text_char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Dekripsi: p(c) = (c - k) mod 26
                decrypted_char = chr((ord(text_char) - ord('A') - shift) % 26 + ord('A'))
                
            result.append(encrypted_char if is_encrypt else decrypted_char)
        else:
            # Jika karakter bukan huruf, biarkan karakter tersebut tidak berubah
            result.append(text[i])
    
    return ''.join(result)

def triple_transposition_vigenere(text, keys, is_encrypt=True):
    t1 = keys[0]
    t2 = keys[1]
    t3 = keys[2]
    s1 = keys[3].upper()
    s2 = keys[4].upper()
    s3 = keys[5].upper()

    if is_encrypt:
        # Enkripsi
        trans1 = transposition(text, t1, True)
        substituted1 = vigenere(trans1, s1, True)
        trans2 = transposition(substituted1, t2, True)
        substituted2 = vigenere(trans2, s2, True)
        trans3 = transposition(substituted2, t3, True)
        substituted3 = vigenere(trans3, s3, True)
        result = substituted3
    else:
        # Dekripsi
        trans3 = vigenere(text, s3, False)
        substituted2 = transposition(trans3, t3, False)
        trans2 = vigenere(substituted2, s2, False)
        substituted1 = transposition(trans2, t2, False)
        trans1 = vigenere(substituted1, s1, False)
        text = transposition(trans1, t1, False)
        text = text.replace("1", " ")
        result = text

    return result

# enkripsi
plaintext = "INI ADALAH PLAINTEXT KRIPTOGRAFI"
keys = [3, 5, 7, "SEMBILAN", "GAJAH", "SEBELAS"]
encrypted_text = triple_transposition_vigenere(plaintext, keys)
print("Encrypted text:", encrypted_text)

# dekripsi
decrypted_text = triple_transposition_vigenere(encrypted_text, keys, False)
print("Decrypted text:", decrypted_text)

#Andiprtm
