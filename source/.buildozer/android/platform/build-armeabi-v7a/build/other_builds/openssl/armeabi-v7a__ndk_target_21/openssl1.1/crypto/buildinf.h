/*
 * WARNING: do not edit!
 * Generated by util/mkbuildinf.pl
 *
 * Copyright 2014-2017 The OpenSSL Project Authors. All Rights Reserved.
 *
 * Licensed under the OpenSSL license (the "License").  You may not use
 * this file except in compliance with the License.  You can obtain a copy
 * in the file LICENSE in the source distribution or at
 * https://www.openssl.org/source/license.html
 */

#define PLATFORM "platform: android-arm"
#define DATE "built on: Sat May 16 09:42:12 2020 UTC"

/*
 * Generate compiler_flags as an array of individual characters. This is a
 * workaround for the situation where CFLAGS gets too long for a C90 string
 * literal
 */
static const char compiler_flags[] = {
    'c','o','m','p','i','l','e','r',':',' ','/','h','o','m','e','/',
    'l','e','o','n','/','.','b','u','i','l','d','o','z','e','r','/',
    'a','n','d','r','o','i','d','/','p','l','a','t','f','o','r','m',
    '/','a','n','d','r','o','i','d','-','n','d','k','-','r','1','9',
    'c','/','t','o','o','l','c','h','a','i','n','s','/','l','l','v',
    'm','/','p','r','e','b','u','i','l','t','/','l','i','n','u','x',
    '-','x','8','6','_','6','4','/','b','i','n','/','c','l','a','n',
    'g',' ','-','t','a','r','g','e','t',' ','a','r','m','v','7','a',
    '-','l','i','n','u','x','-','a','n','d','r','o','i','d','e','a',
    'b','i','2','1',' ','-','f','o','m','i','t','-','f','r','a','m',
    'e','-','p','o','i','n','t','e','r',' ','-','m','a','r','c','h',
    '=','a','r','m','v','7','-','a',' ','-','m','f','l','o','a','t',
    '-','a','b','i','=','s','o','f','t','f','p',' ','-','m','f','p',
    'u','=','v','f','p',' ','-','m','t','h','u','m','b',' ','-','f',
    'P','I','C',' ','-','f','P','I','C',' ','-','p','t','h','r','e',
    'a','d',' ',' ','-','t','a','r','g','e','t',' ','a','r','m','v',
    '7','a','-','l','i','n','u','x','-','a','n','d','r','o','i','d',
    'e','a','b','i',' ','-','g','c','c','-','t','o','o','l','c','h',
    'a','i','n',' ','/','h','o','m','e','/','l','e','o','n','/','.',
    'b','u','i','l','d','o','z','e','r','/','a','n','d','r','o','i',
    'd','/','p','l','a','t','f','o','r','m','/','a','n','d','r','o',
    'i','d','-','n','d','k','-','r','1','9','c','/','t','o','o','l',
    'c','h','a','i','n','s','/','a','r','m','-','l','i','n','u','x',
    '-','a','n','d','r','o','i','d','e','a','b','i','-','4','.','9',
    '/','p','r','e','b','u','i','l','t','/','l','i','n','u','x','-',
    'x','8','6','_','6','4',' ','-','-','s','y','s','r','o','o','t',
    '=','/','h','o','m','e','/','l','e','o','n','/','.','b','u','i',
    'l','d','o','z','e','r','/','a','n','d','r','o','i','d','/','p',
    'l','a','t','f','o','r','m','/','a','n','d','r','o','i','d','-',
    'n','d','k','-','r','1','9','c','/','p','l','a','t','f','o','r',
    'm','s','/','a','n','d','r','o','i','d','-','2','1','/','a','r',
    'c','h','-','a','r','m',' ','-','t','a','r','g','e','t',' ','a',
    'r','m','v','7','a','-','l','i','n','u','x','-','a','n','d','r',
    'o','i','d','e','a','b','i','2','1',' ','-','f','o','m','i','t',
    '-','f','r','a','m','e','-','p','o','i','n','t','e','r',' ','-',
    'm','a','r','c','h','=','a','r','m','v','7','-','a',' ','-','m',
    'f','l','o','a','t','-','a','b','i','=','s','o','f','t','f','p',
    ' ','-','m','f','p','u','=','v','f','p',' ','-','m','t','h','u',
    'm','b',' ','-','f','P','I','C',' ','-','D','O','P','E','N','S',
    'S','L','_','U','S','E','_','N','O','D','E','L','E','T','E',' ',
    '-','D','O','P','E','N','S','S','L','_','P','I','C',' ','-','D',
    '_','_','A','N','D','R','O','I','D','_','A','P','I','_','_','=',
    '2','1',' ','-','i','s','y','s','t','e','m',' ','/','h','o','m',
    'e','/','l','e','o','n','/','.','b','u','i','l','d','o','z','e',
    'r','/','a','n','d','r','o','i','d','/','p','l','a','t','f','o',
    'r','m','/','a','n','d','r','o','i','d','-','n','d','k','-','r',
    '1','9','c','/','s','y','s','r','o','o','t','/','u','s','r','/',
    'i','n','c','l','u','d','e','/','a','r','m','-','l','i','n','u',
    'x','-','a','n','d','r','o','i','d','e','a','b','i',' ','-','i',
    's','y','s','t','e','m',' ','/','h','o','m','e','/','l','e','o',
    'n','/','.','b','u','i','l','d','o','z','e','r','/','a','n','d',
    'r','o','i','d','/','p','l','a','t','f','o','r','m','/','a','n',
    'd','r','o','i','d','-','n','d','k','-','r','1','9','c','/','s',
    'y','s','r','o','o','t','/','u','s','r','/','i','n','c','l','u',
    'd','e',' ','-','D','N','D','E','B','U','G',' ','-','D','_','_',
    'A','N','D','R','O','I','D','_','A','P','I','_','_','=','2','1',
    ' ','-','D','A','N','D','R','O','I','D',' ','-','D','_','_','A',
    'N','D','R','O','I','D','_','A','P','I','_','_','=','2','1',' ',
    '-','I','/','h','o','m','e','/','l','e','o','n','/','.','b','u',
    'i','l','d','o','z','e','r','/','a','n','d','r','o','i','d','/',
    'p','l','a','t','f','o','r','m','/','a','n','d','r','o','i','d',
    '-','n','d','k','-','r','1','9','c','/','s','y','s','r','o','o',
    't','/','u','s','r','/','i','n','c','l','u','d','e','/','a','r',
    'm','-','l','i','n','u','x','-','a','n','d','r','o','i','d','e',
    'a','b','i',' ','-','I','/','h','o','m','e','/','l','e','o','n',
    '/','t','r','a','v','a','i','l','/','c','r','e','m','i','l','a',
    'u','n','c','h','/','.','b','u','i','l','d','o','z','e','r','/',
    'a','n','d','r','o','i','d','/','p','l','a','t','f','o','r','m',
    '/','b','u','i','l','d','-','a','r','m','e','a','b','i','-','v',
    '7','a','/','b','u','i','l','d','/','p','y','t','h','o','n','-',
    'i','n','s','t','a','l','l','s','/','c','r','e','m','i','l','a',
    'u','n','c','h','/','i','n','c','l','u','d','e','/','p','y','t',
    'h','o','n','3','.','8','\0'
};
