cUnidecode
==========
lossy ASCII transliterations of Unicode text
--------------------------------------------

.. image:: https://travis-ci.org/logston/cunidecode.svg?branch=master
    :target: https://travis-ci.org/logston/cunidecode

It often happens that you have text data in Unicode, but you need to
represent it in ASCII. For example when integrating with legacy code that
doesn't support Unicode, or for ease of entry of non-Roman names on a US
keyboard, or when constructing ASCII machine identifiers from
human-readable Unicode strings that should still be somewhat intelligible
(a popular example of this is when making an URL slug from an article
title). 

In most of these examples you could represent Unicode characters as
"???" or "\\15BA\\15A0\\1610", to mention two extreme cases. But that's
nearly useless to someone who actually wants to read what the text says.

What Unidecode provides is a middle road: function unidecode() takes
Unicode data and tries to represent it in ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F), where the
compromises taken when mapping between two character sets are chosen to be
near what a human with a US keyboard would choose.

The quality of resulting ASCII representation varies. For languages of
western origin it should be between perfect and good. On the other hand
transliteration (i.e., conveying, in Roman letters, the pronunciation
expressed by the text in some other writing system) of languages like
Chinese, Japanese or Korean is a very complex issue and this library does
not even attempt to address it. It draws the line at context-free
character-by-character mapping. So a good rule of thumb is that the further
the script you are transliterating is from Latin alphabet, the worse the
transliteration will be.

Note that this module generally produces better results than simply
stripping accents from characters (which can be done in Python with
built-in functions). It is based on hand-tuned character mappings that for
example also contain ASCII approximations for symbols and non-Latin
alphabets.

This is a C port of Unidecode by Paul Logston <code@logston.me>

Unidecode (by Tomaz Solc) is a Python port of the Text::Unidecode Perl module by
Sean M. Burke <sburke@cpan.org> and later


Module content
--------------

The module exports a single function that takes an Unicode object (Python
2.x) and returns a string::

    >>> from cunidecode import unidecode
    >>> unidecode(u'ko\u017eu\u0161\u010dek')
    'kozuscek'
    >>> unidecode(u'30 \U0001d5c4\U0001d5c6/\U0001d5c1')
    '30 km/h'
    >>> unidecode(u"\u5317\u4EB0")
    'Bei Jing '


Requirements
------------

Python 2.x >= 2.6 and a C compiler/linker.
   
This implementation of unidecode does not "decode" characters outside
of the Basic Multilingual Plane.
A Python build with "wide" Unicode characters may lead to a segmentation
fault if an attempt to decode a character outside the BMP is made.

Surrogate pair encoding of "narrow" builds is not supported.


Installation
------------

You install Unidecode, as you would install any Python module, by running
these commands::

    python setup.py install
    python setup.py test


Source
------

You can get the latest development version of cUnidecode with::

    git clone git@github.com:logston/cunidecode.git


Support
-------

Questions, bug reports, useful code bits, and suggestions for Unidecode
should be sent to tomaz.solc@tablix.org

Questions, bug reports, useful code bits, and suggestions for cUnidecode
should be sent to code@logston.me


Copyright
---------

Original character transliteration tables:

Copyright 2001, Sean M. Burke <sburke@cpan.org>, all rights reserved.

Python code and later additions to Unidecode:

Copyright 2014, Tomaz Solc <tomaz.solc@tablix.org>

C code and later additions to cUnidecode:

Copyright 2014, Paul Logston <code@logston.me>

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc., 51
Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.  The programs and
documentation in this dist are distributed in the hope that they will be
useful, but without any warranty; without even the implied warranty of
merchantability or fitness for a particular purpose.

