# data/ — сирі дані команди Flux

Тут лежать сирі дані, на яких побудовані документи в `docs/`.

**Перед тим як витрачати кредити AppKittie або збирати дані заново, перевір цю папку.** Кеш AppKittie безкоштовний лише 24 години, тож повторний запит знову коштує кредитів, а тут відповіді збережені назавжди.

**Правила:**
- **Назва файлу:** `<джерело>_<що>_<РРРР-ММ-ДД>.<розширення>`.
- **Новий файл** = рядок у таблиці нижче + витрати кредитів у `docs/credits_log.md`.
- **Ніколи не кладемо** паролі, коди доступу, API-ключі, особисті дані (імена й контакти людей), матеріали лекцій школи.

---

## appkittie/ — відповіді AppKittie (модельні оцінки)

| Файл | Що всередині | Дата | Використано в |
|---|---|---|---|
| `appkittie_raw_results_2026-11-08_to_22.jsonl` | **Усі 111 відповідей AppKittie** за 08–22.11.2026: `search_apps` ×84, `get_app_detail` ×10, креатори, органіка, реклама, онбординги, ключові слова, історія. Разом ≈ 168 кредитів | 08–22.11.2026 | Усі документи `docs/01_*` і `docs/02_*` |
| `competitors_summary_2026-11-22.json` | Зведення по 10 конкурентах Collectibles: виручка iOS і Google Play, завантаження, ціни підписок, Meta-реклама, креатори, SDK | 22.11.2026 | `docs/02_collectibles/COMPETITORS_DEEP_DIVE.md` |
| `holodex_app_detail_2026-11-22.txt` | Повна картка HoloDex з даними Meta Ads Transparency: охоплення за віком і статтю, витрати, CPM по країнах | 22.11.2026 | там само, розділ 5.2 |
| `holodex_onboarding_screens_2026-11-22.txt` | 19 екранів онбордингу HoloDex з описом дизайну; пейвол — екран 09 | 22.11.2026 | там само, розділ 4.2 |
| `yarnpal_historicals_ios_2026-11-08.txt` | Щоденна історія YarnPal (iOS): виручка, завантаження, оцінки | 08.11.2026 | `docs/01_niche_selection/SHORTLIST_34-67.md`, розділ 7 |

**Формат JSONL** — один рядок на один запит:
```json
{"called_at": "2026-11-22T15:41:10Z", "tool": "get_app_detail", "input": {"appId": "1603892248"},
 "credits_spent": 1, "balance_after": 573, "result": { ... відповідь API ... }}
```
Деякі відповіді не поміщалися в результат інструмента. У таких рядках `result` — це текст «Output has been saved…», а сам вміст — в окремих `.txt` вище.

**Як шукати** (Python):
```python
import json
rows = [json.loads(l) for l in open("data/appkittie/appkittie_raw_results_2026-11-08_to_22.jsonl", encoding="utf-8")]
collectr = [r for r in rows if "1603892248" in json.dumps(r["input"]) or "collectr" in json.dumps(r["input"]).lower()]
```

**Застереження:**
- Виручка й завантаження — **модельні оцінки AppKittie** за останні 30 днів, глобально, лише стори. Продажів через сайт і комісій маркетплейсів у них немає.
- Оцінки змінюються: Collectr на iOS за 2 тижні змінився з $635K на $934K. Тож дата запиту важлива.
- Для YarnPal історія виручки ≈ коефіцієнт × кількість оцінок застосунку. Спаду вона не показує (`docs/01_niche_selection/SHORTLIST_34-67.md`, розділ 7).
- Індекс реклами AppKittie неповний. Кількість активних оголошень беремо з Meta Ad Library (`COMPETITORS_DEEP_DIVE.md`, розділ 5.4).

---

## 01_niche_selection/ — вибір ніші (безкоштовні публічні джерела)

| Папка / файл | Що всередині | Джерело | Дата |
|---|---|---|---|
| `shortlist_34-67/itunes_scan.json`, `itunes_targeted.json` | Топ застосунків за кількістю оцінок для ніш 34–67 і цільові пошуки брендів | iTunes Search API (US) | 08.11.2026 |
| `shortlist_34-67/entrants_scan.json` | Новачки 2024–2026 у 8 нішах і частка тих, хто «вижив» (≥ 1K оцінок) | iTunes Search API | 08.11.2026 |
| `shortlist_34-67/wayback_all.json` | Кількість оцінок 15 лідерів у US App Store за 2022–2026 роки | Wayback Machine | 08.11.2026 |
| `team_niches_deep_dive/entrants_team.json`, `itunes_competitors.json` | Новачки й конкуренти в 4 нішах тіммейтів | iTunes Search API | 08.11.2026 |
| `team_niches_deep_dive/wb_t1–t3.json` (+ `.txt` логи) | Динаміка оцінок лідерів у 4 нішах (2022–2026) | Wayback Machine | 08.11.2026 |
| `*.py` | Скрипти, якими все це зібрано. Шляхи в них вказують на старі локальні папки, тож перед запуском їх треба змінити | — | — |

## 02_collectibles/ — ніша Collectibles

| Файл | Що всередині | Джерело | Дата |
|---|---|---|---|
| `appstore_reviews.json` | **≈ 4 400 свіжих відгуків** (до 500 на застосунок) по 12 конкурентах + описи й ціни з App Store. Поля: оцінка, заголовок, текст, версія, дата; **імен авторів немає** | RSS-фід відгуків App Store + iTunes Lookup | 10.11.2026 |
| `themes.json`, `analyze.py`, `fetch_reviews.py` | Теми скарг (regex) і скрипти збору й аналізу | — | 10.11.2026 |
| `google_trends_22-11-2026.json` | Google Trends, США, 5 років: «pokemon card value», «collectr», «tcgplayer», «card grading», «psa grading» — середні за роками і порівняння рік до року | Google Trends | 22.11.2026 |
| `sources/collectr_state_of_hobby_2026_mid_year.pdf` | Звіт Collectr «State of the TCG Hobby, mid-2026» (самозвіт компанії). © Collectr; оригінал: https://public.getcollectr.com/public-assets/reports/state-of-the-hobby-2026-mid-year-report.pdf | Collectr | 06.2026 |

**Застереження:** тексти відгуків — це користувацький контент з App Store. У документах їх переказуємо, а не цитуємо масово.
