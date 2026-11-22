# Flux — база знань команди (Genesis Warsaw IT School 5.0, Final Project)

Спільна база знань команди **Flux**: дослідження ринку, конкуренти, продукт, юніт-економіка, пітч.

Кожен учасник працює з репозиторієм **локально**, разом зі своїм AI-агентом (Claude Code, Cursor, Codex). Через GitHub ми синхронізуємося, а кожна зміна потрапляє в спільну версію лише після перевірки тіммейтом.

- **Ніша:** Collectibles — AI-сканер, ціна й портфель колекції. Старт з Pokémon TCG.
- **Захист:** 07.12.2026.

**З чого почати читати:**
1. [`docs/02_collectibles/COLLECTIBLES_ANALYSIS.md`](docs/02_collectibles/COLLECTIBLES_ANALYSIS.md) — розділ 0.
2. [`docs/01_niche_selection/DEEP_DIVE_4_niches.md`](docs/01_niche_selection/DEEP_DIVE_4_niches.md) — розділ 0.

---

## Структура

| Шлях | Що всередині |
|---|---|
| `AGENTS.md` | **Правила для AI-агентів.** Агент читає цей файл першим (Claude Code — через `CLAUDE.md`) |
| `docs/01_niche_selection/` | Як обирали нішу: шортлисти, глибокий аналіз 4 ніш, самері тіммейтів |
| `docs/02_collectibles/` | Аналіз ніші: конкуренти, відгуки, функції, ціни, джерела даних, монетизація |
| `docs/03_product/` | Функціонал, MVP, онбординг, пейвол |
| `docs/04_unit_economics/` | Юніт-економіка: припущення, сценарії, розрахунки |
| `docs/05_pitch/` | Структура презентації, тези, Q&A для журі |
| `docs/credits_log.md` | Журнал витрат кредитів AppKittie (спільний бюджет) |
| `templates/TEMPLATE.md` | Шаблон нового документа |
| `data/` | **Сирі дані й скрипти:** відповіді AppKittie, скани App Store, архів Wayback, Google Trends, відгуки, звіт Collectr. Опис — у `data/README.md`. Перед новим дослідженням перевір, чи дані вже є |

---

## Правила

1. **Кожен факт — з джерелом і датою.** Цифри AppKittie підписуємо «оцінка AppKittie».
2. **Припущення позначаємо [гіпотеза].**
3. **Мова — українська.** Назви компаній і метрик — англійською.
4. **Зміни — лише через Pull Request.** У `main` напряму не пушимо. Кожен PR погоджує інший учасник команди.
5. **Сирі дані — у `data/`** з описом у `data/README.md`. Щоб не робити ту саму роботу двічі, перед дослідженням загляни туди.
6. **Кредити AppKittie — спільні.** Витрачаємо лише за згоди команди й записуємо в [`docs/credits_log.md`](docs/credits_log.md).

> ⚠️ **Репозиторій публічний.** Ніколи не комітимо:
> - паролі, коди доступу AppKittie, API-ключі;
> - особисті дані;
> - матеріали лекцій школи.
>
> Якщо щось таке потрапило в репозиторій — одразу пиши Юрію.

---

## 1. Налаштування (один раз, ≈ 15 хв)

### 1.1. Акаунт і доступ
1. Зареєструйся на [github.com/signup](https://github.com/signup) і увімкни двофакторну автентифікацію.
2. У **Settings → Emails** увімкни **Keep my email addresses private**. Так твій email не з'явиться в публічних комітах.
3. Надішли Юрію свій GitHub-нік і прийми запрошення (**Accept invitation** у листі або через 🔔).

### 1.2. Встановити Git і GitHub CLI

**Mac** — у Terminal:
```bash
xcode-select --install          # встановлює git, якщо його ще немає
brew install gh                 # якщо немає Homebrew: https://brew.sh або інсталятор з https://cli.github.com
```

**Windows** — у PowerShell:
```powershell
winget install --id Git.Git -e
winget install --id GitHub.cli -e
```
Після встановлення закрий і відкрий термінал заново.

### 1.3. Увійти в GitHub і скачати репозиторій
Ці команди однакові для Mac і Windows:
```bash
gh auth login                   # GitHub.com → HTTPS → Login with a web browser
gh repo clone Yurii-Levchenko/flux-knowledge-base
cd flux-knowledge-base
git config user.name "Твоє Ім'я"
git config user.email "<id>+<нік>@users.noreply.github.com"   # адресу знайдеш у GitHub → Settings → Emails
```

### 1.4. Підключити свого AI-агента
- **Claude Code:** запусти сесію **в папці `flux-knowledge-base`**. Агент сам прочитає `CLAUDE.md` → `AGENTS.md`.
- **Cursor:** відкрий папку `flux-knowledge-base` як проєкт. `AGENTS.md` підхопиться автоматично.
- **Codex:** запусти агента в папці `flux-knowledge-base`. `AGENTS.md` підхопиться автоматично.
- **Інші агенти:** першим повідомленням напиши «Прочитай AGENTS.md і дотримуйся його».

---

## 2. Щоденна робота

### 2.1. Через агента (основний спосіб)
Дай агенту задачу, а гілку, коміти й PR він зробить сам за правилами з `AGENTS.md`. Приклади запитів:

> Онови `main`, створи гілку `anna/unit-economics`. На основі `docs/02_collectibles/COLLECTIBLES_ANALYSIS.md` (розділи 5–7) створи `docs/04_unit_economics/assumptions.md`: усі припущення з джерелами й позначками [гіпотеза]. Відкрий PR.

> Прочитай PR #3 і дай рецензію: чи є джерела, чи позначені гіпотези, чи немає секретів. Нічого не зливай.

Перед тим як агент відкриє PR, переглянь його зміни сам. **Відповідальність за PR — на людині, а не на агенті.**

### 2.2. Вручну (ті самі кроки)
```bash
git switch main && git pull               # 1. свіжа версія
git switch -c anna/pricing                # 2. своя гілка: <нік>/<тема>
# 3. редагуєш файли (VS Code або будь-який редактор)
git add docs/02_collectibles/pricing.md   # 4. додаєш лише потрібні файли
git diff --staged                         #    перевіряєш: немає секретів і особистих даних
git commit -m "Додав ціни конкурентів"
git push -u origin anna/pricing           # 5. відправляєш гілку
gh pr create --fill                       # 6. відкриваєш Pull Request
```
Після злиття PR:
```bash
git switch main && git pull && git branch -d anna/pricing
```

### 2.3. Рецензія чужого PR
```bash
gh pr list                       # відкриті PR
gh pr checkout 3                 # подивитися PR #3 локально
gh pr review 3 --approve         # погодити
gh pr review 3 --request-changes -b "Додай джерело до цифри X"
```
Також можна на сайті: **Pull requests → Files changed → Review changes**. Зливає PR **автор** після погодження: `gh pr merge 3 --squash --delete-branch` або кнопкою на сайті.

### 2.4. Без терміналу
Невелику правку можна зробити прямо на сайті:
1. Відкрий файл → ✏️ **Edit this file**.
2. Внеси зміни → **Commit changes…**.
3. Обери **Create a new branch… and start a pull request** → **Propose changes** → **Create pull request**.

---

## 3. Як не заважати одне одному
- **Одна тема — одна гілка — один PR.** Невеликі PR швидше перевіряти.
- **Перед роботою — завжди** `git switch main && git pull`.
- **Чужий документ** не переписуємо повністю. Додаємо розділ або точкову правку і пишемо рядок у «Журнал змін» внизу документа.
- **Великі зміни в чужому документі** спершу погоджуємо з автором у чаті.
- **Хто над чим працює** — пишемо в чат команди, щоб двоє не редагували той самий файл одночасно.

## 4. Якщо щось пішло не так

| Ситуація | Що робити |
|---|---|
| `protected branch` / `Changes must be made through a pull request` | Так і має бути: працюй у своїй гілці й відкрий PR |
| `Permission denied` при `push` | Не прийняв запрошення або не увійшов через `gh auth login` |
| Конфлікт при `pull` або в PR | `git pull --rebase origin main` → виправ позначені місця → `git add` → `git rebase --continue`. Або попроси агента розв'язати конфлікт, не видаляючи чужого тексту |
| Закомітив секрет | **Не пуш.** Якщо вже запушив — одразу пиши Юрію. Сам ключ чи пароль треба змінити, бо репозиторій публічний |
| Агент хоче пушити в `main` або витратити кредити AppKittie | Зупини його й нагадай про `AGENTS.md` |
