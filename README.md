# Show Siblings

*This is a plugin for the [Glyphs font editor](http://glyphsapp.com/).*  

It superimposes a group of predefined glyphs in the background of your letters. This can be both pretty helpful in the beginning of a design as well as at intermediate progress where quick proof overview is needed. The degree of a desired match depends on each design, of course.

### Install

1. Download or clone this repository.
2. Either:  
   Double click the `.glyphsReporter` file and confirm the dialogue in Glyphsapp to install.  
   Or:  
   Copy the `.glyphsReporter` into your Glyphsapp Plugins folder (eg. `/Library/Application\ Support/Glyphs/Plugins`). You can use subfolders (e.g. to sort plugins by author) there.
3. Restart Glyphs.

### How to use

When ever you need it, toggle `Show * Siblings` from the view menu.

### Default groups

```
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
```

### Examples

![Show Siblings Shequalin Demo](https://raw.githubusercontent.com/DeutschMark/Show-Siblings/master/Screenshots/ShowSiblings%20Shequalin%20DeutschMark.jpg?raw=true "Show Siblings Shequalin Demo")

![Show Siblings live Demo](https://raw.githubusercontent.com/DeutschMark/Show-Siblings/master/Screenshots/screencapDemoFont.gif?raw=true "Show Siblings live Demo")


##### Known issues

- Currently working on Cyrillic and Greek, as well as a Custom Parameter to set up italic construction for `a` and `g`.
- Removing a component doesn’t update the displayed layer in the group members until the .glyphs file is reopened.

##### Pull Requests

Feel free to comment or pull requests for any improvements.

##### License

Copyright 2015 [Mark Frömberg](http://www.markfromberg.com/) *@DeutschMark*

Made possible with the GlyphsSDK by Georg Seifert (@schriftgestalt) and Rainer Erich Scheichelbauer (@mekkablue).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
