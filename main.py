import flet as ft

def main(page: ft.Page):
    page.title = "SULTAN AI 🦁"
    page.bgcolor = "#000814"  # أزرق ملكي غامق
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 800
    
    # واجهة السلطان (السيغما)
    logo = ft.Icon(name=ft.icons.EMOJI_NATURE, color="#FFD700", size=100)
    title = ft.Text("SULTAN AI - الرفيق الذكي", size=28, weight="bold", color="#FFD700")
    
    # نظام الـ 35 ميزة (البرمجة، المال، الأتمتة)
    features_info = ft.Text(
        "نظام متكامل: برمجة (Python/JS) | إدارة أموال | أتمتة (MacroDroid/n8n) | عقلية السيغما",
        color="white70", text_align="center"
    )

    def on_login_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("مرحباً بك يا سلطان، جاري تشغيل الأنظمة الـ 35... 🦁"))
        page.snack_bar.open = True
        page.update()

    fingerprint = ft.IconButton(
        icon=ft.icons.FINGERPRINT,
        icon_color="#FFD700",
        icon_size=80,
        on_click=on_login_click
    )

    page.add(
        ft.Column([
            ft.Container(height=50),
            logo,
            title,
            ft.Container(content=features_info, padding=20),
            ft.Divider(color="#FFD700", height=40),
            ft.Text("ضع بصمتك للوصول إلى هدف $1000 يومياً", color="white", weight="bold"),
            ft.Container(height=20),
            fingerprint,
            ft.Text("حصري للسلطان فقط", color="#FFD700", size=12)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)

