# MusicBee Tag Hierarchy to Quod Libet Query

An unmaintained Python script that parses MusicBee tag hierarchies based on user input, and converts tags with children to queries usable with Quod Libet, because this was simpler for me to make than actually implementing a tag hierarchy explorer into QL.

Tested working with my RateYourMusic genre hierarchy and psychoadept's location hierarchy.

Be warned that there will be some initial CPU spikes if you decide to use a query with a lot of checks, and some trees will just flat-out crash Quod Libet.

This is here in case someone finds it useful.

# Usage

```
python mbth2qlq.py [-h] {tabs,spaces} file tag
```

The first argument is whether the tag hierarchy file uses tabs or spaces to denote children. The second argument is for the file, and the third for the tag you are looking for. For example, if you wanted every EDM genre in my RYM genre hierarchy, "Electronic Dance Music" would take its place.

This will only work on tags that have children in them. If you want a specific genre, you can just search that.
