# Детермінований бірманський рушій

Активний браузерний рушій і Python API за замовчуванням використовують фіксовані правила репозиторію. Зовнішні G2P-процеси, WFST та словники не запускаються автоматично. Mya2Rom використовується лише в окремому режимі MLCTS-романізації.

## Конвеєр

1. NFC-нормалізація та сегментація Myanmar-послідовностей.
2. Структурний розбір початкових приголосних, kinzi, conjunct, medials, голосних, фіналей та знаків.
3. Застосування явних правил onset–medial–rime.
4. Побудова IPA лише там, де реалізоване правило повністю покриває склад.
5. Відмова від IPA для невстановлених фіналей, тональних/просодичних або неоднозначних комбінацій.

## Детермінованість і межі

Однаковий нормалізований ввід і та сама версія таблиць дають однаковий результат. Статус PROPOSED не означає експертно доведену вимову. Неповний результат позначається як PARTIAL; зовнішні джерела не використовуються як fallback.

Профіль: my-yangon-careful-citation-v1. MLCTS і фонетична IPA-транскрипція — окремі режими.

## Python: правиловий рушій

```python
from burmese_ukrainian import RuleBasedBurmeseEngine
result = RuleBasedBurmeseEngine().analyze("ကာ")
```

## Дослідницький гібридний API

HybridBurmeseEngine обгортає RuleBasedBurmeseEngine і за явної конфігурації збирає зовнішні кандидати: Google WFST, точні IPA-записи myG2P v2, Epitran та pinned CLI adapters для Goruut/CRF. MLCTS не є IPA і не входить до цього шару. Кандидати зберігаються з provenance; голосування та автоматична заміна фінального IPA заборонені. Без provider-ів результат дорівнює результату правилового рушія.

```python
from burmese_ukrainian import HybridBurmeseEngine, make_epitran_backend
engine = HybridBurmeseEngine({"epitran": make_epitran_backend()})
result = engine.analyze("မြန်မာ")
```

Це дослідницький comparator, а не production fallback. Просування кандидата потребує незалежного gold для Standard Yangon та перевірки тону, фонації, довготи, код і сегментації. Див. docs/hybrid-engines.md.
