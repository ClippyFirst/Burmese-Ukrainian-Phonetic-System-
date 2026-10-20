# Third-party notices and licensing status

This file records a research review, not legal advice.

## Repository's own license

No root LICENSE file is currently present and GitHub reports no detected license for this repository. No open-source license is inferred. The owner must choose the license for original code and decide separately how to license the corpus/data before a blanket license is added.

## External candidates reviewed

### Epitran
- Project: https://github.com/dmort27/epitran
- Package metadata identifies the code license as MIT-Modern-Variant.
- The upstream support table lists mya-Mymr but warns that Burmese is limited support because the orthography is highly ambiguous.
- Review mapping/preprocessor/postprocessor files and their provenance individually before redistribution; do not assume a package-code license automatically answers every data-rights question.
- Citation: Mortensen, D. R., Dalmia, S., & Littell, P. (2018). Epitran: Precision G2P for Many Languages. LREC 2018.

### myG2P
- Project: https://github.com/ye-kyaw-thu/myG2P
- Declared dictionary license: CC BY-NC-SA 4.0.
- Noncommercial and ShareAlike conditions make it unsuitable as an unreviewed universal dependency, particularly where commercial use or a differently licensed corpus is possible.
- Preserve attribution and evaluate derivative database/adaptation questions before any reuse.
- Related burmese-G2P repository: https://github.com/kyaw-yethu/burmese-G2P

## Rule for future additions

For every external engine, dictionary, model, or copied data set, record: exact upstream URL; release/commit; component name; code license; data/model license; attribution; commercial-use restrictions; redistribution/adaptation obligations; artifact hash; and whether any material was actually copied into this repository.
