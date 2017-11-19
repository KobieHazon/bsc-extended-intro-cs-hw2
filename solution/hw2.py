#Skeleton file for HW2 - Fall 2017-2018 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

import time

############
# QUESTION 1
############

# 1c
def reverse_dict(d):
    """reverses the given dictionary"""
    return {d[x]: x for x in d}

# 1e
def reverse_dict_in_place(d):
    """reverses the given dictionary in place"""
    keyval_list = d.items()
    l = []
    for key, val in keyval_list: #Create a copy of the dictionary
        l.append((key, val))
    for key, val in l: #remove keys from original dictionary and add the reversed
        if type(d[key]) != tuple:
            d.pop(key, None)
        d[val] = (key, None)
    for key, val in d.items(): #make dictionary in the correct form
        d[key] = val[0]



############
# QUESTION 2b
############

def power_new(a,b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin: 
        if bit == '1':
            result = result*a
        a = a*a
    return result


############
# QUESTION 3
############

#3b
def inc(binary):
    """incerements a given binary by 1 (input is string)"""
    carry = True
    index = len(binary) - 1
    while carry is True:
        if carry is True and binary[index] == '0': #Found a zero
            binary = binary[0:index] + '1' + '0'*(len(binary)-index-1)
            carry = False
        if index == 0 and carry is True: #String of 1's
            binary = '1' + ('0' * len(binary))
            carry = False
        index -= 1
    binary = binary.lstrip('0') #Remove excess zeros if exist
    return binary

#3c
def dec(binary):
    """decrements a given binary(string) by 1"""
    carry = True
    index = len(binary) - 1
    while carry is True:
        if index == 0 and index != (len(binary) - 1): #binary is of '100...'
            binary = ('1' * (len(binary) - 1))
            carry = False
        if carry is True and binary[index] == '1': #Found a one
            binary = binary[0:index] + '0' + ('1' * (len(binary) - 1 - index))
            carry = False
        index -= 1

    if binary != '0': #Remove excess zeros if exist
        binary = binary.lstrip('0')
    return binary

############
# QUESTION 4
############

#4a
def square_digit_chain(n):
    """Checks if square digit chain reaches 1 or 89 first"""
    while n != 89 and n != 1:
        current_num = 0 #Holds the sum of the digits squared
        while n > 0:
            current_num += (n % 10) ** 2
            n = n // 10 #Remove one digit(if there is)
        n = current_num
    return n

#4b
def count_nums_1(limit):
    """How many numbers from 1 to limit(not including) reach 1 first"""
    cnt = 0
    for tested in range(1, limit):
        if square_digit_chain(tested) == 1:
            cnt += 1
    return cnt

#4d
def pow_digit_chain(n, p):
    """finds the number that power (p) digit chain repeats first"""
    prev_nums = []
    while n not in prev_nums:
        current_num = 0
        prev_nums.append(n)
        while n > 0:
            current_num += (n % 10)**p
            n = n // 10
        n = current_num
    return n

#4e
def count_ends(limit, p):
    """Count numbers that have the p digit chain until limir that repeats count times"""
    cnt_dict = {}
    for n in range(1, limit):
        n_stop = pow_digit_chain(n, p)
        if n_stop in cnt_dict:
            cnt_dict[n_stop] += 1
        else:
            cnt_dict[n_stop] = 1
    return cnt_dict




############
# QUESTION 5
############

# 5a
def has_common(s1,s2,k):
    """Finds the k length common substring of s1 and s2"""
    if len(s1)<k or len(s2)<k:
        return False
    something = []
    for i in range(0, len(s1)-k + 1):
        something.append(s1[i:i+k])
    for i in something:
        if i in s2:
            return True
    return False

def lcs_length_1(s1, s2):
    """Checks the longest common substring length with has_common()"""
    k=1
    while has_common(s1,s2,k) == True:
        k+=1
    return k-1

#5b
def lcs_length_2(s1, s2):
    """Check the longest common substring length with 2 dimension list"""
    if len(s1) == 0 or len(s2) == 0:
        return 0
    m = [[0]*len(s2) for i in range(len(s1))] #2 Dimension list of zeroes
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] != s2[j]: 
                m[i][j] = 0 
            elif i == 0 or j == 0: #Borders
                m[i][j] = 1
            else:
                m[i][j] = 1 + m[i-1][j-1] #Diagonal

    return max([max(l) for l in m])

#5c
import random
def gen_str(n, alphabet):
    return "".join([random.choice(alphabet) for i in range(n)])

###Amir's code:
##n=4000
##alphabet = "abcdefghijklmnopqrstuvwxyz"
##print("two random strings of length", n)
##s1 = gen_str(n, alphabet)
##s2 = gen_str(n, alphabet)
##
##t0 = time.clock()
##res1 = lcs_length_1(s1,s2)
##t1 = time.clock()
##print("lcs_length_1", res1, t1-t0)
##
##t0 = time.clock()
##res2 = lcs_length_2(s1,s2)
##t1 = time.clock()
##print("lcs_length_2", res2, t1-t0)

###Michal's code
##n=4000
##alphabet = "abcdefghijklmnopqrstuvwxyz"
##print("two identical random strings of length", n)
##s1 = gen_str(n, alphabet)
##s2 = s1
##
##t0 = time.clock()
##res1 = lcs_length_1(s1,s2)
##t1 = time.clock()
##print("lcs_length_1", res1, t1-t0)
##
##t0 = time.clock()
##res2 = lcs_length_2(s1,s2)
##t1 = time.clock()
##print("lcs_length_2", res2, t1-t0)


#5d
def is_rotated(s1, s2):
    """Checks if s1 is rotated compared to s2"""
    if len(s1) != len(s2):
        return False
    for i in range(1,len(s2)):
        s2_rotated = s2[len(s2)-i:len(s2)] + s2[:len(s2)-i]
        if has_common(s2_rotated,s1,len(s2)):
            return True
    return False


########
# Tester
########

def test():
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    d_ans = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    if reverse_dict(d) != d_ans:
        print("error in reverse_dict()")

    original_id = hex(id(d))
    reverse_dict_in_place(d)
    if d != d_ans:
        print("error in reverse_dict_in_place()")
    if hex(id(d)) != original_id:
        print("reverse_dict_in_place() not in place")

    if power_new(2,3) != 8:
        print("error in power_new()")

    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("error in inc()")

    if dec("1") != "0" or \
       dec("101") != "100" or \
       dec("100") != "11" or \
       dec(dec("11")) != "1":
        print("error in dec()")
    
    if square_digit_chain(44) != 1 or \
       square_digit_chain(85) != 89 or \
       square_digit_chain(135) != 89:
        print("error in square_digit_chain()")

    if count_nums_1(50) != 11 or \
       count_nums_1(100) != 19:
        print("error in count_nums_1()")

    if pow_digit_chain(50, 7) != 5221343 or \
       pow_digit_chain(50, 3) != 371:
        print("error in pow_digit_chain()")

    if count_ends(79, 3) != {1: 2, 55: 1, 133: 9, 153: 26, 217: 3, 370: 10, 371: 23, 407: 3, 1459: 1} or \
       count_ends(44, 3) != {1: 2, 133: 6, 153: 14, 217: 2, 370: 5, 371: 14}:
        print("error in count_ends()")
    
    if has_common("ababc", "dbabca", 5) != False or \
       has_common("ababc", "dbabca", 4) != True or \
       has_common("ababc", "dbabca", 3) != True or \
       has_common("", "dbabca", 2) != False or \
       lcs_length_1("ababc", "dbabca") != 4:
        print("error in has_common()")
    
    if lcs_length_2("ababc", "dbabca") != 4 or \
       lcs_length_2("dbabca", "ababc") != 4 or \
       lcs_length_2("xxx", "ababc") != 0 :
        print("error in lcs_length_2()")

    if is_rotated('amirrub', 'rubamir') != True or \
    	is_rotated('amirrub', 'gilamir') != False:
        print("error in is_rotated()")    	
