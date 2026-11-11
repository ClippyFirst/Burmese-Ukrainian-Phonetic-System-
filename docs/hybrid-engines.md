# Гібридний бірманський IPA-рушій

`burmese_ukrainian.HybridBurmeseEngine` поєднує внутрішній консервативний аналіз із зовнішніми рушіями, не зливаючи орфографічну романізацію з фонетичною транскрипцією.

## Склад

- Внутрішній структурний парсер — Myanmar grapheme clusters, кінзі, підрядкові приголосні, медіалі, голосні та маркери.
- Внутрішній `to_ipa()` — обмежений правиловий кандидат; часткові результати з `?` не потрапляють до голосування.
- `make_google_wfst_backend()` — готовий адаптер з перевіркою echoed input для зібраного Thrax/FST/symbol-table.
- `make_myg2p_dictionary_backend()` — exact-match адаптер п'ятого IPA-поля myG2P v2.0; не MLCTS і не вимовна романізація.
- `burmese-g2p-crf` / Epitran можуть бути додані як окремі backend-и, якщо їхній вихід справді IPA і відповідає профілю.

## Контракт backend-а

```python
def my_backend(text: str) -> dict:
    return {"ipa": "…", "status": "candidate", "provenance": {"engine": "google-wfst", "revision": "pinned-revision"}}
```

Підключення:

```python
from burmese_ukrainian import (
    create_hybrid_engine, make_google_wfst_backend, make_myg2p_dictionary_backend,
)
engine = create_hybrid_engine({
    "google-wfst": make_google_wfst_backend("bazel-bin/utils/thrax_g2p", "bazel-bin/my/G2P.fst", "bazel-bin/my/ipa_phoneme.syms"),
    "myg2p-ipa": make_myg2p_dictionary_backend("myg2p.ver2.0.txt"),
})
result = engine.analyze("မြန်မာ")
```

## Правило злиття

Сирі кандидати зберігаються окремо. Транспортна нормалізація знімає лише зовнішні IPA-дужки й надлишкові пробіли; довгота, тон, фонація, придих, голосність та інші діакритики залишаються значущими. Два незалежно названі backend-и з однаковим IPA дають `ensemble_consensus`. Один кандидат або розбіжність не перетворюються на фінальну IPA-відповідь: `ipa` залишається `null`.

Внутрішній частковий адаптер не голосує, якщо повертає `?`. Зовнішні помилки ізолюються: падіння одного backend-а не знищує результати інших.

## Межі

Консенсус рушіїв — не незалежна експертна оцінка. Потрібно перевіряти можливий спільний словниковий/тренувальний витік, діалект, careful citation profile, тоново-фонаційні контрасти та сегментацію. MLCTS-романізація не є IPA й не може бути голосом IPA-ансамблю. Лише перевірений IPA передається в український target adapter.
