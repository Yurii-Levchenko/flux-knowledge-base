# CONSTRAINTS — шортлист ніш 34–67 (Юрій, команда Flux)

> Цей документ читати першим перед будь-якою роботою над шортлистом. Порушувати його не можна.

## 1. Бюджет AppKittie — ЖОРСТКИЙ ЛІМІТ
- **Максимум 50 кредитів** на весь шортлист ніш 34–67. Це домовленість команди, її не можна порушувати.
- Баланс команди Flux на старті: **298** кредитів (перевірено 08.11.2026).
- Перед кожним платним запитом: план і вартість → «ок» від Юрія → запит.
- Кожен запит записується в журнал кредитів (§6) з накопиченою сумою. **Після 50 — стоп**, навіть якщо якусь нішу не досліджено. Тоді нішу оцінюємо за безкоштовними джерелами й позначаємо «без даних AppKittie».
- Економія:
  - безкоштовне — кеш (результати тіммейтів за останню добу) і `get_supported_countries`;
  - `search_apps` — 1 кредит за застосунок, ліміт **3–5** на запит;
  - **не використовувати**: keyword difficulty (10 кредитів за слово), ranking history (10 за запит), відгуки (1 за відгук);
  - `get_app_historicals` (2 кредити) — лише якщо без нього неможливо прийняти рішення.

## 2. Обсяг роботи
- Ніші **34–67** з файлу `niche_longlist_US.pdf` (34 ніші; перелік у §7).
- Результат: **3 найкращі ніші** з поясненням, таблицею оцінок і джерелами.
- Час: **≈ 1 година**.

## 3. Мета фінального проєкту (критерій відбору)
- Ніша, де реально побудувати продукт з **$500 000 виручки на місяць**.
- Ринок: **США**, B2C / prosumer, мобільний застосунок і/або web2app.
- Монетизація: **підписка** (журі не любить freemium: «не доведемо»).
- Потрібні дані для захисту: обсяг ринку, конкуренти, ціни, канали, LTV/CAC.

## 4. Блекліст (з `Additional Materials`, стор. 32–33)
- **Заборонено повністю:** Adult / NSFW, Gambling / Betting, Crypto / Web3 / NFT.
- **Заборонено (опрацьовані в ДЗ):** FemTech, Homework Help, Mental Health, Comics / Webtoons, Music Education, Sleep Tech.
- **Заборонено (перегріті):** Meditation & Mindfulness, Water / Hydration Tracking, Horoscope & Astrology, Book Summaries / Micro-Learning, Dog Care & Training.
- **Дозволено лише з умовою:** Generic Habit Tracking — лише як механіка; Generic To-Do / Productivity — лише для вузької ЦА; Generic Language Learning — лише для вузького ринку; Generic Fitness / Workout — лише для вузького сегмента.
- **Правило з Q&A:** якщо ніша дозволена, але її вузький сегмент межує з блеклістом — **краще оминати**.
- Жодна з ніш 34–67 не потрапляє в блеклист і не межує з ним (погоджено з Юрієм 08.11.2026).

## 5. Інші правила відбору й даних
- Критерії — з Лекції 3 (Stage 1 kill criteria + Stage 2 шість питань) і з Q&A.
- Без жорсткої регуляторики (медичні claims, ліцензії) і без Китаю / бідних країн.
- **Жодних цифр із market-report сайтів** (Grand View, Precedence, Astute тощо) — тільки bottom-up (сума конкурентів) або top-down (кількість людей × ціна).
- Оцінки AppKittie підписувати «оцінка AppKittie»: це лише стори, без вебу.
- Відокремлювати факти від припущень; не писати те, що не зможемо захистити.

## 6. Журнал кредитів AppKittie
| # | Дата | Запит | Кредитів | Накопичено (ліміт 50) |
|---|---|---|---|---|
| 0 | 08.11.2026 | `get_supported_countries` (перевірка) | 0 | 0 |
| 1 | 08.11.2026 | `search_apps` ×12 (limit 1, iOS): 44 PictureThis, PlantIn, Plantum, Planta; 47 Fishbrain, Fish AI, Fishing Points, FishAngler; 50 CoinSnap, Collectr, CollX, Coin ID | 12 | 12 |
| 2 | 08.11.2026 | `search_apps` ×12 (limit 1, iOS): 61 Ancestry, MyHeritage, Photomyne, Renew; 55 YarnPal, Loopsy, Sewpal, knitCompanion; 63 Paired, Agapé, Between, Evergreen | 12 | 24 |
| 3 | 08.11.2026 | `search_apps` ×10 (limit 1, iOS): 45 Picture Bird, Smart Bird ID, Bird Sounds ID; 67 Roadtrippers, The Dyrt, RV LIFE; 48 AllTrails, Gaia GPS; 41 ReciMe, eMeals | 10 | **34** |
| 4 | 08.11.2026 | `search_apps` ×14 (limit 1, **Google Play**) — за вказівкою Юрія «врахувати максимально Google Play, допрацюй»: 50 Collectr, CoinSnap, CollX; 55 YarnPal, Loopsy, Sewpal; 61 Photomyne, Ancestry, MyHeritage; 44 PictureThis; 41 ReciMe; 47 Fishbrain; 63 Paired; 67 The Dyrt. ⚠ Loopsy: запит повернув не той застосунок (гру «Energy: Anti-Stress Loops») — 1 кредит витрачено даремно, виручка Loopsy в Google Play невідома | 14 | **48** |
| 5 | 08.11.2026 | `get_app_historicals` YarnPal (iOS, period all: revenue, downloads, reviews) — за прямим «ок» Юрія | 2 | **50** |
| — | — | **ЛІМІТ ВИЧЕРПАНО (50 / 50).** Баланс команди 248. Нові запити — лише за новою домовленістю з командою | — | 50 / 50 |

## 7. Ніші 34–67
34 Child activity & camp finder · 35 Special needs parenting organizer (IEP) · 36 Home maintenance tracker · 37 Car ownership assistant · 38 Renter's toolkit · 39 First-time home buyer guide · 40 Home inventory для страховки · 41 Pantry / grocery waste reducer · 42 Moving & relocation planner · 43 Smart home setup assistant · 44 Plant care & identification · 45 Birdwatching / nature journaling · 46 Home brewing / fermentation / sourdough · 47 Fishing companion · 48 Hiking safety & trip planner · 49 Gardening для малих просторів · 50 Collectibles portfolio · 51 Wine / whiskey / coffee cellar · 52 Photography learning & critique · 53 Thrift / resale assistant · 54 Board game companion · 55 Knitting / sewing / DIY pattern manager · 56 Friend group coordination · 57 Local hobby communities · 58 Pickleball / padel court finder · 59 Neighbors / HOA communication · 60 Memorial / legacy storytelling · 61 Family tree + AI-реставрація фото · 62 Wedding planner · 63 Long-distance relationships toolkit · 64 Alumni / community networking · 65 Travel для digital nomads · 66 Accessible travel · 67 Road trip planner (EV, RV)
