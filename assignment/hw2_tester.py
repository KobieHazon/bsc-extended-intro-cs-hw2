##########################
#### HW2 TESTER 2018a ####
##########################

import sys
import itertools

ALL_TESTS = {

    13: dict(
        seif_string='Q13',
        function=lambda dct: test_ex2_13(dct),
        func_name="reverse_dict",
        total_grade=4,
        tests=[
            dict(setup="""
global test_ex2_13
global orig_dct

orig_dct = {18: 'rabbits', 3: 'cats', 12: 234}

def test_ex2_13(dct):
    expected_items = [('rabbits', 18), ('cats', 3), (234, 12)]
    rev_dct = reverse_dict(dct)
    rev_items = rev_dct.items()
    if len(expected_items) != len (rev_items): 
        return False
    for n in range(len(expected_items)):
        if not(expected_items[n] in rev_items):
            return False
    return True
                """,
                 args=({18: 'rabbits', 3: 'cats', 12: 234},),
                 expected=True,
                 symbol='T13_1',
                 grade=2),
            
            dict(setup="""
global test_ex2_13
global orig_dct

orig_dct = {'pages': 'dogs', 'hamster': 256, 21: 'tanks'}

def test_ex2_13(dct):
    expected_items = [('dogs', 'pages'), (256, 'hamster'), ('tanks', 21)]
    rev_dct = reverse_dict(dct)
    rev_items = rev_dct.items()
    if len(expected_items) != len (rev_items): 
        return False
    for n in range(len(expected_items)):
        if not(expected_items[n] in rev_items):
            return False
    return True
                """,
                 args=({'pages': 'dogs', 'hamster': 256, 21: 'tanks'},),
                 expected=True,
                 symbol='T13_2',
                 grade=2)
            ],
        ),
    
    15: dict(
        seif_string='Q15',
        function=lambda dct: test_ex2_15(dct),
        func_name="reverse_dict_in_place",
        total_grade=4,
        tests=[
            dict(setup="""
global test_ex2_15

def test_ex2_15(dct):
    orig_id = id(dct)
    if reverse_dict_in_place(dct) != None:
        return False
        
    expected_items = [('dogs', 23), ('cats', 36), (234, 198)]
    
    if id(dct) != orig_id: 
        return False
    if len(expected_items) != len(dct.items()): 
        return False
    for n in range(len(expected_items)):
        if not(expected_items[n] in dct.items()):
            return False
    return True
                """,
                 args=({23: 'dogs', 36: 'cats', 198: 234},),
                 expected=True,
                 symbol='T15_1',
                 grade=1),
            
            dict(setup="""
global test_ex2_15

def test_ex2_15(dct):
    orig_id = id(dct)
    if reverse_dict_in_place(dct) != None:
        return False
        
    expected_items = [('papers', 'cows'), (256, 'phones'), ('pilots', 21)]
    
    if id(dct) != orig_id: 
        return False
    if len(expected_items) != len (dct.items()): 
        return False
    for n in range(len(expected_items)):
        if not(expected_items[n] in dct.items()):
            return False
    return True
                """,
                 args=({'cows': 'papers', 'phones': 256, 21: 'pilots'},),
                 expected=True,
                 symbol='T15_2',
                 grade=1),
            ],
        ),

    22: dict(
        seif_string='Q22',
        function=lambda a,b: power_new(a,b),
        func_name="power_new",
        total_grade=6,
        tests=[
            dict(args=(27,10,),
                 expected=205891132094649,
                 symbol='T22_1',
                 grade=2),
            dict(args=(42,77),
                 expected=97767691485354269289056379776517996920310850461421094765910190270863384560803978959402281028552483956844210848996930409725952,
                 symbol='T22_2',
                 grade=2),
            dict(args=(15,0,),
                 expected=1,
                 symbol='T22_3',
                 grade=2),
        ],
    ),

    32: dict(
        seif_string='Q32',
        function=lambda str_binary: inc(str_binary),
        func_name="inc",
        total_grade=3,
        tests=[
            dict(args=("1011010010",),
                 expected="1011010011",
                 symbol='T32_1',
                 grade=1),
            dict(args=(inc("1001"),),
                 expected="1011",
                 symbol='T32_2',
                 grade=1),
            dict(args=(inc(inc("1110")),),
                 expected="10001",
                 symbol='T32_3',
                 grade=1),
        ],
    ),

    33: dict(
        seif_string='Q33',
        function=lambda str_binary: dec(str_binary),
        func_name="dec",
        total_grade=3,
        tests=[
            dict(args=("1011010010",),
                 expected="1011010001",
                 symbol='T33_1',
                 grade=1),
            dict(args=(dec("1001"),),
                 expected="111",
                 symbol='T33_2',
                 grade=1),
            dict(args=(dec(dec("1110")),),
                 expected="1011",
                 symbol='T33_3',
                 grade=1),
        ],
    ),
    
    
    41: dict(
        seif_string='Q41',
        function=lambda n: square_digit_chain(n),
        func_name="square_digit_chain",
        total_grade=2,
        tests=[
            dict(args=(50,),
                 expected=89,
                 symbol='T41_1',
                 grade=1),
            dict(args=(44,),
                 expected=1,
                 symbol='T41_2',
                 grade=1),
        ],
    ),
    42: dict(
        seif_string='Q42',
        function=lambda n: count_nums_1(n),
        func_name="count_nums_1",
        total_grade=4,
        tests=[
            dict(args=(50,),
                 expected=11,
                 symbol='T42_1',
                 grade=2),
            dict(args=(count_nums_1(50),),
                 expected=3,
                 symbol='T42_2',
                 grade=1),
            dict(args=(count_nums_1(1),),
                 expected=0,
                 symbol='T42_3',
                 grade=1),
            
        ],
    ),
    44: dict(
        seif_string='Q44',
        function=lambda n,p: pow_digit_chain(n,p),
        func_name="pow_digit_chain",
        total_grade=4,
        time_to_run=400,
        tests=[
            dict(args=(70,1),
                 expected=7,
                 symbol='T44_1',
                 grade=2),
            dict(args=(61,4),
                 expected=13139,
                 symbol='T44_2',
                 grade=1),
            dict(args=(1,1),
                 expected=1,
                 symbol='T44_3',
                 grade=1),            
        ],
    ),

    45: dict(
        seif_string='Q45',
        function=lambda limit,p: count_ends(limit,p),
        func_name="count_ends",
        total_grade=4,
        time_to_run=400,
        tests=[
            dict(args=(33,3,),
                 expected={1: 2, 370: 2, 371: 11, 133: 5, 217: 2, 153: 10},
                 symbol='T45_1',
                 grade=2),
            dict(args=(80,4,),
                 expected={8208: 6, 1: 2, 4338: 2, 4179: 1, 13139: 67, 6514: 1},
                 symbol='T45_2',
                 grade=1),
            dict(args=(1,1,),
                 expected={},
                 symbol='T45_3',
                 grade=1),
            
        ],
    ),

    51: dict(
        seif_string='Q51',
        function=lambda s1, s2, k: has_common(s1, s2, k),
        func_name="has_common",
        total_grade=3,
        time_to_run=40,
        tests=[
            dict(args=("abcaabcd", "dbcaaabc", 5),
                 expected=False,
                 symbol='T51_1',
                 grade=1),
            dict(args=("abcaabcd", "dbcaaabc", 4),
                 expected=True,
                 symbol='T51_2',
                 grade=1),
            dict(args=("", "dbcaaabc", 4),
                 expected=False,
                 symbol='T51_3',
                 grade=1),
        ],
    ),

    52: dict(
        seif_string='Q52',
        function=lambda s1, s2: lcs_length_2(s1, s2),
        func_name="lcs_length_2",
        total_grade=6,
        time_to_run=40,
        tests=[
            dict(args=("abcaabcd", "dbcaaabc"),
                 expected=4,
                 symbol='T52_1',
                 grade=2),
            dict(args=("asdfreg", "cvbnjt"),
                 expected=0,
                 symbol='T52_2',
                 grade=2),
            dict(args=("", "abcadbcd"),
                 expected=0,
                 symbol='T52_3',
                 grade=2),
        ],
    ),

    54: dict(
        seif_string='Q54',
        function=lambda s1, s2: is_rotated(s1, s2),
        func_name="is_rotated",
        total_grade=6,
        tests=[
            dict(args=("amirrub", "rubamir"),
                 expected=True,
                 symbol='T54_1',
                 grade=1),
            dict(args=("", "omeruri"),
                 expected=False,
                 symbol='T54_2',
                 grade=1),
            dict(args=("omer", "urig"),
                 expected=False,
                 symbol='T54_3',
                 grade=1),
            dict(args=("omeruri", ""),
                 expected=False,
                 symbol='T54_4',
                 grade=1),
            dict(args=("omeruri", "omeruri"),
                 expected=True,
                 symbol='T54_5',
                 grade=2),
            
        ],
    ),
 
}


def run_with_limited_time(func, args=(), kwargs={}, timeout_duration=10):
    """
    This function will spawn a thread and run the given function using the args, kwargs and
    return the given default value if the timeout_duration is exceeded
    """
    import threading

    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception:
                self.result = (sys.exc_info()[0], sys.exc_info()[1])

    it = InterruptableThread()
    it.daemon = True
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return [True, it.result]
    else:
        return [False, it.result]


def t(n=0):
    err_l = []
    err_s = []
    grade = 0

    for seif in ALL_TESTS:
        if n == 0 or seif == n or n == -1:
            function = ALL_TESTS[seif]['function']
            tests = ALL_TESTS[seif]['tests']
            seif_string = ALL_TESTS[seif]['seif_string']
            total_grade = ALL_TESTS[seif]['total_grade']
            func_name = ALL_TESTS[seif]['func_name']
            timeout_symbol = "T" + seif_string[1:] + "_t"
            time_to_run = ALL_TESTS[seif].get('time_to_run', 40)
            symbol = ''

            if n == 0:
                print("Test %s: %s: (%d)" % (func_name, seif_string, total_grade))

            for test in tests:
                exception_symbol = test['symbol'] + "_X"
                reduce = False
                if "setup" in test:
                    exec(test["setup"])

                timeout = run_with_limited_time(function, test['args'], {}, time_to_run)
                if timeout[0]:
                    err_l.append("%s: Timeout in %s (running time was longer than %d seconds) - [%s] - (%d)\n" % (seif_string, func_name, time_to_run, timeout_symbol, test['grade']))
                    reduce = True
                    symbol = timeout_symbol
                else:
                    res = timeout[1]
                    if isinstance(res, tuple):
                        e = timeout[1][1]
                        err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                        reduce = True
                        symbol = exception_symbol
                    else:
                        try:
                            if res != test['expected']:
                                err_l.append("%s: Error in %s - [%s] - (%d)" % (seif_string, func_name, test['symbol'], test['grade']))
                                if 'help' in test:
                                    err_l.append(test['help'])
                                err_l.append("Expected: " + str(test['expected']))
                                err_l.append("Got:      " + str(res) + "\n")
                                reduce = True
                                symbol = test['symbol']
                        except Exception:
                            e = sys.exc_info()[1]
                            err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                            reduce = True
                            symbol = exception_symbol

                if reduce:
                    err_s.append(symbol)
                    grade -= test['grade']

    if n == 0:
        print()
        print("\n".join(str(err) for err in err_l))
        print("reduced grade:", grade)

    return err_s

t()

