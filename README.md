# Show Siblings

*This is a plugin for the [Glyphs font editor](http://glyphsapp.com/).*  

It superimposes a group of predefined glyphs in the background of your letters. This can be both pretty helpful in the beginning of a design as well as at intermediate progress where quick proof overview is needed. The degree of a desired match depends on each design, of course.

### Install

In *Glyphs > Preferences > Addons > Modules*, click on the *Install Modules* button. This installs the Vanilla module by Tal Leming which is required by the *Show Siblings* plug-in.

Then either:

1. In *Window > Plugin Manager*, click on the *Install* button next to the *Show Siblings* entry. 
2. Restart Glyphs.

or:

1. Download or clone this repository.
2. Either:  
   Double click the `.glyphsReporter` file and confirm the dialogue in Glyphsapp to install.  
   Or:  
   Copy the `.glyphsReporter` into your Glyphsapp Plugins folder (eg. `/Library/Application\ Support/Glyphs/Plugins`). You can use subfolders (e.g. to sort plugins by author) there.
3. Restart Glyphs.

### How to use

When ever you need it, toggle `Show * Siblings` from the *View* menu.

### Default groups (current status)

```
LATIN
    c e o
    b p
    d q
    h n r l
    i j
    t f
    k x
    v y
    B D P R
    C G O Q
    H U N
    K V X Y

CYRILLIC
    o-cy be-cy fita-cy obarred-cy
    ef-cy sha-cy iu-cy
    el-cy de-cy
    ka-cy k
    ve-cy softsign-cy hardsign-cy
    en-cy ii-cy pe-cy tse-cy
    ia-cy zhe-cy x
    
    Ii-cy H N Nje-cy
    El-cy De-cy Lje-cy
    Be-cy Ve-cy Ge-cy Gheupturn-cy Softsign-cy
    Ze-cy B three
    Ka-cy K X
    E-cy C
    Obarred-cy O
    Ia-cy Zhe-cy X
    Hardsign-cy Yeru-cy

GREEK
    kappa k
    mu u
    nu gamma v y
    zeta xi sigmafinal epsilon c
    beta germandbls rho p sigma
    iota tau i
    upsilon u delta theta omicron
    chi x
    psi phi omega

    Delta Lambda A
    Xi Sigma E Z
    Omega O
    Phi Psi U
    Theta Eta Omicron

```

### Examples

<p align="center">

<img src="https://github.com/Mark2Mark/Glyphsapp-Plugins/blob/Screenshots/ShowSiblings/Screenshots/ShowSiblings Shequalin DeutschMark.jpg" alt="Show Siblings Shequalin Demo" height="300px">

<img src="https://github.com/Mark2Mark/Glyphsapp-Plugins/blob/Screenshots/ShowSiblings/Screenshots/screencapDemoFont.gif" alt="Show Siblings live Demo" height="300px">

</p>


##### Known issues

- Currently working on Cyrillic and Greek, as well as a Custom Parameter to set up italic construction for `a` and `g`.
- Removing a component doesn’t update the displayed layer in the group members until the .glyphs file is reopened.

##### Pull Requests

Feel free to comment or pull requests for any improvements.

##### License

Copyright 2015 [Mark Frömberg](http://www.markfromberg.com/) *@Mark2Mark*

Made possible with the GlyphsSDK by Georg Seifert (@schriftgestalt) and Rainer Erich Scheichelbauer (@mekkablue).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
