# Кандидатний гібридний IPA-шар Burmese

HybridBurmeseEngine запускає чинний RuleBasedBurmeseEngine і збирає зовнішні IPA-кандидати. Google WFST та myG2P підключаються окремо; Epitran — додатковий comparator із tones=True за замовчуванням; Goruut/інші CLI-сумісні рушії — через make_command_backend. MLCTS не є IPA.


Зовнішні провайдери **не завантажуються й не запускаються автоматично**. Виклик `HybridBurmeseEngine()` без аргументу `providers` запускає лише внутрішні правила та повертає порожній список зовнішніх кандидатів. Щоб запустити конкретні зовнішні рушії, їх потрібно явно передати в словник `providers` після локального встановлення/підготовки залежностей і перевірки прав. Це не змінює поведінку опублікованого сайту та не запускає мережеві завантаження під час звичайного аналізу.

## Підключення

```python
from burmese_ukrainian import (
    HybridBurmeseEngine, make_google_wfst_backend,
    make_myg2p_dictionary_backend, make_epitran_backend,
)
engine = HybridBurmeseEngine({
    "google-wfst": make_google_wfst_backend("bazel-bin/utils/thrax_g2p", "bazel-bin/my/G2P.fst", "bazel-bin/my/ipa_phoneme.syms"),
    "myg2p-ipa": make_myg2p_dictionary_backend("myg2p.ver2.0.txt"),
    "epitran": make_epitran_backend(),
})
result = engine.analyze("မြန်မာ")
```

Кандидати не голосують і не замінюють фінальне ipa. Внутрішній детермінований рушій зберігає контроль до появи незалежного gold.

## Бенчмарки та рішення

- myG2P v2: 24,009 унікальних записів. У попередньому тесті внутрішнього рушія 635 повних IPA-виходів, 0 строгих збігів; це свідчить про невідповідність/розбіжність, а не про точність myG2P.
- Окремий CRF diagnostic: 100/100 прогнозів, 84 source-concordant, але можливий train/test overlap і вхід уже містить межі складів.
- Google WFST: збірка й smoke 6/6 структурних проб; accuracy не обчислюється.
- Epitran 1.35.3: 6/6 raw outputs на структурних пробах; accuracy не обчислюється.
- Незалежне Yangon-profile IPA gold = 0.

myG2P має CC BY-NC-SA 4.0; не копіювати словник у цей репозиторій без окремої перевірки прав. Google Language Resources — Apache-2.0, але транзитивні залежності не повністю pinned.

## Пріоритети провайдерів

Нижче число задає порядок запуску й показу кандидатів (менше = раніше), а не доведену якість чи право на автоматичне просування:

1. **myG2P exact IPA lookup (10)** — першим лише для однозначного точного словникового збігу; неоднозначні записи відхиляються. Права CC BY-NC-SA 4.0 та відповідність Yangon IPA-профілю залишаються обов'язковими умовами.
2. **Google Burmese WFST (20)** — головний кандидат для системної контекстної граматики; наразі лише 6/6 smoke-виходів, незалежний gold = 0, транзитивні залежності ще потребують повного pinning.
3. **Epitran (40)** — сегментний comparator з tones=True; профільна точність не встановлена.
4. **CRF (60)** — лише експериментальний comparator, доки не доведено відсутність train/test overlap і не усунуто перевагу від попередньої сегментації.
5. **Goruut (90)** — останній comparator; слабка concordance, неповні фрагменти й відсутній weights asset.
6. Невідомі провайдери (50) — не отримують довіри лише через підключення.

Фінальне IPA залишається за внутрішніми детермінованими правилами. Підвищення джерела до авторитетного вимагає незалежного Yangon IPA gold, оцінки тону/фонації/довготи/код, відсутності витоку даних і відтворюваного профільного benchmark.


## Current-branch exact raw-output run — 2026-11-14

Optional workflow **43582075278 SUCCESS** on code/test SHA `45d3513ad1f6bbbda8d9a97768e493cdda08856d`:

- Google Burmese Thrax/OpenFst: pinned Bazel 7.4.1 build and symbol-table invariants passed; **6/6** non-empty raw outputs on structural-only probes. Report SHA-256 `88372233d85df73593b030ee0f91aa678fe86fd1c6d5cdc18e7c609b8eefd2c6`; artifact ZIP SHA-256 `501a279189bbfb643b1c185a043bdc80ea6de9ca55e0a1116f4f8ba30ce59820`.
- Epitran 1.35.3: six raw structural-only outputs; e.g. `ကော်` → `kaʊʔ`, `မြန်` → `məjaɴ`; zero independently verified gold; exact-match count and accuracy remain null. Artifact ZIP SHA-256 `4b60180e479d884826ed158dab525c809a3c45c66e627eb4904e61c8be048304`.
- Burmese-G2P CRF: **100/100** predictions; 84 source-concordant; zero gold; `NOT_SCORED_POSSIBLE_TRAINING_OVERLAP`; supplied syllable segmentation means end-to-end segmentation is not tested. Artifact ZIP SHA-256 `fbf339ed34dfb80b4147998d7b2fee4c602fcb1abc10c91b9229ea10ccf7bb9d`.

All three artifacts were downloaded and inspected. None provides accuracy or adjudicated IPA gold. External outputs remain diagnostic candidates only.
