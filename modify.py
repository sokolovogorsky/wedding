import re

with open('index_2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS injection
mosaic_css = '''
        /* ===== INFO MOSAIC ===== */
        .info-mosaic-section {
            background: var(--alabaster);
            padding: 6rem 2rem;
        }
        .info-mosaic-grid {
            max-width: 1100px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
        }
        .mosaic-card {
            background: var(--white);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 3rem 2.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.02);
            display: flex;
            flex-direction: column;
        }
        .mosaic-card.full-width {
            grid-column: 1 / -1;
            align-items: center;
            text-align: center;
        }
        .mosaic-card.center-text {
            text-align: center;
            align-items: center;
        }
        .mosaic-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.2rem;
            color: var(--text-primary);
            margin-bottom: 2rem;
            text-align: center;
        }
        .mosaic-card p {
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        
        /* Map adjustments */
        .mosaic-map {
            width: 100%;
            height: 220px;
            border-radius: 8px;
            overflow: hidden;
            margin-top: 1.5rem;
            border: 1px solid var(--border);
        }
        .mosaic-map iframe {
            width: 100%; height: 100%; border: 0;
            filter: grayscale(60%) contrast(1.05);
        }
        
        @media (max-width: 768px) {
            .info-mosaic-grid { grid-template-columns: 1fr; }
            .mosaic-card { padding: 2rem 1.5rem; }
        }
'''

content = content.replace('/* ===== FOOTER ===== */', mosaic_css + '\n        /* ===== FOOTER ===== */')

# HTML injection
mosaic_html = '''    <!-- Info Mosaic Section -->
    <section class="info-mosaic-section">
        <div class="info-mosaic-grid">
            
            <!-- Countdown -->
            <div class="mosaic-card full-width reveal">
                <h2 class="mosaic-title">До нашего торжества</h2>
                <div class="countdown-grid" style="margin-top:0;">
                    <div class="countdown-card">
                        <span class="countdown-number" id="days">---</span>
                        <span class="countdown-label">дней</span>
                    </div>
                    <div class="countdown-card">
                        <span class="countdown-number" id="hours">--</span>
                        <span class="countdown-label">часов</span>
                    </div>
                    <div class="countdown-card">
                        <span class="countdown-number" id="minutes">--</span>
                        <span class="countdown-label">минут</span>
                    </div>
                    <div class="countdown-card">
                        <span class="countdown-number" id="seconds">--</span>
                        <span class="countdown-label">секунд</span>
                    </div>
                </div>
            </div>

            <!-- Program -->
            <div class="mosaic-card reveal">
                <h2 class="mosaic-title">Программа дня</h2>
                <div class="program-grid" style="max-width: 100%; margin:0;">
                    <div class="program-item">
                        <div class="program-time">15:00</div>
                        <div>
                            <div class="program-title">Сбор гостей</div>
                            <div class="program-desc">Фуршет и welcome-напитки</div>
                        </div>
                    </div>
                    <div class="program-item">
                        <div class="program-time">16:00</div>
                        <div>
                            <div class="program-title">Церемония</div>
                            <div class="program-desc">Торжественная выездная регистрация</div>
                        </div>
                    </div>
                    <div class="program-item">
                        <div class="program-time">17:00</div>
                        <div>
                            <div class="program-title">Банкет</div>
                            <div class="program-desc">Праздничный ужин и поздравления</div>
                        </div>
                    </div>
                    <div class="program-item">
                        <div class="program-time">19:30</div>
                        <div>
                            <div class="program-title">Вечеринка</div>
                            <div class="program-desc">Танцы и веселье до утра</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Venue -->
            <div class="mosaic-card reveal">
                <h2 class="mosaic-title">Локация</h2>
                <div class="venue-info" style="padding:0; text-align:center; box-shadow:none; border:none; background:transparent;">
                    <h3 class="venue-name" style="font-size: 1.5rem;">Резиденция «Мария»</h3>
                    <p class="venue-address">г. Энгельс, ул. Пятница, 7</p>
                </div>
                <!-- Yandex Map -->
                <div class="mosaic-map">
                    <iframe src="https://yandex.ru/map-widget/v1/?text=Энгельс,+улица+Пятницкая,+7,+Резиденция+Мария&z=16" allowfullscreen="true"></iframe>
                </div>
            </div>

            <!-- Dresscode -->
            <div class="mosaic-card center-text reveal">
                <h2 class="mosaic-title">Дресс-код</h2>
                <p>Мы будем рады, если ваш наряд будет в тёплых, приглушённых тонах.</p>
                <div class="dresscode-palette" style="margin-top: 1rem;">
                    <div class="color-swatch" style="background: #D4C5B9;"></div>
                    <div class="color-swatch" style="background: #C8B8A9;"></div>
                    <div class="color-swatch" style="background: #E8DDD3;"></div>
                    <div class="color-swatch" style="background: #8B8178;"></div>
                    <div class="color-swatch" style="background: #1A1A1A;"></div>
                </div>
            </div>

            <!-- Gifts -->
            <div class="mosaic-card center-text reveal">
                <h2 class="mosaic-title">О подарках</h2>
                <p>Мы будем рады разделить этот день с вами!</p>
                <p>Пожалуйста, не дарите нам живые цветы — они быстро завянут, а нам будет сложно забрать их после праздника.</p>
                <p>Вместо этого мы будем очень рады бутылочке вашего любимого вина. Как-нибудь вечером мы откроем её на дегустации под чтение стихов и с теплом вспомним нашу свадьбу.</p>
            </div>

        </div>
    </section>

    <!-- RSVP Section -->'''

# Remove old sections
content = re.sub(r'<!-- Countdown -->.*?<!-- RSVP Section -->', mosaic_html, content, flags=re.DOTALL)

with open('index_2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification done!")
