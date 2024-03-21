'''The seed_gen.py module serves as a standalone component within the MiddleSquareWeylRandom ecosystem,
specifically dedicated to the generation of seed values required for initiating the Middle Square Weyl sequence algorithm.
This module is designed with a focus on providing high-quality, 64-bit odd constants as seed values,
ensuring the robustness and randomness of the generated sequences.

GitHub Repositry link: https://github.com/Volcano-Dragon/msws
Module Author: Garv Saxena
Garv Saxena email: garvsaxena185@gmail.com
 
Middle Square Weyl Sequence author: Bernard Widynski
Copyright (c) 2014-2022 Bernard Widynski
Bernard Widynski  email: mswsrng@gmail.coms
License: The Middle-Square Weyl Sequence RNG is available (free, but without warranty)
as open-source software under the GNU General Public License.
'''

sconst = [
0x37e1c9b5e1a2b843, 0x56e9d7a3d6234c87, 0xc361be549a24e8c7, 0xd25b9768a1582d7b,
0x18b2547d3de29b67, 0xc1752836875c29ad, 0x4e85ba61e814cd25, 0x17489dc6729386c1,
0x7c1563ad89c2a65d, 0xcdb798e4ed82c675, 0xd98b72e4b4e682c1, 0xdacb7524e4b3927d,
0x53a8e9d7d1b5c827, 0xe28459db142e98a7, 0x72c1b3461e4569db, 0x1864e2d745e3b169,
0x6a2c143bdec97213, 0xb5e1d923d741a985, 0xb4875e967bc63d19, 0x92b64d5a82db4697,
0x7cae812d896eb1a5, 0xb53827d41769542d, 0x6d89b42c68a31db5, 0x75e26d434e2986d5,
0x7c82643d293cb865, 0x64c3bd82e8637a95, 0x2895c34d9dc83e61, 0xa7d58c34dea35721,
0x3dbc5e687c8e61d5, 0xb468a235e6d2b193
]

xi,wi,si = 0,0,0
def mswsi():
    '''
    This is the local copy of the MSWS-Middle-Square Weyl Sequence Random Number Generator (32-bit output).

    The msws consists of three 64 bit numbers:  xi, wi, and si                                                                       
    xi - random number (final random number output)                                         
    wi - Weyl sequence (period 2^64)                                         
    si - an odd constant (seed value)                                                    
                                                                      
    The Weyl sequence is added to the square of x. The middle is extracted by shifting right 32 bits.

    Parameters: 
        None - it uses the globally declared variables (xi, wi, si) which is mutable by rand_digits(n)
            
    Returns:
        xi - middle bits of the numbers
    '''
    global xi, wi, si
    xi = ((xi%2**64)**2)%2**64
    wi = (wi%2**64+si%2**64)%2**64
    xi = (xi%2**64+wi%2**64)%2**64
    xi = ((xi>>32) | (xi<<32))%2**64
    return xi%2**32

def rand_digits(n):
    '''
    This function creates a random 64-bit pattern, which can be used to      
    initialize seed value s in msws PRNG.  The pattern is chosen  
    so that the 8 upper hexadecimal digits are different and also that the 
    8 lower digits are different. Only non-zero digits are used and the   
    last digit is chosen to be odd. Roughly half the bits will be set to  
    one and roughly half of the bits will be set to zero. This assures       
    sufficient change in the Weyl sequence on each iteration of the RNG.

    Parameters: 
        n - The input parameter n is a 64-bit number in the range of 0 to 2^64-1.
            A set of random digits will be created for this input value
            
    Returns:
        u - Random 64-bit pattern seed value which can be used in the msws PRNG.
    '''
    global xi, wi, si
    r = n // 100000000
    t = n % 100000000
    si = sconst[r%30]
    r //= 30
    xi = (t*si) + (r*si*100000000)
    wi = xi
    u = (mswsi()%8)*2 + 1
    v = 1<<u
    m=60
    c=0
    while(m>0):
        j = mswsi() 
        for i in range(0, 32, 4):
            k = (j>>i) & 0xf 
            if (k!=0) and ((c & (1<<k)) == 0): #
                c |= (1<<k)
                u |= (k<<m) 
                m -= 4
                if m==24 or m==28:
                    c = (1<<k) | v
                if m==0:
                    break
    return u
