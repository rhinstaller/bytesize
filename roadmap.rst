Roadmap
=======

Completed
---------
* implementation
* extend tests (90% coverage, about as good as possible)

Future
------
1. Make library documentation actually appear on readthedocs

   - no dependency

2. package

   - no dependency

3. include _parseSpec change to parseSpec() in changelog and remark about
   change in next version for benefit of unknown downstream users

   - no dependency

4. update known downstream to use parseSpec

   - depends on 3

5. change blivet to use bytesize package

   - depends on 2
   - include the change in Changelog, warn that in subsequent version, size
     must be imported directly from bytesize package
   - export bytesize.size package from blivet as appropriate

6. change known downstream to get rid of dependence on blivet's size and
   depend on bytesize's size instead

   - depends on 5

7. stop exporting bytesize from blivet at all

   - depends on 6
   - ChangeLog entry

Task List
=========

Package
-------
* general packaging
* port translations from blivet

Use - Transform client code to use new library correctly
--------------------------------------------------------
By following the steps below we should be able to switch the packages
we have control over to bytesize package in such a way that at each
step downstream is compatible with two adjacent overlapping blivet
versions, so it will be possible to alternate updates to blivet and to
downstream w/out breaking downstream.

* Before:

  - Make parseSpec() public in blivet.
  - xform all Size(<string>) calls in anaconda/blivet-gui to
    Size(size.parseSpec(<string>)) calls. Not necessary for open-lmi;
    open-lmi doesn't seem to use str argument at all.

* Switch blivet to use bytesize library.

  - import, and export Size class and parseSpec, from new library so
    downstream see bytesize Size class.
  - eliminate all unnecessary Size(<string>) calls and substitute
    Size(parseSpec(<string>)) calls where they are necessary.
  - delete blivet/size.py and size tests from blivet package and any spec
    stuff.

* Switch downstream to use bytesize library.

  - inform openlmi, they will just have to change an import
  - for blivet-gui and anaconda, eliminate uses of parseSpec wherever possible
    as with blivet and add new dependency. Make sure Size is imported
    from bytesize.
  - in blivet, stop exporting bytesize size package.

Notes
=====

Needed to pull in a small amount of i18n and i18n related utils from
blivet. Maybe davidshea could be persuaded to centralize all of this
someday?
