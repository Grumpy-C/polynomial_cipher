# polynomial cipher
a very inefficient and pointless cipher made by me (it is not the kind of polynomial cipher you're thinking of if you're a real crypto nerd. probably)

## how does this work ??
let's say we got some plaintext $`p`$\
and some key $`k`$\
and the encrypted text $`e`$\
all of the characters will be in the decimal range 0~255

we loop over each character in the plaintext, index $`n`$\
$`x`$ is the highest index in the key's array\
encryption for each character is $`e[n] = \big(p[n]\,+\,k[0]\,+\,k[1]*n\,+\,k[2]*n^2\,+\,\,...\,\,+\,k[x-1]*n^{x-1}\,+\,k[x]*n^x\big)\,\text{mod}\,256`$

## is this even fast
No

## why did you make this then
i was trying to make affine cipher. then i fucked up. the equation to make ciphertext became $`e[n] = ax\,+\,b\,+\,p[n]`$ (in this encryption thing, terms would become $`e[n] = p[n]\,+ \,k[0]\,+\,k[1]*n`$ ) and i turned it into an encryption puzzle thing with the user having to brute the keys a and b that since that is only 65536 permutations to bruteforce. like a year later i thought to myself that this would be a cool idea for a cipher. 

i'm 16 bro don't expect me to come up with some groundbreaking shit

## is it secure
somewhat yea. maybe. idk, i'm not a math crypto prodigy. just use a key longer than like 4 characters and you should probably be fine
