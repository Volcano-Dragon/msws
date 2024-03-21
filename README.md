# MSWS

## Overview
The msws package is designed to generate random numbers using the Middle Square Weyl sequence algorithm. This algorithm offers a methodical approach to producing pseudo-random numbers with a focus on simplicity and efficiency. The module offers functionalities to both generate random numbers and seed values necessary for the process.


## Getting Started

### Installation

```
pip install msws
```


### Quick Start Example

```python
import msws as m
# msws_rand(change_seed=False, input_seed=False, input_seed_value=None)

print(m.msws_rand()) #prints first random generated number using inbuilt seed generation (seed_gen.py) module
print(m.msws_rand()) #prints second random generated number using the above seed value

#Sequence of random number...
print(m.msws_rand()) #prints third...
print(m.msws_rand()) #prints forth...
print(m.msws_rand())
print(m.msws_rand()) 
```

### Change the seed
You can change the seed value if you want a new random number sequence, It uses inbuilt seed_gen.py module for generation and changing the seed value:

**Set change_seed = True**:
  To change the seed value, for generating a new random number sequence. (Default = **False**)

```python
import msws as m
# msws_rand(change_seed=False, input_seed=False, input_seed_value=None)

#prints first random generated number using changed seed value
print(m.msws_rand(True)) #postional argument to set change_seed = True
print(m.msws_rand()) #prints second random generated number using the changed seed value

#Sequence of random number...
print(m.msws_rand()) #prints third...
print(m.msws_rand()) #prints forth...
print(m.msws_rand())
print(m.msws_rand()) 
```

### Input the seed value
If you want to set your seed value for a random number sequence:

**Set input_seed = True**:
  To set the **input_seed_value** as a RNG seed value, for generating a new random number sequence.<br>(Default = **False**)

***Note***: Enter a 64-bit integer value in **input_seed_value** that has an irregular patterns of bits, to make sure the good random number sequence is generated.


```python
import msws as m
# msws_rand(change_seed=False, input_seed=False, input_seed_value=None)

#prints first random generated number using input seed value
print(m.msws_rand(False,True,13091206342165455529)) #postional argument to set input_seed = True and input_seed_value = <your seed value>
print(m.msws_rand()) #prints second random generated number using the input seed value

#Sequence of random number...
print(m.msws_rand()) #prints third...
print(m.msws_rand()) #prints forth...
print(m.msws_rand())
print(m.msws_rand()) 
```

