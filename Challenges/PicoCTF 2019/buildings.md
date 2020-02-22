# Solution

## Process
Initially I thought that the answer was a file hidden inside the image so binwalk was attempted, that didn't work.

![binwalk](https://user-images.githubusercontent.com/32277825/75099894-f0b2ec80-5594-11ea-9820-cde38fac9c5d.png)


This is not the case as the hint notes encoded data.
> There is data encoded somewhere, there might be an online decoder


## zsteg
https://github.com/zed-0xff/zsteg

zsteg seems to do exactly what we want to do and reveals the flag.

### Syntax
```
zsteg buildings.png
```

![zsteg](https://user-images.githubusercontent.com/32277825/75099912-2c4db680-5595-11ea-9ed2-d2d5cfe074e9.png)

```
picoCTF{h1d1ng_1n_th3_b1t5}
```
