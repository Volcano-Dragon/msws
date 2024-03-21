```
NAME 
    msws

DESCRIPTION 
    The msws.py module is a Python library designed to generate random numbers using the Middle Square Weyl sequence algorithm.
    This algorithm offers a methodical approach to producing pseudo-random numbers with a focus on simplicity and efficiency.
    The module offers functionalities to both generate random numbers and seed values necessary for the process.
    
    GitHub Repositry link: https://github.com/Volcano-Dragon/msws
    Module Author: Garv Saxena
    Garv Saxena email: garvsaxena185@gmail.com
     
    Middle Square Weyl Sequence author: Bernard Widynski
    Copyright (c) 2014-2022 Bernard Widynski
    Bernard Widynski  email: mswsrng@gmail.coms
    License: The Middle-Square Weyl Sequence RNG is available (free, but without warranty)
    as open-source software under the GNU General Public License.

FUNCTIONS
    msws_rand(change_seed=False, input_seed=False, input_seed_value=None)
        This function generates 64 bits random numbers based on the seed. It uses the Middle square weyl sequence for generating random numbers.
        x - random output [0,0xffffffff]                                        
        w - Weyl sequence (period 2^64)                                         
        s - an odd constant chosen by the rand_digits,
            So that the 8 upper hexadecimal digits are different and also that the 8 lower digits are different.
            Only non-zero digits are used and the last digit is chosen to be odd.
            This assures sufficient change in the Weyl sequence on each iteration of the RNG. 
        Parameters:
            change_seed = To change the seed value, for generating a new random number sequence.
                Default: False
            input_seed = To set the input_seed_value as a seed value, for generating a new random number sequence.
                Default: False
            input_seed_value = The integer value of 64 bit. (for better random output sequence use irregular pattern of the bits)
        Returns:
            x = 32 bits final random integer number
    
    set_seed()
        This function changes the seed value using the rand_digits function from seed_gen.py
        Parameters:
            None
        Returns:
            None
```
